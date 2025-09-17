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

返回值，int類型，0\~4095
