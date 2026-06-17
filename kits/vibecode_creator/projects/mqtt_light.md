# IoT遙距點燈

<figure><img src="../../../.gitbook/assets/網絡時鐘.png" alt=""><figcaption></figcaption></figure>

## 模型搭建說明書

{% file src="../../../.gitbook/assets/網絡時鐘.pdf" %}

## 範例生成指令詞

{% hint style="info" %}
範例程式使用了Makercloud平台
{% endhint %}

```
寫一個程式，連接MQTT MQTT伺服器是mqtt.makercloud.scaleinnotech.com，MQTT話題是xxxxxx 當用家按A時發送訊息hello，按B發送kittenbot 將收到的話題訊息顯示在屏幕

創建另一個程式，當主題收到顏色例如red/blue，就將彩燈設為相應顏色
```

在對話中加入以下模塊：聯網及MQTT

<figure><img src="../../../.gitbook/assets/image (284).png" alt=""><figcaption></figcaption></figure>

## 範例程式

```python
from screen import Screen
from uwifi import WIFI
from wifi import *
from future import NeoPixel
from board import *

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
BG_COLOR = 0x000000

# 初始化彩灯
np = NeoPixel("NEOPIX", 3)

# ============ WiFi 配置 ============
WIFI_NAME = ''        # WiFi 名称，留空则使用系统自动连接
WIFI_PASSWORD = ''    # WiFi 密码
# ===================================

# MQTT 配置
MQTT_SERVER = 'mqtt.makercloud.scaleinnotech.com'
MQTT_TOPIC = 'xxxx'
DEVICE_NAME = 'kittenbot_color'

# 颜色映射
COLORS = {
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'purple': (255, 0, 255),
    'cyan': (0, 255, 255),
    'white': (255, 255, 255),
    'orange': (255, 165, 0),
    'off': (0, 0, 0)
}

# 当前颜色
current_color = "未設置"
color_time = 0

# 计算居中坐标函数
def get_center_position(text, size=1, screen_w=160, screen_h=128):
    chinese_w, english_w, number_w, space_w, char_h = 12, 7, 7, 6, 12
    total_width = 0
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            total_width += chinese_w
        elif ch.isdigit():
            total_width += number_w
        elif ch == ' ':
            total_width += space_w
        else:
            total_width += english_w
    w, h = total_width * size, char_h * size
    x, y = (screen_w - w) // 2, (screen_h - h) // 2
    return x, y, w, h

# 设置彩灯颜色
def set_led_color(color_name):
    """根据颜色名称设置彩灯"""
    color_name = color_name.lower().strip()
    
    if color_name in COLORS:
        color_rgb = COLORS[color_name]
        np.setColorAll(color_rgb)
        np.setbrightness(80)
        np.update()
        return color_name
    else:
        return "未知顏色"

# 检查并连接 WiFi
def connect_to_wifi():
    if not isconnected():
        s.rect(0, 0, 160, 128, BG_COLOR, 1)
        x, y, w, h = get_center_position("MQTT彩燈", 2)
        s.text("MQTT彩燈", x, 30, 2, 0xFFFFFF)
        x, y, w, h = get_center_position("連接WiFi...", 1)
        s.text("連接WiFi...", x, 80, 1, 0xFFFF00)
        s.refresh()
        
        if WIFI_NAME:
            connect_wifi(WIFI_NAME, WIFI_PASSWORD)
        else:
            try_auto_connect()

# 初始化WiFi和MQTT
connect_to_wifi()

s.rect(0, 0, 160, 128, BG_COLOR, 1)
x, y, w, h = get_center_position("MQTT彩燈", 2)
s.text("MQTT彩燈", x, 30, 2, 0xFFFFFF)
x, y, w, h = get_center_position("連接MQTT...", 1)
s.text("連接MQTT...", x, 80, 1, 0xFFFF00)
s.refresh()

# 连接MQTT服务器
wifi = WIFI()
try:
    wifi.mqttConnect(MQTT_SERVER, DEVICE_NAME, '', '')
    wifi.subscribe(MQTT_TOPIC)
    print(f"MQTT已連接: {MQTT_SERVER}")
    print(f"已訂閱話題: {MQTT_TOPIC}")
except Exception as e:
    print(f"MQTT連接失敗: {e}")
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    x, y, w, h = get_center_position("連接失敗", 2)
    s.text("連接失敗", x, 50, 2, 0xFF0000)
    s.refresh()
    import time
    time.sleep(2)

# 主循环
while True:
    # 接收消息
    msg = wifi.getMessage(MQTT_TOPIC)
    if msg:
        print(f"收到: {msg}")
        # 设置颜色
        result = set_led_color(msg)
        current_color = result
        color_time = 0
    
    # 更新显示时间
    if color_time < 100:  # 显示约10秒
        color_time += 1
    else:
        if current_color == "未知顏色":
            current_color = "等待顏色..."
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("MQTT彩燈控制", 2)
    s.text("MQTT彩燈控制", x, 10, 2, 0xFFFFFF)
    
    # 显示话题
    s.text(f"話題: {MQTT_TOPIC}", 5, 35, 0, 0x00FF00)
    
    # 显示分隔线
    s.line(0, 50, 160, 50, 0x444444)
    
    # 显示当前颜色
    s.text("當前顏色:", 5, 60, 0, 0xFFFF00)
    
    # 显示颜色名称
    if current_color:
        x, y, w, h = get_center_position(current_color, 1)
        s.text(current_color, x, 80, 1, 0xFFFFFF)
    else:
        x, y, w, h = get_center_position("等待顏色...", 1)
        s.text("等待顏色...", x, 80, 1, 0x888888)
    
    # 显示支持的颜色
    s.text("支持的顏色:", 5, 100, 0, 0x888888)
    supported = "red blue green yellow"
    s.text(supported, 5, 112, 0, 0x666666)
    s.text("purple cyan white off", 5, 124, 0, 0x666666)
    
    # 显示连接状态
    if isconnected():
        s.text("WiFi: 已連接", 95, 5, 0, 0x00FF00)
    else:
        s.text("WiFi: 未連接", 95, 5, 0, 0xFF0000)
    
    # 刷新屏幕
    s.refresh()
```

{% file src="../../../.gitbook/assets/mqtt_color_control.py" %}

## 示範短片

{% embed url="https://drive.google.com/file/d/1NWCfrNsXyMdRmw8JlGccrOAkBs6k2Id5/view?usp=drive_link" %}
