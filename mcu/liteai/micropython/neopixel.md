# 5 彩燈

## 5 彩燈

### 5.1 構建對象

`class future.NeoPixel(pin,quantity)`

參數

* pin：str類型，引腳
  * NEOPIX：板載彩燈
  * P1
  * P2
  * P3
  * P4
* quantity：int類型，菜單數量

```python
from future import *

neopix=NeoPixel('NEOPIX', 3)
```

### 5.2 設置彩燈亮度

`setbrightness(light)`

參數

* light：int類型，範圍0\~100

### 5.3 設置單個彩燈顏色

`setColor(index,color)`

參數

* index：int類型，彩燈序號
* color：rgb顏色

### 5.4 設置全部彩燈顏色

`setColorAll(color)`

參數

* color：rgb顏色

### 5.5 刷新彩燈顯示

`update()`

### 5.6 預置彩燈效果

`breath(neopix)`

`flow(neopix)`

`rainbow(neopix)`

`firefly(neopix)`

`blink(neopix)`

`heartbeat(neopix)`

`brighter(neopix)`

`dimmer(neopix)`
