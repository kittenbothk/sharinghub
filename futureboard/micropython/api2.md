# 未來板MicroPython編程2：板載感應器

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 02: 板載感應器類

#### 1. 按鍵

```
sensor.btnValue(btn)
```

btn代表按鍵，a或b。返回True或False。

#### 2. 亮度感應器

```
sensor.getLight()
```

返回0\~4095。

#### 3. 溫度感應器

```
sensor.getTemp()
```

返回攝氏溫度，範圍由-40\~85度。

#### 1\~3使用範例

```
# 按A顯示亮度，按B顯示溫度
from future import *

from time import sleep

screen.fill((0, 0, 0))
while True:
  if sensor.btnValue('a'):
    screen.text(str("Light: ")+str(sensor.getLight()),5,10,1,(0, 119, 255))
    sleep(0.5)
  if sensor.btnValue('b'):
    screen.text(str("Temp: ")+str(sensor.getTemp()),5,30,1,(0, 119, 255))
    sleep(0.5)
```



#### 4 加速度計

```
sensor.accX()
sensor.accY()
sensor.accZ()
```

獲取加速度計3個軸的讀數，單位為G(重力加速度)。

#### 5. 姿勢角度

```
sensor.roll()
sensor.pitch()
```

分別獲取加速度計的橫滾度與旋轉度。

#### 4\~5使用範例

```
from future import *

from time import sleep

screen.sync = 0
while True:
  screen.fill((0, 0, 0))
  screen.text(str("X: ")+str(sensor.accX()),5,10,1,(0, 119, 255))
  screen.text(str("Y: ")+str(sensor.accY()),5,25,1,(0, 119, 255))
  screen.text(str("Z: ")+str(sensor.accZ()),5,40,1,(0, 119, 255))
  screen.text(str("Roll: ")+str(sensor.roll()),5,55,1,(0, 119, 255))
  screen.text(str("Pitch: ")+str(sensor.pitch()),5,70,1,(0, 119, 255))
  screen.refresh()
  sleep(0.2)
```



#### 6. 姿勢檢測

```
sensor.gesture(gesture)
```

未來板能偵測8種姿勢。返回True或False。

1. ‘shake’ : 搖晃
2. ‘freefall’ : 自由落體
3. ‘tilt\_up’ : 正立
4. ‘tilt\_down’ : 倒立
5. ‘tilt\_left’ : 左傾
6. ‘tilt\_right’ : 右傾
7. ‘face\_up’ : 朝上
8. ‘face\_down’ : 朝下

#### 7. 姿勢檢測觸發事件

```
sensor.gesTrig[ges] = fn
sensor.startSchedule()
```

#### 6\~7使用範例

```
# 屏幕顯示姿勢的狀態，搖晃未來板更改背景顏色為白色。
from future import *

from time import sleep

def onGesture_shake():
  buzzer.melody(JUMP_UP)

sensor.gesTrig['shake']=onGesture_shake
sensor.startSchedule()

screen.sync = 0
while True:
  screen.fill((0, 0, 0))
  screen.text(str("Face Up: ")+str(sensor.gesture('face_up')),5,10,1,(0, 119, 255))
  screen.text(str("Face Down: ")+str(sensor.gesture('face_down')),5,25,1,(0, 119, 255))
  screen.refresh()
  sleep(0.2)
```



#### 8. 磁場校正

```
calibrateCompass()
```

使用磁力計或者指南針前必須要校正。

#### 9. 獲取磁力計讀數

```
sensor.magX()
sensor.magY()
sensor.magZ()
sensor.magStrength()
```

分別獲取三軸的磁力強度和平均強度。單位為uT。

#### 10. 指南針指向

```
sensor.heading()
```

獲取當前方位，範圍為0\~360，0為北方。

#### 8\~10使用範例

```
from future import *
import math
calibrateCompass()
screen.sync = 0
ds = ''
while 1:
    d = int(math.fabs(360-sensor.heading()))
    screen.fill(44)
    if (d<20) | (d>340):
        ds = '北'
    elif (d<70):
        ds = '東北'
    elif (d<110):
        ds = '東'
    elif (d<160):
        ds = '東南'
    elif (d<200):
        ds = '南'
    elif (d<250):
        ds = '西南'
    elif (d<290):
        ds = '西'
    else:
        ds = '西北'
    screen.text(d, 5,5)
    screen.textCh(ds,5,30)
    screen.text(str('Strength: ')+str(sensor.magStrength()),5,80)
    screen.refresh()

```
