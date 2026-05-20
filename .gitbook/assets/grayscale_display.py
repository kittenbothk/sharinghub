from sugar import Grayscale
from screen import Screen

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
BG_COLOR = 0x000000

# 初始化灰度传感器
sensor = Grayscale('P3')

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
while True:
    # 读取灰度值
    value = sensor.value()
    
    # 根据灰度值计算距离（线性插值）
    # 0cm -> 3100, 11cm -> 980
    # 公式：distance = (3100 - value) * 11 / 2120
    if value >= 3100:
        distance = 0
    elif value <= 980:
        distance = 11
    else:
        distance = (3100 - value) * 11 / 2120
    
    # 判断表面类型
    if value < 1000:
        surface = "黑色"
        surface_color = 0x000000
    elif value < 2000:
        surface = "深色"
        surface_color = 0x004400
    elif value < 3000:
        surface = "淺色"
        surface_color = 0x444400
    else:
        surface = "白色"
        surface_color = 0xFFFFFF
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("灰度感應器", 2)
    s.text("灰度感應器", x, 15, 2, 0xFFFFFF)
    
    # 显示传感器数值
    x, y, w, h = get_center_position(f"数值: {value}", 1)
    s.text(f"数值: {value}", x, 45, 1, 0x00FF00)
    
    # 显示估算距离（整数）
    x, y, w, h = get_center_position(f"數值: {int(distance)}cm", 2)
    s.text(f"數值: {int(distance)}cm", x, 70, 2, 0xFFFF00)
    
    # 显示表面类型
    x, y, w, h = get_center_position(f"表面: {surface}", 1)
    s.text(f"表面: {surface}", x, 105, 1, surface_color)
    
    # 刷新屏幕
    s.refresh()