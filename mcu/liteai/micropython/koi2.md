# 15 AI鏡頭 KOI 2

## 參考程式1: 顯示文字與按鍵

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
while True:
  koi.read_from_uart()
  if koi.getBtnState('A'):
    koi.displayText(0+40,0,3*1000,(182, 141, 105),'A')
  if koi.getBtnState('B'):
    koi.displayText(0+40,0,3*1000,(182, 141, 105),'B')

```

## 參考程式2: 拍照保存

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
while True:
  koi.read_from_uart()
  if koi.getBtnState('A'):
    koi.takePic('/flash/'+'abc.jpg')
  if koi.getBtnState('B'):
    koi.displayPic('/flash/'+'abc.jpg',3*1000)

```

## 參考程式3: 鏡頭方向

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
while True:
  koi.read_from_uart()
  if koi.getBtnState('A'):
    koi.direction(2)
  if koi.getBtnState('B'):
    koi.direction(0)

```

## 參考程式4: 色塊追蹤

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.setModel(16) #set to color blob mode
koi.colorSwitch(1) #change color to track
#0 = red, 1 = blue, 2 = green, 3 = yellow, 4 = custom
while True:
  koi.read_from_uart()
  screens.text((koi.xywh[0]),5,10,1,(0, 170, 170)) #x coordinate
  screens.text((koi.xywh[1]),5,30,1,(0, 170, 170)) #y coordinate
  screens.text((koi.xywh[2]),5,50,1,(0, 170, 170)) #width
  screens.text((koi.xywh[3]),5,70,1,(0, 170, 170)) #height
  screens.refresh()
  if koi.getBtnState('A'):
    koi.colorCalibration() #calibration custom color
    koi.colorSwitch(9) #switch to track custom color

```

## 參考程式5: 線條追蹤

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.setModel(32) #set to line track mode
koi.lineSwitch(0) #change color to track
while True:
  koi.read_from_uart()
  screens.text((koi.xy12[0]),5,10,1,(0, 170, 170)) #x1 coordinate
  screens.text((koi.xy12[1]),5,30,1,(0, 170, 170)) #y1 coordinate
  screens.text((koi.xy12[2]),5,50,1,(0, 170, 170)) #x2 coordinate
  screens.text((koi.xy12[3]),5,70,1,(0, 170, 170)) #y2 coordinate
  screens.refresh()
  if koi.getBtnState('A'):
    koi.colorCalibration() #calibrate custom color
    koi.lineSwitch(4) #change to track custom color

```

## 參考程式6: 人面追蹤

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.setModel(9) #change to face tracking mode
while True:
  koi.read_from_uart()
  screens.text((koi.xywh[0]),5,10,1,(0, 170, 170)) #x coordinate
  screens.text((koi.xywh[1]),5,30,1,(0, 170, 170)) #y coordinate
  screens.text((koi.xywh[2]),5,50,1,(0, 170, 170)) #width
  screens.text((koi.xywh[3]),5,70,1,(0, 170, 170)) #height
  screens.text((int(koi.getFaceAttr(8))),5,90,1,(0, 170, 170)) #number of faces
  screens.text((int(koi.getFaceAttr(6))),5,110,1,(0, 170, 170)) #smile boolean
  # getFaceAttr
  # 4 = male(boolean)
  # 5 = mouth open(boolean)
  # 6 = smile(boolean)
  # 7 = glasses(boolean)
  # 8 = number of faces
  # 9 = number of males
  # 10 = number of open mouths
  # 11 = number of smiles
  # 12 = number of glasses
  # 13 = number of females
  screens.refresh()

```

## 參考程式7: 口罩辨認

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.direction(0)
koi.setModel(7) #set to mask track mode
while True:
  koi.read_from_uart()
  screens.text((koi.xywh[0]),5,10,1,(0, 170, 170)) #x coordinate
  screens.text((koi.xywh[1]),5,30,1,(0, 170, 170)) #y coordinate
  screens.text((koi.xywh[2]),5,50,1,(0, 170, 170)) #width
  screens.text((koi.xywh[3]),5,70,1,(0, 170, 170)) #height
  screens.text((koi.strVal == 'with-mask'),5,90,1,(0, 170, 170)) #mask detection
  screens.refresh()
