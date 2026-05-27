# 感應夜燈

<figure><img src="../../../.gitbook/assets/網絡時鐘.png" alt=""><figcaption></figcaption></figure>

## 模型搭建說明書

{% file src="../../../.gitbook/assets/網絡時鐘.pdf" %}

## 範例生成指令詞

```
寫一個小夜燈程式，當P3的人體紅外線感應器感應到有人走過就亮起彩燈。
```

在對話中加入以下模塊：人體紅外感應器

<figure><img src="../../../.gitbook/assets/image (275).png" alt=""><figcaption></figcaption></figure>

## 範例程式

```python
from screen import Screen
from sugar import PIR
from future import NeoPixel
from board import *
import time

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
s.setBrightness(1)
BG_COLOR = 0x000000

# 初始化PIR传感器（P3端口）
pir = PIR('P3')

# 初始化板载RGB LED（3颗）
np = NeoPixel("NEOPIX", 3)
np.setbrightness(80)
np.setColorAll((0, 0, 0))
np.update()

# 小夜灯参数
LIGHT_DURATION = 5  # 灯光持续时间（秒）

# 灯光状态
light_on = False
light_timer = 0
color_index = 0

# 彩色灯效（RGB颜色）
colors = [
    (255, 0, 0),      # 红色
    (255, 128, 0),    # 橙色
    (255, 255, 0),    # 黄色
    (0, 255, 0),      # 绿色
    (0, 255, 255),    # 青色
    (0, 0, 255),      # 蓝色
    (128, 0, 255),    # 紫色
    (255, 0, 255),    # 粉色
]

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

# 绘制灯光效果
def draw_light():
    center_x = 80
    center_y = 70
    radius = 30
    
    if light_on:
        # 绘制光芒效果
        color = colors[color_index]
        
        # 外圈光芒
        for i in range(8):
            angle = i * 45
            import math
            rad = angle * math.pi / 180
            x1 = center_x + radius * math.cos(rad)
            y1 = center_y - radius * math.sin(rad)
            x2 = center_x + (radius + 10) * math.cos(rad)
            y2 = center_y - (radius + 10) * math.sin(rad)
            s.line(int(x1), int(y1), int(x2), int(y2), color)
        
        # 绘制灯泡主体
        s.circle(center_x, center_y, radius, color, 0)
        
        # 内圈
        s.circle(center_x, center_y, radius - 8, 0xFFFFFF, 0)
        
        # 中心点
        s.circle(center_x, center_y, 5, color, 1)
        
        light_text = "燈光開啟"
        light_color = color
    else:
        # 绘制关闭的灯泡
        s.circle(center_x, center_y, radius, 0x333333, 0)
        s.circle(center_x, center_y, radius - 8, 0x222222, 0)
        s.circle(center_x, center_y, 5, 0x444444, 1)
        
        light_text = "燈光關閉"
        light_color = 0x888888
    
    return light_text, light_color

# 主循环
while True:
    current_time = time.ticks_ms()
    
    # 读取PIR传感器
    pir_value = pir.value()
    
    # 检测到人
    if pir_value == 1:
        if not light_on:
            light_on = True
            light_timer = current_time
            color_index = (color_index + 1) % len(colors)
            # 亮起彩灯
            np.setColorAll(colors[color_index])
            np.update()
            print(f"Motion detected, light ON: {colors[color_index]}")
        else:
            # 持续检测到人，重置计时器
            light_timer = current_time
    
    # 灯光持续时间结束
    if light_on and time.ticks_diff(current_time, light_timer) >= LIGHT_DURATION * 1000:
        light_on = False
        # 关闭灯光
        np.setColorAll((0, 0, 0))
        np.update()
        print("Light OFF")
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("小夜燈", 2)
    s.text("小夜燈", x, 5, 2, 0xFFFFFF)
    
    # 显示PIR状态
    if pir_value == 1:
        pir_text = "PIR: 檢測到人"
        pir_color = 0xFFFF00
    else:
        pir_text = "PIR: 無人"
        pir_color = 0x888888
    s.text(pir_text, 5, 28, 0, pir_color)
    
    # 显示端口
    s.text("P3端口", 5, 38, 0, 0x888888)
    
    # 绘制灯光效果
    light_text, light_color = draw_light()
    
    # 显示灯光状态
    x, y, w, h = get_center_position(light_text, 1)
    s.text(light_text, x, 110, 1, light_color)
    
    # 显示剩余时间
    if light_on:
        remaining = LIGHT_DURATION - time.ticks_diff(current_time, light_timer) // 1000
        if remaining > 0:
            s.text(f"剩餘: {remaining}秒", 5, 118, 0, 0xAAAAAA)
    
    # 刷新屏幕
    s.refresh()
    
    # 短暂延迟
    time.sleep(0.05)

```

{% file src="../../../.gitbook/assets/night_light.py" %}

## 示範短片

{% embed url="https://drive.google.com/file/d/1BCiwL26PZfjcAS4M7w1I8rJIqHGq60Iw/view?usp=drive_link" %}
