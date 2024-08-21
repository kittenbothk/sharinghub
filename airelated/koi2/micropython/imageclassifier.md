# 圖像辨識

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

## 選擇圖像辨識模式

```
koi.setModel(5)
```

選擇圖像辨識模式

## 圖像辨識添加分類

```
koi.classifierAddTag(class)
```

圖像辨識添加分類

參數:&#x20;

class: 分類名稱

## 儲存圖像辨識模型

```
koi.classifierSave(location'+json)
```

儲存圖像辨識模型.

參數:

位置: '/sd/' = 儲存到SD卡, '/flash/' = 儲存到板載空間

json: 檔案名稱，必須以".json"結尾

## 範例程式: 圖像辨識模型訓練

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(5)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.classifierAddTag('A')
    sleep(0.2)
  if sensor.btnValue('b'):
    koi.classifierAddTag('B')
    sleep(0.2)
  if koi.getBtnState('A'):
    koi.classifierSave('/flash/'+'abc.json')

```

{% file src="../../../.gitbook/assets/Image Classifier Save.py" %}

## 獲取圖像辨識結果

```
koi.strVal
```

返回圖像辨識結果

## 獲取相似值

```
koi.getSimilarity()
```

返回相似值

## 載入圖像辨識模型

```
koi.classifierLoad(location'+json)
```

載入圖像辨識模型.

參數:

位置: '/sd/' = SD卡, '/flash/' = 板載空間

json: 檔案名稱，必須以".json"結尾

## 設定相似值目標為最近似結果

```
koi.classifierGetMostSimilarResults()
```

設定相似值目標為最近似結果

## 指定相似值目標為特定分類

```
koi.classifierSetDetectionTarget(class)
```

指定相似值目標為特定分類

參數:&#x20;

class: 分類名稱

## 重設圖像分類

```
koi.classifierReset()
```

重設圖像分類模式並清除未儲存之訓練數據.

## 範例程式: 圖像辨識模型載入+運行

```python
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(5)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.classifierLoad('/flash/'+'abc.json')
    sleep(0.5)
  screen.fill((0, 0, 0))
  screen.text(koi.strVal,5,10,2,(255, 255, 255))
  screen.text(koi.getSimilarity(),5,40,2,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Image Classifier Load.py" %}
