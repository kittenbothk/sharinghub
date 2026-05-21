from screen import Screen
from sugar import PIR, LED
from board import *
import time

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
s.setBrightness(1)
BG_COLOR = 0x000000

# 初始化PIR传感器（P1端口）
pir = PIR('P1')

# 初始化LED灯（P2端口）
led = LED('P2')

# 广告文字（快餐店新产品介绍）
ad_text = "歡迎光臨！全新雞腿堡套餐，酥脆多汁，限量優惠價HK$28！還有新品珍珠奶茶！"

# 广告牌参数
AD_DURATION = 30      # 广告显示持续时间（秒）
SCROLL_SPEED = 80    # 滚动速度（毫秒）
SCROLL_STEP = 7       # 每次滚动的像素数

# 状态变量
motion_detected = False
ad_timer = 0
scroll_offset = 0
last_scroll_time = 0

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

# 计算文字宽度
def get_text_width(text, size=1):
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
    return total_width * size

# 绘制滚动广告
def draw_scrolling_ad():
    global scroll_offset, last_scroll_time
    
    current_time = time.ticks_ms()
    
    # 更新滚动偏移
    if time.ticks_diff(current_time, last_scroll_time) >= SCROLL_SPEED:
        scroll_offset += SCROLL_STEP
        last_scroll_time = current_time
        
        # 滚动重置（当文字完全移出屏幕后）
        text_width = get_text_width(ad_text, 2)
        if scroll_offset > text_width + 160:
            scroll_offset = 0
    
    # 绘制广告框
    s.rect(5, 40, 150, 40, 0xFF00FF, 0)
    
    # 清除广告框内部（避免文字重叠）
    s.rect(6, 41, 148, 38, BG_COLOR, 1)
    
    # 绘制滚动文字
    start_x = 150 - scroll_offset
    y = 46
    
    # 计算每个字符位置（字号为2）
    chinese_w, english_w, number_w, space_w, char_h = 12, 7, 7, 6, 12
    char_spacing = 15  # 字符间隔
    x = start_x
    
    for ch in ad_text:
        if '\u4e00' <= ch <= '\u9fff':
            char_width = chinese_w
        elif ch.isdigit():
            char_width = number_w
        elif ch == ' ':
            char_width = space_w
        else:
            char_width = english_w
        
        # 只绘制在屏幕范围内的字符
        if -char_width <= x <= 160:
            s.text(ch, int(x), y, 2, 0xFFFFFF)  # 使用2号字
        
        x += char_width + char_spacing  # 增加字符间隔

# 绘制LED灯效果
def draw_led():
    center_x = 80
    center_y = 85
    radius = 20
    
    if motion_detected:
        # LED亮起（黄色光晕）
        # 外圈光晕
        s.circle(center_x, center_y, radius, 0xFFFF00, 0)
        # 中圈
        s.circle(center_x, center_y, radius - 5, 0xFFAA00, 1)
        # 中心点
        s.circle(center_x, center_y, 8, 0xFFFFFF, 1)
        
        led_text = "燈光開啟"
        led_color = 0xFFFF00
    else:
        # LED关闭（灰色）
        s.circle(center_x, center_y, radius, 0x333333, 0)
        s.circle(center_x, center_y, radius - 5, 0x222222, 1)
        s.circle(center_x, center_y, 8, 0x444444, 1)
        
        led_text = "燈光關閉"
        led_color = 0x888888
    
    return led_text, led_color

# 主循环
while True:
    current_time = time.ticks_ms()
    
    # 读取PIR传感器
    pir_value = pir.value()
    
    # 检测到人
    if pir_value == 1:
        if not motion_detected:
            motion_detected = True
            ad_timer = current_time
            scroll_offset = 0
            # 亮起LED
            led.state('ON')
            led.brightness(100)
            print(f"Motion detected, LED ON, ad started")
        else:
            # 持续检测到人，重置计时器
            ad_timer = current_time
    
    # 广告显示时间结束
    if motion_detected and time.ticks_diff(current_time, ad_timer) >= AD_DURATION * 1000:
        motion_detected = False
        scroll_offset = 0
        # 关闭LED
        led.state('OFF')
        print("Ad ended, LED OFF")
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("快餐廣告牌", 2)
    s.text("快餐廣告牌", x, 5, 2, 0xFFFFFF)
    
    # 显示PIR状态
    if pir_value == 1:
        pir_text = "PIR: 檢測到人"
        pir_color = 0xFFFF00
    else:
        pir_text = "PIR: 無人"
        pir_color = 0x888888
    s.text(pir_text, 5, 28, 0, pir_color)
    
    # 显示端口
    s.text("P1:PIR  P2:LED", 5, 118, 0, 0x888888)
    
    # 绘制滚动广告
    if motion_detected:
        draw_scrolling_ad()
        
        # 显示剩余时间
        remaining = AD_DURATION - time.ticks_diff(current_time, ad_timer) // 1000
        if remaining > 0:
            s.text(f"廣告: {remaining}秒", 5, 80, 0, 0xAAAAAA)
    else:
        # 显示等待信息
        x, y, w, h = get_center_position("等待顧客...", 1)
        s.text("等待顧客...", x, 55, 1, 0x888888)
        
        # 绘制LED灯效果
        led_text, led_color = draw_led()
        x, y, w, h = get_center_position(led_text, 1)
        s.text(led_text, x, 110, 1, led_color)
    
    # 刷新屏幕
    s.refresh()
    
    # 短暂延迟
    time.sleep(0.03)
