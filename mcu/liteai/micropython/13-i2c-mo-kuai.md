# 13 I2C模塊

## 13.1 激光測距模塊

### 13.1.1 構造對象

`class sugar.TOFDistance()`

```python
from sugar import *

tofDis = TOFDistance()
```

### 13.1.2 獲取距離

`value()`

返回值，int類型(毫米)

## 13.2 溫濕度傳感器模塊

### 13.2.1 構造對象

`class sugar.ENV()`

```python
from sugar import *

env1 = ENV()
```

### 13.2.2 獲取溫濕度

`update()`

* 返回值，(double temp,double hum)

## 13.3 氣壓傳感器模塊

### 13.3.1 構造對象

`class sugar.ENV2()`

```python
from sugar import *

env2 = ENV2()
```

### 13.3.2 獲取氣壓

`read_pres()`

* 返回值，double(百帕)

### 13.3.3 獲取海拔

`read_altitude()`

* 返回值，double(米)

### 13.3.4 獲取溫度

`read_temp()`

* 返回值，(double °C,double °F)

## 13.4 五向搖桿模塊

### 13.4.1 構造對象

`class sugar.Joystick()`

```python
from sugar import *

joystick = Joystick()
```

### 13.4.2 搖桿狀態

`state()`

* 返回值，str類型
  * up
  * down
  * left
  * right
  * pressed

### 13.4.3 搖桿數值

`value(type)`

參數

* type：string類型
  * x：橫坐標
  * y：縱坐標

返回值，int類型，坐標值

## 13.5 空氣質量傳感器

### 13.5.1 構造對象

`class sugar.PMSA003I()`

```python
from sugar import *

pm = PMSA003I()
```

### 13.5.2 雜質濃度

`read(type)`

* 返回值：（double pm1.0, double pm2.5, double pm10）

## 13.6 RFID模塊

### 13.6.1 構造對象

`class sugar.RFID()`

```python
from sugar import *

rfids = RFID()
```

### 13.6.2 檢測到RFID卡

`scan()[0]`

返回值：bool類型

### 13.6.3 獲取卡uuid

`uuid()`

返回值：str類型，rfid卡號

### 13.6.4 寫入數據

`write(address,data)`

參數

* address：int類型，0\~46
* data：str類型

### 13.6.5 讀取數據

`read(address)`

參數

* address：int類型，0\~46

## 13.7 數碼管模塊

### 13.7.1 構造對象

`class sugar.Nixietube()`

```python
from sugar import *

display = Nixietube()
```

### 13.7.2 顯示數字

`shownum(number)`

參數

* number：int類型

### 13.7.3 在指定位置顯示內容

`showbit(text,index)`

參數

* ext：int類型,顯示的數字也可以是"-"
* index：int類型，位置

### 13.7.4 顯示冒號

參數

* show：bool類型,啟用與否
