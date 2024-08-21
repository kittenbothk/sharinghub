# 人面追蹤

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

## 選擇人面口罩模式

```
koi.setModel(7)
```

Sets the KOI mode to Face Mask Detection.

## 獲取人面數據

```
koi.xywh[0]
```

獲取人面數據

參數:&#x20;

data:&#x20;

<table><thead><tr><th width="324">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X coordinates</td></tr><tr><td>1</td><td>Y coordinates</td></tr><tr><td>2</td><td>Width of face</td></tr><tr><td>3</td><td>Height of face</td></tr></tbody></table>

## 獲取口罩數據

```
koi.strVal
```

獲取口罩數據

返回數值:

"with-mask": 人面有佩戴口罩

"without-mask": 人面沒有佩戴口罩

## 範例程式: 人面口罩追蹤

```python
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(7)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  screen.fill((0, 0, 0))
  screen.text(koi.strVal,5,10,2,(255, 255, 255))
  screen.text(koi.xywh[0],5,40,1,(255, 255, 255))
  screen.text(koi.xywh[1],5,60,1,(255, 255, 255))
  screen.text(koi.xywh[2],5,80,1,(255, 255, 255))
  screen.text(koi.xywh[3],5,100,1,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Mask Detection.py" %}

## 切換人面屬性模式

```
koi.setModel(9)
```

切換人面屬性模式

## 獲取人面數據

```python
koi.xywh[data]
```

獲取人面數據

參數:

data: 數據類型

<table><thead><tr><th width="324">data</th><th>代表</th></tr></thead><tbody><tr><td>0</td><td>X 座標</td></tr><tr><td>1</td><td>Y 座標</td></tr><tr><td>2</td><td>闊度</td></tr><tr><td>3</td><td>高度</td></tr></tbody></table>

## 獲取人面數量

```
koi.getFaceAttr(attr)
```

獲取人面數量

返回數值: 整數

參數:&#x20;

attr[^1]:

| attr(decimal) | 代表    |
| ------------- | ----- |
| 8             | 人面總數  |
| 9             | 男性數目  |
| 10            | 張開口數目 |
| 11            | 微笑數目  |
| 12            | 戴眼鏡數目 |
| 13            | 女性數目  |

## 獲取主要角色人面屬性

獲取主要角色人面屬性.

返回數值: 布林值

參數:

attr:

| attr(decimal) | 代表    |
| ------------- | ----- |
| 4             | 是否為男性 |
| 5             | 是否張開口 |
| 6             | 是否微笑  |
| 7             | 是否戴眼鏡 |

## 範例程式: 人面屬性追蹤

```python
from future import *
from koi2 import KOI2



koi = KOI2('P2', 'P12')
koi.setModel(9)
sleep(15)
koi.direction(2)
koi.mirror(0)
screen.sync = 0
while True:
  koi.read_from_uart()
  screen.fill((0, 0, 0))
  screen.text(int(koi.getFaceAttr(4)),5,10,1,(255, 255, 255))
  screen.text(koi.xywh[0],5,30,1,(255, 255, 255))
  screen.text(koi.xywh[1],5,50,1,(255, 255, 255))
  screen.text(koi.xywh[2],5,70,1,(255, 255, 255))
  screen.text(koi.xywh[3],5,90,1,(255, 255, 255))
  screen.refresh()

```

{% file src="../../../.gitbook/assets/Face Attribute.py" %}

[^1]: 
