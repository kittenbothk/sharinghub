# 11 Sugar數碼模組

## 11.1 方糖按鍵模塊

### 11.1.1 構建對象

`class sugar.Button(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

button = Button('P1')
```

### 11.1.2 檢測按下

`value()`

* 返回值：bool類型

## 11.2 PIR人體檢測模塊

### 11.2.1 構造對象

`class sugar.PIR(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

pir_p1 = PIR('P1')
```

### 11.2.2 檢測到有人

`value()`

* 返回值：bool類型

## 11.3 數字巡線模塊

### 11.3.1 構造對象

`class sugar.Tracker(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

tracker_p1 = Tracker('P1')
```

### 11.3.2 檢測到黑線

`value()`

* 返回值：bool類型

## 11.4 磁力傳感器模塊

### 11.4.1 構造對象

`class sugar.Hall(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

tracker_p1 = Hall('P1')
```

### 11.4.2 檢測磁鐵

`value()`

* 返回值：bool類型，檢測到的時候為低電平

## 11.5 碰撞傳感器模塊

### 11.5.1 構造對象

`class sugar.Crash(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

crash_p1 = Crash('P1')
```

### 11.5.2 觸發碰撞傳感器

`value()`

* 返回值：bool類型，檢測到的時候為低電平

## 11.6 觸摸傳感器模塊

### 11.6.1 構造對象

`class sugar.Touch(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

touch_p1 = Touch('P1')
```

### 11.6.2 觸發觸摸傳感器

`value()`

返回值：bool類型，檢測到的時候為低電平

## 11.7 LED模塊

### 11.7.1 構造對象

`class sugar.LED()`

```python
from sugar import *

led_p1 = LED('P1')
```

### 11.7.2 設置led狀態

`state(type)`

參數

* type：str類型，ON or OFF

### 11.7.3 設置百分比亮度

`brightness(value)`

參數

* value：int類型

## 11.8 LED燈串模塊

### 11.8.1 構造對象

`class sugar.LED()`

```python
from sugar import *

ledStrand_p1.state('ON')
```

### 11.8.2 設置led燈串狀態

`state(type)`

參數

* type：str類型，ON or OFF

### 11.8.3 設置百分比亮度

`brightness(value)`

參數

* value：int類型

## 11.9 紅點激光模塊

### 11.9.1 構造對象

`class sugar.Laser()`

```python
from sugar import *

laser_p1 = Laser('P1')
```

### 11.9.2 設置led燈串狀態

`state(type)`

參數

* type：str類型，ON or OFF
