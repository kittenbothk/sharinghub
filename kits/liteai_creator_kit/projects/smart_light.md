# 智能電筒

<figure><img src="../../../.gitbook/assets/網絡時鐘.png" alt=""><figcaption></figcaption></figure>

## 模型搭建說明書

{% file src="../../../.gitbook/assets/網絡時鐘.pdf" %}

## 範例生成指令詞

```
幫我寫一個智能手電筒程式，因應環境亮度控制彩燈的亮度
```

## 範例程式

```python
from sensor import Sensor
from future import NeoPixel
from screen import Screen

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
BG_COLOR = 0x000000

# 初始化传感器和彩灯
sensor = Sensor()
np = NeoPixel("NEOPIX", 3)

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

# 主循环
last_brightness = -1  # 记录上次的亮度，避免重复设置

while True:
    # 读取环境亮度
    light_value = sensor.getLight()
    
    # 计算彩灯亮度（环境越暗，彩灯越亮）
    # 光敏值范围0-4095，彩灯亮度0-100
    # 使用反比例：亮度 = (4095 - 光敏值) / 4095 * 100
    brightness = int((4095 - light_value) / 4095 * 100)
    
    # 限制亮度范围
    if brightness < 0:
        brightness = 0
    elif brightness > 100:
        brightness = 100
    
    # 只有亮度变化时才设置（优化性能）
    if brightness != last_brightness:
        # 设置彩灯为白色
        np.setColorAll((255, 255, 255))
        # 设置亮度
        np.setbrightness(brightness)
        # 更新显示
        np.update()
        last_brightness = brightness
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("智能手电筒", 2)
    s.text("智能手电筒", x, 20, 2, 0xFFFFFF)
    
    # 显示环境亮度
    s.text("环境亮度:", 10, 50, 1, 0x00FF00)
    s.text(f"{light_value}", 70, 50, 1, 0x00FF00)
    
    # 显示彩灯亮度
    s.text("灯光亮度:", 10, 70, 1, 0xFFFF00)
    s.text(f"{brightness}%", 70, 70, 1, 0xFFFF00)
    
    # 根据亮度显示状态
    if brightness == 0:
        status = "关闭"
        status_color = 0x888888
    elif brightness < 30:
        status = "微亮"
        status_color = 0x00FFFF
    elif brightness < 70:
        status = "适中"
        status_color = 0xFFFF00
    else:
        status = "最亮"
        status_color = 0xFF0000
    
    x, y, w, h = get_center_position(status, 1)
    s.text(status, x, 100, 1, status_color)
    
    # 刷新屏幕
    s.refresh()
```

{% file src="../../../.gitbook/assets/smart_flashlight.py" %}

## 示範短片

{% embed url="https://drive.google.com/file/d/1CUMoRIcH-3iGnRvaBZz-MABchsECdHDd/view?usp=drive_link" %}
