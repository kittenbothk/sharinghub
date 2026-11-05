import urequests
import utime
from wifi import *
from sensor import Sensor
from screen import Screen

import json

def form_encode(value):
    return "".join(
        chr(b) if (
            65 <= b <= 90 or 97 <= b <= 122
            or 48 <= b <= 57 or b in b"-._~"
        ) else "%%%02X" % b
        for b in value.encode("utf-8")
    )


def get_access_token():
    with open("token.json") as f:
        credentials = json.load(f)

    fields = {
        "client_id": credentials["client_id"],
        "client_secret": credentials["client_secret"],
        "refresh_token": credentials["refresh_token"],
        "grant_type": "refresh_token",
    }

    body = "&".join(
        form_encode(key) + "=" + form_encode(value)
        for key, value in fields.items()
    )

    response = urequests.post(
        "https://oauth2.googleapis.com/token",
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        },
        data=body,
    )

    try:
        result = response.json()
        if response.status_code != 200:
            raise RuntimeError(
                "Token refresh failed: "
                + str(result.get("error", response.status_code))
            )

        return result["access_token"]
    finally:
        response.close()

# ============ WiFi 配置 ============
WIFI_NAME = ''        # WiFi 名称，留空则使用系统自动连接
WIFI_PASSWORD = ''    # WiFi 密码
# ===================================

# 连接WiFi
if not isconnected():
    if WIFI_NAME:
        connect_wifi(WIFI_NAME, WIFI_PASSWORD)
    else:
        try_auto_connect()

SPREADSHEET_ID = "SHEET ID"
SHEET_NAME = "Sheet1"  # 试算表名称，用户可自行修改

# Search for the existing table in the sheet columns A:B.
# 注意：表名中的 "!" 需转义为 %21
url = (
    "https://sheets.googleapis.com/v4/spreadsheets/"
    + SPREADSHEET_ID
    + "/values/"
    + form_encode(SHEET_NAME) + "%21A%3AB:append"
    + "?valueInputOption=USER_ENTERED"
    + "&insertDataOption=INSERT_ROWS"
)

sensors = Sensor()

# 初始化屏幕
screens = Screen()
screens.autoRefresh(False)
BG_COLOR = 0x000000


def show_light(light_value):
    """在屏幕上显示当前亮度读数"""
    screens.rect(0, 0, 160, 128, BG_COLOR, 1)
    screens.text('Brightness:', 38, 40, 1, 0xFFFFFF)
    screens.text(str(light_value), 80, 60, 2, 0x00FF00)
    screens.text('Log every 2s', 45, 100, 1, 0x888888)
    screens.refresh()


def log_reading(light_value):
    """记录当前时间与亮度数值到表格"""
    now = utime.localtime()
    time_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        now[0], now[1], now[2], now[3], now[4], now[5])

    response = urequests.post(
        url,
        headers={
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
        },
        json={
            "majorDimension": "ROWS",
            "values": [[time_str, light_value]],
        },
    )

    try:
        if 200 <= response.status_code < 300:
            result = response.json()
            print("Added:", result["updates"]["updatedRange"])
        else:
            print("Error:", response.status_code, response.text)
    finally:
        response.close()

access_token = get_access_token()
# 主循环：每10秒记录一次亮度数值
while True:
    light = sensors.getLight()
    show_light(light)  # 屏幕显示当前亮度
    log_reading(light)
    utime.sleep(2)