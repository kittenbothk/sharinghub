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

## Get Face Data

```
koi.xywh[0]
```

Returns data for the detected face.

Parameters:&#x20;

data: The type of data to return.

<table><thead><tr><th width="324">data</th><th>Meaning</th></tr></thead><tbody><tr><td>0</td><td>X coordinates</td></tr><tr><td>1</td><td>Y coordinates</td></tr><tr><td>2</td><td>Width of face</td></tr><tr><td>3</td><td>Height of face</td></tr></tbody></table>

## Get Mask Value

```
koi.strVal
```

Returns whether the face detected is wearing a mask.

Return Value:

"with-mask": Person is wearing mask

"without-mask": Person is not wearing mask

## Sample Code: Mask Detection

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

{% file src="broken-reference" %}

## Select Face Attribute Mode

```
koi.setModel(9)
```

Sets the KOI mode to Face Attribute Detection.

## Get Face Data

```python
koi.xywh[data]
```

Returns data for the detected face.

Parameters:&#x20;

data: The type of data to return.

<table><thead><tr><th width="324">data</th><th>Meaning</th></tr></thead><tbody><tr><td>0</td><td>X coordinates</td></tr><tr><td>1</td><td>Y coordinates</td></tr><tr><td>2</td><td>Width of face</td></tr><tr><td>3</td><td>Height of face</td></tr></tbody></table>

## Get Number of Faces

```
koi.getFaceAttr(attr)
```

Returns the number of faces detected.

Return Value: Integer

Parameters:&#x20;

attr:

| attr(decimal) | meaning                              |
| ------------- | ------------------------------------ |
| 8             | Total number of faces detected       |
| 9             | Total number of male detected        |
| 10            | Total number of open mouths detected |
| 11            | Total number of smiles detected      |
| 12            | Total number of glasses detected     |
| 13            | Total number of female detected      |

## Get Attribute of Main Character

Returns the attribute of main character.

Return Value: Boolean

Parameters:

attr:

| attr(decimal) | meaning                               |
| ------------- | ------------------------------------- |
| 4             | Whether the person is a male          |
| 5             | Whether the person has an open mouth  |
| 6             | Whether the person is smiling         |
| 7             | Whether the person is wearing glasses |

## Sample Code: Face Attribute

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

{% file src="broken-reference" %}
