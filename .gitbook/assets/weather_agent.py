from screen import Screen
from sugar import ENV
from board import *
import time

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
BG_COLOR = 0x000000

# 初始化温湿度模块
env = ENV()

# 历史数据存储（最多保存20条记录）
history_data = []

# Agent响应状态
agent_response = ""
agent_requesting = False

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

# 调用Agent预测天气
def call_weather_agent():
    global agent_requesting, agent_response
    
    if len(history_data) < 3:
        agent_response = "數據不足"
        return
    
    agent_requesting = True
    agent_response = "請稍候..."
    
    try:
        # 构建数据摘要
        data_summary = []
        for temp, humi, ts in history_data[-10:]:  # 最近10条记录
            data_summary.append(f"T{temp:.1f}H{humi:.0f}")
        
        data_str = ",".join(data_summary)
        prompt = f"基于温湿度数据[{data_str}]预测未来天气变化，回答控制在30字以内"
        
        # 调用Agent（使用future板的Agent API）
        from agent import Agent
        agent = Agent()
        response = agent.chat(prompt)
        
        # 限制回答长度为20字
        if len(response) > 20:
            response = response[:20]
        
        agent_response = response
        
    except Exception as e:
        agent_response = "預測失敗"
        print(f"Agent error: {e}")
    
    agent_requesting = False

# 上次读取时间
last_read_time = 0
READ_INTERVAL = 2  # 读取间隔（秒）

# 主循环
while True:
    current_time = time.ticks_ms()
    
    # 定期读取温湿度数据
    if time.ticks_diff(current_time, last_read_time) >= READ_INTERVAL * 1000:
        temp, humi = env.update()
        history_data.append((temp, humi, current_time))
        
        # 保持最近20条记录
        if len(history_data) > 20:
            history_data.pop(0)
        
        last_read_time = current_time
    
    # 检测A键
    btn = read_button()
    if btn == 1 and not agent_requesting:
        call_weather_agent()
    
    # 清除屏幕
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    # 显示标题
    x, y, w, h = get_center_position("天氣預測", 2)
    s.text("天氣預測", x, 5, 2, 0xFFFFFF)
    
    # 显示当前温湿度
    if history_data:
        current_temp, current_humi, _ = history_data[-1]
        s.text("當前:", 5, 30, 1, 0x00FF00)
        s.text(f"溫度: {current_temp:.1f}°C", 5, 43, 1, 0xFFFF00)
        s.text(f"濕度: {current_humi:.1f}%", 5, 56, 1, 0xFFFF00)
        s.text(f"記錄: {len(history_data)}條", 5, 69, 1, 0x00FFFF)
    
    # 显示分隔线
    s.line(0, 82, 160, 82, 0x444444)
    
    # 显示Agent响应
    s.text("預測:", 5, 87, 1, 0xFF00FF)
    if agent_requesting:
        s.text("正在分析...", 5, 100, 1, 0xFFFF00)
    elif agent_response:
        s.text(agent_response, 5, 100, 1, 0xFFFFFF)
    else:
        s.text("按A鍵預測", 5, 100, 1, 0x888888)
    
    # 显示控制提示
    s.text("按A鍵預測天氣", 5, 118, 0, 0xAAAAAA)
    
    # 刷新屏幕
    s.refresh()
    
    # 短暂延迟
    time.sleep(0.1)
