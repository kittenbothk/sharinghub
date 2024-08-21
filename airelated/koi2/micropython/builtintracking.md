# 預載追蹤模型

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

## 選擇路牌追蹤模式

```
koi.setModel(1)
```

選擇路牌追蹤模式

## 獲取路牌追蹤數據

```
koi.xywh[0]
```

返回路牌追蹤數據

參數:&#x20;

data: 數據類型

<table><thead><tr><th width="311">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X 座標</td></tr><tr><td>1</td><td>Y 座標</td></tr><tr><td>2</td><td>闊度</td></tr><tr><td>3</td><td>高度</td></tr></tbody></table>

## 獲取路牌名稱

```
koi.strVal
```

返回路牌名稱

返回數值: U-Turn, forward, left, right, limit-30, stop, tunnel

## 範例程式: 路牌追蹤

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(1)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  screen.fill((0, 0, 0))
  screen.text(koi.strVal,5,10,2,(255, 255, 255))
  screen.text(koi.xywh[0],5,30,2,(255, 255, 255))
  screen.text(koi.xywh[1],5,50,2,(255, 255, 255))
  screen.text(koi.xywh[2],5,70,2,(255, 255, 255))
  screen.text(koi.xywh[3],5,90,2,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Road Sign.py" %}

## 選擇物件追蹤模式

```
koi.setModel(2)
```

選擇物件追蹤模式

## 獲取物件追蹤數據

```
koi.xywh[0]
```

獲取物件追蹤數據

參數:&#x20;

data: 數據類型

<table><thead><tr><th width="311">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X 座標</td></tr><tr><td>1</td><td>Y 座標</td></tr><tr><td>2</td><td>闊度</td></tr><tr><td>3</td><td>高度</td></tr></tbody></table>

## 獲取物件追蹤名稱

```
koi.strVal
```

返回物件追蹤名稱.

返回數值: aeroplane, bicycle, bird, boat, bottle, bus, car, cat, chair, cow, diningtable, dog, horse, motorbike, person, pottedplant, sheep, sofa, train, tvmonitor

## 範例程式: 物件追蹤

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(2)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  screen.fill((0, 0, 0))
  screen.text(koi.strVal,5,10,2,(255, 255, 255))
  screen.text(koi.xywh[0],5,30,2,(255, 255, 255))
  screen.text(koi.xywh[1],5,50,2,(255, 255, 255))
  screen.text(koi.xywh[2],5,70,2,(255, 255, 255))
  screen.text(koi.xywh[3],5,90,2,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Item Tracking.py" %}

## 選擇字母追蹤模式

```
koi.setModel(6)
```

選擇字母追蹤模式

## 獲取字母追蹤數據

```
koi.xywh[0]
```

獲取字母追蹤數據

參數:&#x20;

data: 數據類型

<table><thead><tr><th width="208">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X 座標</td></tr><tr><td>1</td><td>Y 座標</td></tr><tr><td>2</td><td>闊度</td></tr><tr><td>3</td><td>高度</td></tr></tbody></table>

## 獲取字母追蹤名稱

```
koi.strVal
```

返回字母追蹤名稱.

返回數值: A, B, C, D, E, F

## 範例程式: 字母追蹤

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(6)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  screen.fill((0, 0, 0))
  screen.text(koi.strVal,5,10,2,(255, 255, 255))
  screen.text(koi.xywh[0],5,30,2,(255, 255, 255))
  screen.text(koi.xywh[1],5,50,2,(255, 255, 255))
  screen.text(koi.xywh[2],5,70,2,(255, 255, 255))
  screen.text(koi.xywh[3],5,90,2,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Alphabet Tracking.py" %}

## 選擇數字追蹤模式

```
koi.setModel(4)
```

選擇數字追蹤模式

## 獲取數字追蹤數據

```
koi.xywh[0]
```

獲取數字追蹤數據

參數:&#x20;

data: 數據類型

<table><thead><tr><th width="208">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X 座標</td></tr><tr><td>1</td><td>Y 座標</td></tr><tr><td>2</td><td>闊度</td></tr><tr><td>3</td><td>高度</td></tr></tbody></table>

## 獲取數字追蹤名稱

```
koi.numberVal
```

返回數字追蹤名稱.

返回數值: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

## 範例程式: 數字追蹤

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(4)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  screen.fill((0, 0, 0))
  screen.text(koi.numberVal,5,10,2,(255, 255, 255))
  screen.text(koi.xywh[0],5,30,2,(255, 255, 255))
  screen.text(koi.xywh[1],5,50,2,(255, 255, 255))
  screen.text(koi.xywh[2],5,70,2,(255, 255, 255))
  screen.text(koi.xywh[3],5,90,2,(255, 255, 255))
  screen.refresh()

```
