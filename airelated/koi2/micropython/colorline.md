# 色塊追蹤與線條追蹤

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

## 選擇線條追蹤模式

```
koi.setModel(16)
```

選擇線條追蹤模式

## 選擇目標顏色

```
koi.colorSwitch(color)
```

參數:

color: 顏色

<table><thead><tr><th width="286">color</th><th width="249">代表</th></tr></thead><tbody><tr><td>0</td><td>紅色</td></tr><tr><td>1</td><td></td></tr><tr><td>2</td><td>Blue</td></tr><tr><td>3</td><td>Yellow</td></tr><tr><td>9</td><td>自定義(需要校正)</td></tr></tbody></table>

## 校正自定義顏色

```
koi.colorCalibration()
```

校正自定義顏色

## 獲取色塊數據

```
koi.xywh[0]
```

獲取色塊數據

參數:&#x20;

data: 數據類型

<table><thead><tr><th width="324">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X coordinates</td></tr><tr><td>1</td><td>Y  coordinates</td></tr><tr><td>2</td><td>Width of blob</td></tr><tr><td>3</td><td>Height of blob</td></tr></tbody></table>

## 範例程式: 色塊追蹤

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(16)
screen.sync = 0
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.colorSwitch(0)
  if sensor.btnValue('b'):
    koi.colorCalibration()
    koi.colorSwitch(9)
  screen.fill((0, 0, 0))
  screen.text(koi.xywh[0],5,10,1,(255, 255, 255))
  screen.text(koi.xywh[1],5,30,1,(255, 255, 255))
  screen.text(koi.xywh[2],5,50,1,(255, 255, 255))
  screen.text(koi.xywh[3],5,70,1,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Color Blob Tracking.py" %}

## 選擇線條追蹤模式

```
koi.setModel(32)
```

選擇線條追蹤模式

## 選擇目標顏色

```
koi.colorSwitch(color)
```

參數:

color: 顏色

<table><thead><tr><th width="286">color</th><th width="249">代表</th></tr></thead><tbody><tr><td>0</td><td>紅色</td></tr><tr><td>1</td><td></td></tr><tr><td>2</td><td>Blue</td></tr><tr><td>3</td><td>Yellow</td></tr><tr><td>9</td><td>自定義(需要校正)</td></tr></tbody></table>

## 校正自定義顏色

```
koi.colorCalibration()
```

校正自定義顏色

## 獲取線條數據

```
koi.xy12[data]
```

獲取線條數據

參數:

data: The type of data to return.

<table><thead><tr><th width="294">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X1 coordinates</td></tr><tr><td>1</td><td>Y1 coordinates</td></tr><tr><td>2</td><td>X2 coordinates</td></tr><tr><td>3</td><td>Y2 </td></tr></tbody></table>

## 範例程式: 線條追蹤

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(32)
screen.sync = 0
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.lineSwitch(3)
  if sensor.btnValue('b'):
    koi.colorCalibration()
    koi.lineSwitch(4)
  screen.fill((0, 0, 0))
  screen.text(koi.xy12[0],5,10,1,(255, 255, 255))
  screen.text(koi.xy12[1],5,30,1,(255, 255, 255))
  screen.text(koi.xy12[2],5,50,1,(255, 255, 255))
  screen.text(koi.xy12[3],5,70,1,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Item Tracking.py" %}

