# 網絡時鐘

<figure><img src="../../../.gitbook/assets/網絡時鐘.png" alt=""><figcaption></figcaption></figure>

## 模型搭建說明書

{% file src="../../../.gitbook/assets/網絡時鐘.pdf" %}

## 範例生成指令詞

```
創作一個網絡時鐘程式
加入使用時鐘圖像顯示時間
```

在對話中加入以下模塊：網路時間

<figure><img src="../../../.gitbook/assets/image (271).png" alt=""><figcaption></figcaption></figure>

## 範例程式

```python
from screen import Screen
from wifi import *
import ntptime
import utime
import math

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
BG_COLOR = 0x000000

# ============ WiFi 配置 ============
WIFI_NAME = 'hello'        # WiFi 名称，留空则使用系统自动连接
WIFI_PASSWORD = '12345678'    # WiFi 密码
# ===================================

# 时钟参数
CLOCK_CENTER_X = 80
CLOCK_CENTER_Y = 75
CLOCK_RADIUS = 50

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

# 绘制时钟
def draw_clock(hour, minute, second):
    # 绘制表盘外圈
    s.circle(CLOCK_CENTER_X, CLOCK_CENTER_Y, CLOCK_RADIUS, 0xFFFFFF, 0)
    s.circle(CLOCK_CENTER_X, CLOCK_CENTER_Y, CLOCK_RADIUS - 3, 0x888888, 0)
    
    # 绘制刻度
    for i in range(12):
        angle = (i * 30) * math.pi / 180
        # 小时刻度
        x1 = int(CLOCK_CENTER_X + (CLOCK_RADIUS - 10) * math.sin(angle))
        y1 = int(CLOCK_CENTER_Y - (CLOCK_RADIUS - 10) * math.cos(angle))
        x2 = int(CLOCK_CENTER_X + (CLOCK_RADIUS - 3) * math.sin(angle))
        y2 = int(CLOCK_CENTER_Y - (CLOCK_RADIUS - 3) * math.cos(angle))
        s.line(x1, y1, x2, y2, 0xFFFFFF)
        
        # 分钟刻度
        for j in range(4):
            sub_angle = ((i * 30) + (j + 1) * 6) * math.pi / 180
            x3 = int(CLOCK_CENTER_X + (CLOCK_RADIUS - 5) * math.sin(sub_angle))
            y3 = int(CLOCK_CENTER_Y - (CLOCK_RADIUS - 5) * math.cos(sub_angle))
            x4 = int(CLOCK_CENTER_X + (CLOCK_RADIUS - 3) * math.sin(sub_angle))
            y4 = int(CLOCK_CENTER_Y - (CLOCK_RADIUS - 3) * math.cos(sub_angle))
            s.line(x3, y3, x4, y4, 0x666666)
    
    # 计算指针角度
    # 秒针角度
    second_angle = (second / 60) * 360
    # 分针角度
    minute_angle = (minute / 60) * 360 + (second / 60) * 6
    # 时针角度（12小时制）
    hour_angle = ((hour % 12) / 12) * 360 + (minute / 60) * 30
    
    # 绘制时针
    hour_rad = hour_angle * math.pi / 180
    hour_len = CLOCK_RADIUS * 0.5
    hx = int(CLOCK_CENTER_X + hour_len * math.sin(hour_rad))
    hy = int(CLOCK_CENTER_Y - hour_len * math.cos(hour_rad))
    s.line(CLOCK_CENTER_X, CLOCK_CENTER_Y, hx, hy, 0x00FFFF)
    
    # 绘制分针
    minute_rad = minute_angle * math.pi / 180
    minute_len = CLOCK_RADIUS * 0.7
    mx = int(CLOCK_CENTER_X + minute_len * math.sin(minute_rad))
    my = int(CLOCK_CENTER_Y - minute_len * math.cos(minute_rad))
    s.line(CLOCK_CENTER_X, CLOCK_CENTER_Y, mx, my, 0x00FF00)
    
    # 绘制秒针
    second_rad = second_angle * math.pi / 180
    second_len = CLOCK_RADIUS * 0.85
    sx = int(CLOCK_CENTER_X + second_len * math.sin(second_rad))
    sy = int(CLOCK_CENTER_Y - second_len * math.cos(second_rad))
    s.line(CLOCK_CENTER_X, CLOCK_CENTER_Y, sx, sy, 0xFF0000)
    
    # 绘制中心点
    s.circle(CLOCK_CENTER_X, CLOCK_CENTER_Y, 3, 0xFFFFFF, 1)

# 同步网络时间
def sync_time():
    """同步网络时间"""
    # 检查并连接 WiFi
    if not isconnected():
        s.rect(0, 0, 160, 128, BG_COLOR, 1)
        x, y, w, h = get_center_position("網絡時鐘", 2)
        s.text("網絡時鐘", x, 30, 2, 0xFFFFFF)
        x, y, w, h = get_center_position("連接wifi...", 1)
        s.text("連接wifi...", x, 80, 1, 0xFFFF00)
        s.refresh()
        
        # 如果指定了 WiFi 名称，则连接指定 WiFi
        if WIFI_NAME:
            connect_wifi(WIFI_NAME, WIFI_PASSWORD)
        else:
            try_auto_connect()
    
    # 同步时间
    try:
        s.rect(0, 0, 160, 128, BG_COLOR, 1)
        x, y, w, h = get_center_position("網絡時鐘", 2)
        s.text("網絡時鐘", x, 30, 2, 0xFFFFFF)
        x, y, w, h = get_center_position("同步時間...", 1)
        s.text("同步時間...", x, 80, 1, 0xFFFF00)
        s.refresh()
        
        ntptime.sync(tz=8, set_rtc=True)
        print("同步時間成功")
        return True
    except Exception as e:
        print(f"同步時間失败: {e}")
        return False

# 首次同步时间
sync_time()

# 主循环
while True:
    # 获取本地时间
    local_time = utime.localtime()
    
    # 格式化时间
    year = local_time[0]
    month = local_time[1]
    day = local_time[2]
    hour = local_time[3]
    minute = local_time[4]
    second = local_time[5]
    weekday = local_time[6]
    
    # 星期几
    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    weekday_str = weekdays[weekday]
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("網絡時鐘", 1)
    s.text("網絡時鐘", x, 5, 1, 0xFFFFFF)
    
    # 显示日期和星期
    date_str = f"{year}年{month}月{day}日"
    s.text(date_str, 5, 18, 0, 0x00FF00)
    s.text(weekday_str, 5, 25, 0, 0x00FFFF)
    
    # 显示数字时间
    time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
    s.text(time_str, 5, 123, 0, 0xFFFF00)
    
    # 绘制时钟
    draw_clock(hour, minute, second)
    
    # 显示WiFi连接状态
    if isconnected():
        s.text("WiFi", 140, 5, 0, 0x00FF00)
    else:
        s.text("WiFi", 140, 5, 0, 0xFF0000)
    
    # 刷新屏幕
    s.refresh()
    
    # 短暂延迟
    utime.sleep(0.05)
```

{% file src="../../../.gitbook/assets/network_clock_graphic.py" %}

## 示範短片

{% embed url="https://drive.google.com/file/d/1-KKuw_N1wE7NXpQQmeV2gv-6x1UxL2AZ/view?usp=drive_link" %}