```

## 參考程式8: 路牌辨識

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.direction(2)
koi.setModel(1) #set to road sign tracking mode
while True:
  koi.read_from_uart()
  screens.text((koi.xywh[0]),5,10,1,(0, 170, 170)) #x coordinate
  screens.text((koi.xywh[1]),5,30,1,(0, 170, 170)) #y coordinate
  screens.text((koi.xywh[2]),5,50,1,(0, 170, 170)) #width
  screens.text((koi.xywh[3]),5,70,1,(0, 170, 170)) #height
  screens.text((koi.strVal),5,90,1,(0, 170, 170)) #road sign name
  screens.refresh()

```

## 參考程式9: 物件辨識

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.direction(2)
koi.setModel(2) #set to item tracking mode
while True:
  koi.read_from_uart()
  screens.text((koi.xywh[0]),5,10,1,(0, 170, 170)) #x coordinate
  screens.text((koi.xywh[1]),5,30,1,(0, 170, 170)) #y coordinate
  screens.text((koi.xywh[2]),5,50,1,(0, 170, 170)) #width
  screens.text((koi.xywh[3]),5,70,1,(0, 170, 170)) #height
  screens.text((koi.strVal),5,90,1,(0, 170, 170)) #item name
  screens.refresh()

```

## 參考程式10: 數字辨識

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.direction(2)
koi.setModel(4) #set to digit tracking mode
while True:
  koi.read_from_uart()
  screens.text((koi.xywh[0]),5,10,1,(0, 170, 170)) #x coordinate
  screens.text((koi.xywh[1]),5,30,1,(0, 170, 170)) #y coordinate
  screens.text((koi.xywh[2]),5,50,1,(0, 170, 170)) #width
  screens.text((koi.xywh[3]),5,70,1,(0, 170, 170)) #height
  screens.text((koi.numberVal),5,90,1,(0, 170, 170)) #digit name
  screens.refresh()

```

## 參考程式11: 掃碼模式

```python
from future import *
from koi2 import KOI2
from screen import Screen


screens = Screen()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.direction(2)
koi.setModel(256) #set mode to code scanner
while True:
  koi.read_from_uart()
  screens.text((koi.xywh[0]),5,10,1,(0, 170, 170)) #x coordinate
  screens.text((koi.xywh[1]),5,30,1,(0, 170, 170)) #y coordinate
  screens.text((koi.xywh[2]),5,50,1,(0, 170, 170)) #width
  screens.text((koi.xywh[3]),5,70,1,(0, 170, 170)) #height
  screens.text((koi.strVal),5,90,1,(0, 170, 170)) #code contents
  screens.refresh()
  if koi.getBtnState('A'):
    koi.scanCodeSwitchType(0) #switch to QR code mode
  if koi.getBtnState('B'):
    koi.scanCodeSwitchType(1) #switch to barcode mode

```

## 參考程式12: 圖像辨識模型訓練

```python
from future import *
from sensor import Sensor
from koi2 import KOI2
from screen import Screen


screens = Screen()
sensors = Sensor()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.direction(2)
koi.setModel(5) #set to machine learning mode
while True:
  koi.read_from_uart()
  screens.refresh()
  if sensors.btnValue('a'):
    koi.classifierAddTag('A') #add tag 'A' to classifier
  if sensors.btnValue('b'):
    koi.classifierAddTag('B') #add tag 'B' to classifier
  if sensors.btnValue('m'):
    koi.classifierSave('/flash/'+'abc.json') #save model

```

## 參考程式13: 圖像辨識模型運行

```python
from future import *
from sensor import Sensor
from koi2 import KOI2
from screen import Screen


screens = Screen()
sensors = Sensor()


screens.autoRefresh(False)
koi = KOI2('uart0')
koi.direction(2)
koi.setModel(5) #set to machine learning mode
koi.classifierLoad('/flash/'+'abc.json') #load model
while True:
  koi.read_from_uart()
  screens.fill((0, 0, 0))
  screens.text((koi.strVal),5,10,1,(0, 170, 170)) #get classifier result
  screens.text((koi.getSimilarity()),5,30,1,(0, 170, 170)) #get confidence
  screens.refresh()
  if sensors.btnValue('a'):
    koi.classifierGetMostSimilarResults() #set confidence to most similar result
  if sensors.btnValue('b'):
    koi.setDetectionTarget('A') #set confidence to specific tag

```
