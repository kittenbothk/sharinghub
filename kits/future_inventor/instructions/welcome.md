# 迎賓機械人

模擬商店歡迎顧客，當檢測到有人靠近時自動揮手並發出聲效歡迎顧客。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/welcome1.jpg)

### 組裝說明書

[組裝說明書下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/pdf/welcome.pdf)

### 參考接線

![](https://kittenbothk.readthedocs.io/en/latest/\_images/welcome\_wire.png)

### 參考程式

#### KittenBlock參考程式

![](https://kittenbothk.readthedocs.io/en/latest/\_images/welcome\_code.png)

[參考程式下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/sb3/welcome.sb3)

#### Python參考程式

```
#/bin/python

from time import sleep
from future import *
from sugar import *
import robotbit

x = 0
y = 0


def detect():
  global x,y

  if PIR("P0").value():
    if TOFDistance().value() < 300:
      x = TOFDistance().value()
      sleep(1)
      y = TOFDistance().value()
      if x > y:
        welcome()



def welcome():
  global x,y

  buzzer.melody(CORRECT)
  screen.fill((0, 119, 255))
  screen.textCh("歡迎光臨",30,50,2,(255, 255, 255))
  screen.refresh()
  for count in range(3):
    robot.geekServo2kg(1, 90)
    sleep(0.2)
    robot.geekServo2kg(1, 0)
    sleep(0.2)
  screen.clear()



robot = robotbit.RobotBit()

robot.geekServo2kg(1, 0)

while True:
  detect()
```

[參考程式下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/py/welcome.py)

### 模型玩法

有人走過的時候，模型會揮手歡迎。
