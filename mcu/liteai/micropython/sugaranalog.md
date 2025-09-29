# 12 Sugar模擬模組

## 12.1 火焰傳感器模塊

### 12.1.1 構造對象

`class sugar.Flame(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

flame_p3 = Flame('P3')
```

### **12.1.2 火焰光照度**

`value()`

* 返回值，int類型，0\~4095隨著火光強度變換

## 12.2 電位器模塊

### 12.2.1 構造對象

`class sugar.Angle(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

angle_p1 = Angle('P1')
```

### **12.2.2** 電位器值

`value()`

* 返回值，int類型，0\~4095

## 12.3 灰度傳感器模塊

### 12.2.1 構造對象

`class sugar.Angle(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

angle_p1 = Angle('P1')
```

### 12.3.2 灰度值

`value()`

* 返回值，int類型，0\~4095

## 12.4 光敏傳感器模塊

### 12.4.1 構造對象

`class sugar.Light(pin)`

參數

* pin：str類型，引腳

### **12.4.2 光照度**

`value()`

* 返回值，int類型，0\~4095

## 12.5 土壤濕度傳感器模塊

### 12.5.1 構造對象

`class sugar.Soil(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

soil_p1 = Soil('P1')
```

### 12.5.2 土壤濕潤度

`value()`

* 返回值，int類型，0\~4095

## 12.6 雨滴水位傳感器模塊

### 12.6.1 構造對象

`class sugar.WaterLevel(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

waterLever_p1 = WaterLevel('P1')
```

### **12.6.2 水位**

`value()`

* 返回值，int類型，0\~4095

## 12.7 聲音模塊

### 12.7.1 構造對象

`class sugar.Sound(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

sound_p1 = Sound('P1')
```

### 12.7.2 聲音強度

`value()`

* 返回值，int類型，0\~4095

## 12.8 水溫傳感器模塊

### 12.8.1 構造對象

`class sugar.DS18X20(pin)`

參數

* pin：str類型，引腳

```python
from sugar import *

ds1 = DS18X20('P1')
```

### 12.8.2 獲取水溫

`temperature`

* 返回值，double類型(攝氏度)
