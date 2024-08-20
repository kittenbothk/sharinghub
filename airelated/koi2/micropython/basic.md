# 基本操作

## 加入KOI 2庫

```python
from future import *
from koi2 import KOI2
```

## 初始化KOI 2

```python
koi = KOI2(tx, rx)
```

初次化KOI 2連接。

參數:

tx: TX 針腳，Robotbit EDU使用P2

rx: RX 針腳，Robotbit EDU使用P12

## KOI切換模式

```python
koi.setModel(mode)
```

選擇KOI 2模式

參數:

mode:

| 參數(數字 | 功能                          |
| ----- | --------------------------- |
| 0     | None Mode                   |
| 1     | Built-in Road Sign Tracking |
| 2     | Built-in Item Tracking      |
| 3     | Custom Tracking Model       |
| 4     | Built-in Number Tracking    |
| 5     | Image Classifier            |
| 6     | Built-in Alphabets Tracking |
| 7     | Fa Mak Detection            |
| 9     | Face Attributes Detection   |
| 10    | Color Blob Detection        |
| 32    | Line Trace Detection        |
| 256   | Code Scanner                |

## KOI鏡頭方向

```python
koi.direction(dir)
```

設定鏡頭方向

參數:

dir: 0=前置鏡頭, 2=後置鏡頭

## KOI更新數據

```python
koi.read_from_uart()
```

從KOI讀取數據。

## KOI按鍵

```python
koi.getBtnState(btn)
```

返回按鍵狀態：按下時返回1，沒按下時返回0。

Parameters:

btn: 字串，"A" 代表A按鍵，"B"代表B按鍵

## KOI錄音

```
koi.recorded('/sd/'+name,duration)
```

錄音並儲存到SD卡。

參數:

name: 檔案名稱，必須以".wav"結尾

duration: 長度(秒)，一般為3秒

## KOI播放音頻檔

```
koi.playAudio('/sd/'+name)
```

播放SD卡上的音頻檔。

參數:

name: 檔案名稱，必須以".wav"結尾

## KOI 拍照儲存

```
koi.takePic(location+name)
```

儲存一張照片。

參數:

location: 位置, '/sd/'=SD卡, '/flash/'=板載空間

name: 檔案名稱，必須以".jpg"結尾

## KOI 顯示照片

```
koi.displayPic(location+name,duration)
```

顯示一張照片

參數:

location: 位置, '/sd/'=SD卡, '/flash/'=板載空間

name: 檔案名稱，必須以".jpg"結尾

duration: 時長(毫秒)

## KOI 顯示字串

```
koi.displayText(x,y,duration,color(r,g,b),text)
```

顯示字串

參數:

x: X座標

y: Y座標

duration: 時長(毫秒)

color: 文字RGB顏色

text: 字串

## 參考程式

```
from future import *
from koi2 import KOI2

koi = KOI2('P2', 'P12')
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.displayText(0+40,0,3*1000,(255, 255, 255),'hello')
  if koi.getBtnState('A'):
    koi.takePic('/flash/'+'abc.jpg')
  if koi.getBtnState('B'):
    koi.displayPic('/flash/'+'abc.jpg',3*1000)
```

{% file src="../../../.gitbook/assets/basicoperations1.py" %}
