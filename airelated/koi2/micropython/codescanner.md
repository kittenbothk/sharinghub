# 掃碼模式

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

## 選擇掃碼模式

```
koi.setModel(256)
```

選擇掃碼模式

## 選擇掃碼類型

```
koi.scanCodeSwitchType(type)
```

選擇掃碼類型

參數:

type: 0 = QR Code, 1 = Barcode

## 獲取掃碼數據

```
koi.xywh[0]
```

獲取掃碼數據

參數:

data: 類型

<table><thead><tr><th width="324">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X coordinates</td></tr><tr><td>1</td><td>Y coordinates</td></tr><tr><td>2</td><td>Width of code</td></tr><tr><td>3</td><td>Height of code</td></tr></tbody></table>

## 獲取掃碼結果

```
koi.strVal
```

返回掃碼結果

## 範例程式: 掃碼模式

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(256)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  if sensor.btnValue('a'):
    koi.scanCodeSwitchType(0)
  if sensor.btnValue('b'):
    koi.scanCodeSwitchType(1)
  screen.fill((0, 0, 0))
  screen.text(koi.strVal,5,10,2,(255, 255, 255))
  screen.text(koi.xywh[0],5,40,1,(255, 255, 255))
  screen.text(koi.xywh[1],5,60,1,(255, 255, 255))
  screen.text(koi.xywh[2],5,80,1,(255, 255, 255))
  screen.text(koi.xywh[3],5,100,1,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Code Scanner.py" %}
