from screen import Screen
from sonar import MeowSonar
from future import geekservo9g
from board import *
import time

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
s.setBrightness(1)
BG_COLOR = 0x000000

# 初始化超声波传感器（P2端口）
sonar = MeowSonar('P2')

# 舵机角度（使用geekservo9g函数）
SERVO_DOWN = 0   # 闸门落下（0度，允许通行）
SERVO_UP = 90    # 闸门升起（90度，阻挡通行）

# 设置初始舵机角度
geekservo9g('P1', SERVO_DOWN)

# 停车场参数
DETECT_DISTANCE = 5  # 检测距离（厘米）
TOTAL_SPOTS = 3        # 总车位数

# 停车位状态（True=占用，False=空闲）
parking_spots = [False, False, False]

# 闸门状态
gate_raised = False  # 闸门是否升起
gate_timer = 0       # 闸门计时器

# 车辆检测状态
vehicle_detected = False
vehicle_entering = False

# 舵机初始状态（闸门落下）
#servo.setAnalog(SERVO_DOWN)

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

# 获取可用车位数量
def get_available_spots():
    return parking_spots.count(False)

# 获取第一个空闲车位编号（1-3）
def get_first_available_spot():
    for i, occupied in enumerate(parking_spots):
        if not occupied:
            return i + 1  # 返回1-3
    return -1  # 无可用车位

# 车辆进入
def vehicle_enter():
    global gate_raised, gate_timer, vehicle_entering
    
    available_spots = get_available_spots()
    
    if available_spots > 0:
        # 有空位，允许进入
        spot_number = get_first_available_spot()
        parking_spots[spot_number - 1] = True
        
        # 升起闸门
        gate_raised = True
        gate_timer = time.ticks_ms()
        geekservo9g('P1', SERVO_UP)
        
        vehicle_entering = True
        print(f"Vehicle entered, occupied spot {spot_number}")
        return spot_number
    else:
        # 无空位，闸门保持落下
        print("No available spots, gate closed")
        return -1

# 车辆离开（通过按键模拟）
def vehicle_leave(spot_number):
    if 1 <= spot_number <= 3:
        if parking_spots[spot_number - 1]:
            parking_spots[spot_number - 1] = False
            print(f"Vehicle left, spot {spot_number} released")
            return True
    return False

# 绘制停车位示意图
def draw_parking_spots():
    spot_width = 45
    spot_height = 30
    start_x = 5
    start_y = 45
    gap = 5
    
    for i in range(TOTAL_SPOTS):
        x = start_x + i * (spot_width + gap)
        y = start_y
        
        # 绘制车位边框
        border_color = 0xFF0000 if parking_spots[i] else 0x00FF00
        s.rect(x, y, spot_width, spot_height, border_color, 0)
        
        # 绘制车位编号
        s.text(f"{i + 1}", x + spot_width // 2 - 3, y + 5, 1, border_color)
        
        # 绘制车位状态
        if parking_spots[i]:
            # 占用状态
            s.text("滿", x + spot_width // 2 - 6, y + 15, 1, 0xFFFF00)
        else:
            # 空闲状态
            s.text("空", x + spot_width // 2 - 6, y + 15, 1, 0x00FF00)

# 绘制闸门示意图
def draw_gate():
    center_x = 80
    center_y = 95
    
    # 绘制闸门框
    s.rect(center_x - 30, center_y - 15, 60, 30, 0x888888, 0)
    
    # 绘制闸门
    if gate_raised:
        # 闸门升起
        s.line(center_x - 28, center_y + 13, center_x - 28, center_y - 13, 0xFF0000)
        s.text("閘門", center_x - 4, center_y - 7, 1, 0xFF0000)
        gate_text = "閘門升起"
        gate_color = 0xFF0000
    else:
        # 闸门落下
        s.line(center_x - 28, center_y + 13, center_x + 28, center_y + 13, 0x00FF00)
        s.text("閘門", center_x - 4, center_y - 7, 1, 0x00FF00)
        gate_text = "閘門落下"
        gate_color = 0x00FF00
    
    return gate_text, gate_color

# 上次按键状态
last_btn = None
last_vehicle_detected = False

# 主循环
while True:
    current_time = time.ticks_ms()
    
    # 读取超声波距离
    distance = sonar.checkdist('cm')
    
    # 检测车辆
    is_detected = distance < DETECT_DISTANCE if distance <= 340 else False
    
    # 车辆进入检测（边沿触发）
    if is_detected and not last_vehicle_detected:
        vehicle_enter()
    
    last_vehicle_detected = is_detected
    
    # 检测按键（模拟车辆离开）
    btn = read_button()
    if btn == 1 and last_btn != 1:
        # A键：车位1车辆离开
        if vehicle_leave(1):
            pass
    elif btn == 2 and last_btn != 2:
        # M键：车位2车辆离开
        if vehicle_leave(2):
            pass
    elif btn == 3 and last_btn != 3:
        # B键：车位3车辆离开
        if vehicle_leave(3):
            pass
    
    last_btn = btn
    
    # 闸门自动落下（3秒后）
    if gate_raised and time.ticks_diff(current_time, gate_timer) >= 3000:
        gate_raised = False
        geekservo9g('P1', SERVO_DOWN)
        print("Gate lowered after 3 seconds")
    
    # 车辆离开检测区后重置进入状态
    if not is_detected and vehicle_entering:
        vehicle_entering = False
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("智能停車場", 2)
    s.text("智能停車場", x, 5, 2, 0xFFFFFF)
    
    # 显示可用车位
    available = get_available_spots()
    available_color = 0x00FF00 if available > 0 else 0xFF0000
    s.text(f"空位: {available}/{TOTAL_SPOTS}", 5, 28, 0, available_color)
    
    # 显示距离
    if distance <= 340:
        s.text(f"距離: {distance:.1f}cm", 100, 28, 0, 0x888888)
    else:
        s.text("距離: --", 100, 28, 0, 0x888888)
    
    # 绘制停车位
    draw_parking_spots()
    
    # 绘制闸门
    gate_text, gate_color = draw_gate()
    s.text(gate_text, 5, 85, 0, gate_color)
    
    # 显示分隔线
    s.line(0, 108, 160, 108, 0x444444)
    
    # 显示控制提示
    s.text("A:車位1  M:車位2  B:車位3", 5, 113, 0, 0xAAAAAA)
    s.text("按鍵釋放車位", 5, 120, 0, 0x888888)
    
    # 刷新屏幕
    s.refresh()
    
    # 短暂延迟
    time.sleep(0.5)
