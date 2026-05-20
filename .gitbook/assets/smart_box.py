from screen import Screen
from sonar import MeowSonar
from sugar import Grayscale
from future import geekservo9g
from board import *
import time

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
s.setBrightness(1)
BG_COLOR = 0x000000

# 初始化超声波传感器（P1端口）- 检测手
sonar = MeowSonar('P1')

# 初始化灰度传感器（P3端口）- 检测物品
grayscale = Grayscale('P3')

# 初始化灰度传感器（P4端口）- 显示读数
grayscale_p4 = Grayscale('P4')

# 舵机角度（P2端口）
SERVO_CLOSED = 135      # 关闭箱盖（0度）
SERVO_OPEN = -45    # 打开箱盖（135度）

# 设置初始舵机角度（关闭）
geekservo9g('P2', SERVO_CLOSED)

# 检测参数
HAND_DETECT_DISTANCE = 10  # 手检测距离（厘米）
DETECT_THRESHOLD = 10       # 距离变化阈值
ITEM_THRESHOLD = 100      # 灰度阈值（低于此值表示有物品）

# 箱子状态
box_open = False        # 箱盖是否打开
open_timer = 0          # 打开计时器
has_item = False        # 是否有物品

# 手检测状态
hand_near = False       # 手是否靠近
last_distance = 999     # 上次距离
debounce_count = 0      # 防抖动计数
DEBOUNCE_THRESHOLD = 3  # 防抖动阈值

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

# 检测挥手
def detect_wave():
    global hand_near, last_distance, debounce_count
    
    # 读取距离
    distance = sonar.checkdist('cm')
    
    # 距离无效则跳过
    if distance > 340:
        return False, 999
    
    # 检测手靠近
    if distance < HAND_DETECT_DISTANCE:
        debounce_count += 1
        # 连续检测到才触发
        if debounce_count >= DEBOUNCE_THRESHOLD:
            hand_near = True
            return True, distance
    else:
        # 手离开，重置状态
        if hand_near and debounce_count >= DEBOUNCE_THRESHOLD:
            hand_near = False
            debounce_count = 0
            return True, distance
        debounce_count = 0
    
    last_distance = distance
    return False, distance

# 检测物品
def detect_item():
    global has_item
    
    # 读取灰度值
    gray_value = grayscale.value()
    
    # 判断是否有物品（灰度值低于阈值表示有黑色物品）
    if gray_value < ITEM_THRESHOLD:
        has_item = True
    else:
        has_item = False
    
    return gray_value

# 打开箱盖
def open_box():
    global box_open, open_timer
    
    if not box_open:
        box_open = True
        open_timer = time.ticks_ms()
        geekservo9g('P2', SERVO_OPEN)
        print("Box opened")

# 关闭箱盖
def close_box():
    global box_open
    
    if box_open:
        box_open = False
        geekservo9g('P2', SERVO_CLOSED)
        print("Box closed")

# 绘制箱子示意图
def draw_box():
    # 绘制箱子主体
    box_x = 55
    box_y = 65
    box_width = 50
    box_height = 35
    
    # 箱子边框
    s.rect(box_x, box_y, box_width, box_height, 0x00FFFF, 0)
    
    # 绘制箱盖
    if box_open:
        # 箱盖打开（斜线表示）
        s.line(box_x, box_y, box_x - 20, box_y - 30, 0xFFFF00)
        s.line(box_x + box_width, box_y, box_x + box_width + 20, box_y - 30, 0xFFFF00)
        s.line(box_x - 20, box_y - 30, box_x + box_width + 20, box_y - 30, 0xFFFF00)
        lid_text = "開"
        lid_color = 0xFFFF00
    else:
        # 箱盖关闭（实线表示）
        s.line(box_x, box_y, box_x + box_width, box_y, 0x00FF00)
        lid_text = "關"
        lid_color = 0x00FF00
    
    # 绘制箱内物品
    if has_item:
        s.rect(box_x + 15, box_y + 10, 30, 20, 0xFF0000, 1)
        s.text("📦", box_x + 22, box_y + 12, 1, 0xFFFFFF)
    
    return lid_text, lid_color

# 主循环
while True:
    current_time = time.ticks_ms()
    
    # 检测挥手
    wave_detected, distance = detect_wave()
    
    # 检测到挥手，打开箱盖
    if wave_detected and hand_near and not box_open:
        open_box()
    
    # 检测物品
    gray_value = detect_item()
    
    # 读取P4灰度传感器
    gray_value_p4 = grayscale_p4.value()
    
    # 箱盖自动关闭（5秒后）
    if box_open and time.ticks_diff(current_time, open_timer) >= 5000:
        close_box()
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("智能箱子", 2)
    s.text("智能箱子", x, 5, 2, 0xFFFFFF)
    
    # 显示手检测状态
    if distance < HAND_DETECT_DISTANCE and distance <= 340:
        hand_text = "檢測到手"
        hand_color = 0xFFFF00
    else:
        hand_text = "等待揮手"
        hand_color = 0x888888
    s.text(hand_text, 5, 28, 0, hand_color)
    
    # 显示距离
    if distance <= 340:
        s.text(f"距離: {distance:.1f}cm", 5, 38, 0, 0x888888)
    else:
        s.text("距離: --", 5, 38, 0, 0x888888)
    
    # 显示灰度值
    s.text(f"P3灰度: {gray_value}", 90, 38, 0, 0x888888)
    s.text(f"P4灰度: {gray_value_p4}", 90, 48, 0, 0x888888)
    
    # 绘制箱子
    lid_text, lid_color = draw_box()
    
    # 显示箱盖状态
    s.text(f"箱蓋: {lid_text}", 5, 110, 0, lid_color)
    
    # 显示物品状态
    if has_item:
        item_text = "狀態: 滿"
        item_color = 0xFF0000
    else:
        item_text = "狀態: 空"
        item_color = 0x00FF00
    s.text(item_text, 5, 120, 0, item_color)
    
    # 刷新屏幕
    s.refresh()
    
    # 短暂延迟
    time.sleep(0.05)
