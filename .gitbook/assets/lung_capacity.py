from screen import Screen
from uaudio import Audio
from board import *
import time

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
s.setBrightness(1)
BG_COLOR = 0x000000

# 初始化麦克风
audio = Audio()

# 肺活量检测参数
BLOW_THRESHOLD = 5   # 吹气音量阈值
MIN_BLOW_DURATION = 1  # 最小吹气持续时间（秒）
MAX_BLOW_DURATION = 10 # 最大吹气持续时间（秒）

# 检测状态
is_blowing = False
blow_start_time = 0
blow_duration = 0
max_loudness = 0
total_loudness = 0
sample_count = 0
lung_capacity = 0

# 结果显示
result_shown = False
result_start_time = 0

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

# 计算肺活量（模拟值）
def calculate_lung_capacity(duration, avg_loudness):
    # 模拟公式：持续时间 × 平均音量 / 100
    capacity = duration * avg_loudness / 100
    return int(capacity)

# 肺活量等级评价
def get_capacity_level(capacity):
    if capacity < 2:
        return "偏弱", 0xFF0000
    elif capacity < 4:
        return "一般", 0xFFFF00
    elif capacity < 6:
        return "良好", 0x00FF00
    else:
        return "優秀", 0x00FFFF

# 绘制肺活量条
def draw_capacity_bar(capacity, max_capacity=10):
    bar_width = min(capacity / max_capacity * 140, 140)
    
    # 绘制背景条
    s.rect(10, 90, 140, 20, 0x333333, 1)
    
    # 根据肺活量选择颜色
    if capacity < 2:
        bar_color = 0xFF0000  # 红色
    elif capacity < 5:
        bar_color = 0xFFFF00  # 黄色
    elif capacity < 8:
        bar_color = 0x00FF00  # 绿色
    else:
        bar_color = 0x00FFFF  # 青色
    
    # 绘制肺活量条
    s.rect(10, 90, int(bar_width), 20, bar_color, 1)

# 绘制音量指示器
def draw_volume_indicator(loudness):
    max_volume = 100
    bar_width = min(loudness / max_volume * 140, 140)
    
    # 绘制背景条
    s.rect(10, 65, 140, 10, 0x333333, 1)
    
    # 根据音量选择颜色
    if loudness < BLOW_THRESHOLD:
        bar_color = 0x888888  # 灰色（未达到阈值）
    else:
        bar_color = 0x00FF00  # 绿色（达到阈值）
    
    # 绘制音量条
    s.rect(10, 65, int(bar_width), 10, bar_color, 1)

# 绘制呼吸动画
def draw_breath_animation():
    center_x = 80
    center_y = 100
    radius = 20
    
    if is_blowing:
        # 吹气时：圆圈扩大动画
        elapsed = time.ticks_diff(time.ticks_ms(), blow_start_time) / 1000
        expansion = min(elapsed * 5, 10)
        
        # 绘制多个圆圈
        for i in range(3):
            r = radius + int(expansion) - i * 5
            if r > 0:
                alpha = 255 - i * 80
                color = 0x00FF00
                s.circle(center_x, center_y, r, color, 0)
    else:
        # 等待时：静态圆圈
        s.circle(center_x, center_y, radius, 0x888888, 0)
        s.circle(center_x, center_y, radius - 5, 0x222222, 1)
        s.circle(center_x, center_y, 3, 0x444444, 1)

# 主循环
while True:
    current_time = time.ticks_ms()
    
    # 读取麦克风音量
    loudness = audio.loudness()
    
    # 检测吹气
    if loudness > BLOW_THRESHOLD:
        if not is_blowing:
            # 开始吹气
            is_blowing = True
            blow_start_time = current_time
            max_loudness = loudness
            total_loudness = 0
            sample_count = 0
            print(f"Blowing started, loudness: {loudness}")
    else:
        if is_blowing:
            # 结束吹气
            blow_duration = time.ticks_diff(current_time, blow_start_time) / 1000
            
            # 只有持续时间超过最小值才计算肺活量
            if blow_duration >= MIN_BLOW_DURATION:
                avg_loudness = total_loudness / sample_count if sample_count > 0 else max_loudness
                lung_capacity = calculate_lung_capacity(blow_duration, avg_loudness)
                result_shown = True
                result_start_time = current_time
                print(f"Blowing ended, duration: {blow_duration:.1f}s, avg loudness: {avg_loudness:.0f}, capacity: {lung_capacity}")
            
            is_blowing = False
    
    # 记录吹气数据
    if is_blowing:
        if loudness > max_loudness:
            max_loudness = loudness
        total_loudness += loudness
        sample_count += 1
        
        # 超过最大持续时间自动停止
        if time.ticks_diff(current_time, blow_start_time) >= MAX_BLOW_DURATION * 1000:
            is_blowing = False
            print("Max duration reached")
    
    # 结果显示5秒后重置
    if result_shown and time.ticks_diff(current_time, result_start_time) >= 5000:
        result_shown = False
        lung_capacity = 0
        print("Result reset")
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("肺活量檢測", 2)
    s.text("肺活量檢測", x, 5, 2, 0xFFFFFF)
    
    # 显示状态
    if is_blowing:
        status_text = "吹氣中..."
        status_color = 0x00FF00
        duration = time.ticks_diff(current_time, blow_start_time) / 1000
        duration_text = f"時間: {duration:.1f}秒"
    elif result_shown:
        status_text = "檢測完成"
        status_color = 0x00FFFF
        duration_text = f"時間: {blow_duration:.1f}秒"
    else:
        status_text = "請吹氣"
        status_color = 0x888888
        duration_text = "時間: 0.0秒"
    
    x, y, w, h = get_center_position(status_text, 1)
    s.text(status_text, x, 30, 1, status_color)
    
    # 显示吹气时间
    s.text(duration_text, 5, 118, 0, 0xAAAAAA)
    
    # 显示音量
    s.text(f"音量: {loudness:.0f}", 5, 80, 0, 0x888888)
    
    # 绘制呼吸动画
    draw_breath_animation()
    
    # 绘制音量指示器
    draw_volume_indicator(loudness)
    
    # 显示肺活量结果
    if result_shown:
        # 显示肺活量数值
        x, y, w, h = get_center_position(f"肺活量: {lung_capacity}", 1)
        s.text(f"肺活量: {lung_capacity}", x, 50, 1, 0xFFFFFF)
        
        # 显示等级评价
        level_text, level_color = get_capacity_level(lung_capacity)
        x, y, w, h = get_center_position(f"等級: {level_text}", 1)
        s.text(f"等級: {level_text}", x, 95, 1, level_color)
        
        # 绘制肺活量条
        draw_capacity_bar(lung_capacity)
    else:
        # 显示提示
        x, y, w, h = get_center_position("請吹氣", 1)
        #s.text("請吹氣", x, 80, 1, 0x888888)
    
    # 显示阈值提示
    s.text(f"閾值: >{BLOW_THRESHOLD}", 5, 125, 0, 0x666666)
    
    # 刷新屏幕
    s.refresh()
    
    # 短暂延迟
    time.sleep(0.03)
