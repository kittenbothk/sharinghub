# 保險夾萬

模擬一個夾萬，用家需要扭動電位器輸入密碼，密碼正確就會開啟夾萬。另外亦模擬了強行爆開夾萬的防盜警報。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/safe1.jpg)

### 組裝說明書

[組裝說明書下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/pdf/safe.pdf)

### 參考接線

![](https://kittenbothk.readthedocs.io/en/latest/\_images/safe\_wire1.png)

### KittenBlock參考程式

![](https://kittenbothk.readthedocs.io/en/latest/\_images/safe\_code1.png)

[參考程式下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/sb3/safe.sb3)

### Python參考程式

```
#/bin/python

from time import sleep
from future import *
from sugar import *
import robotbit

lock_password = 0
curr_password = 0
curr_digit = 0
x = 0
y = 0
authorize = 0
digit = 0


def activate():
  global lock_password,curr_password,curr_digit,x,y,authorize,digit

  if Button("P1").value() == 0:
    sleep(0.2)
    enterPW()



def break_in():
  global lock_password,curr_password,curr_digit,x,y,authorize,digit

  if not Hall("P2").value() == 0:
    while not Hall("P2").value() == 0:
      neopix.setColorAll((255, 0, 0))
      buzzer.melody(NOTICE)
      sleep(2)
    neopix.setColorAll((0,0,0))



def enterPW():
  global lock_password,curr_password,curr_digit,x,y,authorize,digit

  while not (len(curr_password) == len(str(lock_password))):
    screen.fill((0, 0, 0))
    screen.text(str(str(curr_password)+str(curr_digit)),30,55,3,(0, 119, 255))
    screen.refresh()
    curr_digit = (round(valmap(Angle("P0").value(), 0, 4095, 0, 9)))
    if Button("P1").value() == 0:
      curr_password = (str(curr_password)+str(curr_digit))
      digit += 1
      sleep(0.2)
    break_in()
  test()



def init():
  global lock_password,curr_password,curr_digit,x,y,authorize,digit

  robot.geekServo2kg(1, 0)
  neopix.setColorAll((0,0,0))
  screen.clear()
  lock_password = (str(2021))
  curr_password = ""
  authorize = 0
  digit = 1
  screen.textCh("請輸入密碼",20,56,2,(255, 255, 255))
  screen.refresh()



def test():
  global lock_password,curr_password,curr_digit,x,y,authorize,digit

  if curr_password == lock_password:
    screen.fill((0, 255, 0))
    screen.textCh("密碼正確",35,50,2,(255, 255, 255))
    screen.refresh()
    authorize = 1
    buzzer.melody(CORRECT)
    robot.geekServo2kg(1, 90)
    sleep(1)
    while not Button("P1").value() == 0:
      pass
    sleep(1)
  else:
    screen.fill((255, 0, 0))
    screen.textCh("密碼錯誤",35,50,2,(255, 255, 255))
    screen.refresh()
    buzzer.melody(ERROR)
  init()



def valmap(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)


robot = robotbit.RobotBit()

neopix=NeoPixel("P7",3)

screen.sync = 0

init()

while True:
  activate()
  if not authorize == 1:
    break_in()
```

[參考程式下載](https://github.com/kittenbothk/kittenbothk/raw/master/Kits/future\_inventor/instructions/py/safe.py)

### 模型玩法

按下按鈕啟動，扭動電位器調較數字，按下按鈕確認。輸入正確4位數的密碼(預設為2021)就會打開大門。
