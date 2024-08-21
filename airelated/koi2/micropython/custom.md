# 自定義追蹤模型

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

## 選擇自定義追蹤模型模式

```
koi.setModel(3)
```

選擇自定義追蹤模型模式

## 載入自定義追蹤模型

```python
koi.initCustomModel(name, anchor)
koi.initCustomModel('/sd/ballRGB.kmodel',[1.25,1.25,1.50,1.50,1.72,1.72,1.97,1.97,2.34,2.31]) #example for color balls model
```

載入自定義追蹤模型

參數:

name: 檔案名稱

anchor: 錨點值

## 獲取自定義追蹤數據

```
koi.xywh[0]
```

返回自定義追蹤數據

參數:&#x20;

data: 數據類型

<table><thead><tr><th width="311">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X 座標</td></tr><tr><td>1</td><td>Y 座標</td></tr><tr><td>2</td><td>闊度</td></tr><tr><td>3</td><td>高度</td></tr></tbody></table>

## 獲取自定義追蹤名稱

```
koi.strVal
```

返回自定義追蹤名稱

## 範例程式: 自定義追蹤模型

```
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(3)
sleep(15)
koi.initCustomModel(10616832,[1.25,1.25,1.50,1.50,1.72,1.72,1.97,1.97,2.34,2.31])
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

{% file src="../../../.gitbook/assets/Custom Ball Model.py" %}
