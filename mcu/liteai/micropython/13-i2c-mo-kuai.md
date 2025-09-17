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
