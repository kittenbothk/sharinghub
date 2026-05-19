# 巡線小車

<figure><img src="../../../.gitbook/assets/巡線小車 (1).png" alt=""><figcaption></figcaption></figure>

## 模型搭建說明書

{% file src="../../../.gitbook/assets/巡線小車.pdf" %}

## 範例生成指令詞

```
幫我寫一個跟蹤黑線的小車程式 利用左邊P3右邊P1的灰度感應器控制左輪M2右輪M1
當兩個感應器都看到黑線時就停止小車
加一個按A就停止或啟動馬達的功能
```

在對話中加入以下模塊：電機，灰度感應器

<figure><img src="../../../.gitbook/assets/image (267).png" alt=""><figcaption></figcaption></figure>

## 範例程式

```python
from sugar import Grayscale
from future import Motor
from board import read_button

# 初始化灰度传感器
left_sensor = Grayscale('P3')  # 左边传感器
right_sensor = Grayscale('P1')  # 右边传感器

# 初始化电机
motor = Motor()

# 黑线阈值（低于此值认为是黑线）
BLACK_THRESHOLD = 1500

# 速度参数
FORWARD_SPEED = 60      # 前进速度
TURN_SPEED = 50         # 转弯速度

# 运行状态
is_running = False  # 初始停止状态
last_button_a = False  # 记录上一次A键状态

print("黑线跟踪小车启动...")
print("按A键启动或停止")

# 主循环
while True:
    # 检测A键
    button = read_button()
    button_a = (button == 1)
    
    # 按A键切换运行状态（按下时触发一次）
    if button_a and not last_button_a:
        is_running = not is_running
        if is_running:
            print("启动电机")
        else:
            print("停止电机")
            motor.stopMotor(0)  # 停止所有电机
    
    # 更新按键状态
    last_button_a = button_a
    
    # 只有在运行状态下才控制电机
    if is_running:
        # 读取左右传感器值
        left_value = left_sensor.value()
        right_value = right_sensor.value()
        
        # 判断传感器状态
        left_on_black = left_value < BLACK_THRESHOLD
        right_on_black = right_value < BLACK_THRESHOLD
        
        # 根据传感器状态控制电机
        if left_on_black and right_on_black:
            # 两个传感器都在黑线上 - 停止小车
            motor.stopMotor(0)
            
        elif left_on_black and not right_on_black:
            # 左边在黑线，右边偏离 - 向左转
            motor.setSpeed(1, TURN_SPEED)      # 右轮M1正转
            motor.setSpeed(2, 0)               # 左轮M2停止
            
        elif not left_on_black and right_on_black:
            # 左边偏离，右边在黑线 - 向右转
            motor.setSpeed(1, 0)               # 右轮M1停止
            motor.setSpeed(2, -TURN_SPEED)     # 左轮M2反转
            
        else:
            # 两个传感器都偏离 - 慢速前进寻找黑线
            motor.setSpeed(1, FORWARD_SPEED // 2)   # 右轮M1慢速正转
            motor.setSpeed(2, -FORWARD_SPEED // 2)  # 左轮M2慢速反转
```

{% file src="../../../.gitbook/assets/line_follower.py" %}

## 示範短片

{% embed url="https://drive.google.com/file/d/17zgSsSmQyAXOWVgJrqATvMcIKlG22SjR/view?usp=drive_link" %}
