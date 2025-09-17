# 6 電機和舵機

## 6.1 電機

### 6.1.1構建對象

`class future.Motor()`

```python
from future import *

motor = Motor()
```

### 6.1.2 設置速度

`setSpeed(index,speed,sec)`

參數

* index：int類型，電機序號1、2
* speed：int類型，電機速度，範圍0\~100
* sec：int類型，秒，如果為0則持續不斷

### 6.1.3 停止電機

`stopMotor(index)`

參數

* index：index類型，序號，0、1、2，設置為0的時候停止全部電機

## 6.2 舵機

### 6.2.1 設置角度

`future.geekservo9g(pin,angle)`

參數

* pin：str類型，引腳
  * P1, P2, P3, P4
* angle：int類型，角度，範圍-45\~225

```python
from future import *

geekservo9g('P1', 90)
```

