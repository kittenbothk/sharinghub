# Sugar 磁力感應模組

![](https://kittenbothk.readthedocs.io/en/latest/\_images/magnet1.png)

這是一隻磁力感應模組，可以感應附近是否有磁石。背後亦設有塑膠積木孔，可以完美配搭塑膠積木使用。

### 產品參數

* 尺寸：24 x 24 x 16 mm
* 重量：4.7g
* 訊號：有磁石時返回0，否則返回1

### 產品接線

用3Pin 連接線將模組與Robotbit Edu連接起來。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/magnet\_wire.png)

### 編程教學

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner15.png)

#### 加載Sugar插件：

#### 在擴展頁直接搜尋sugar (sugar已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/sugar\_search.gif)

#### 你亦可以用插件地址搜尋

Sugar插件：https://github.com/KittenBot/pxt-sugar

#### [詳細方法](../../programmingplatforms/makecode/kittenbotandmakecode.md)

{% embed url="https://makecode.microbit.org/_LRV7D0FrfAtU" %}

[參考程式](https://makecode.microbit.org/\_LRV7D0FrfAtU)

#### Kittenblock 編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner9.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/magnet3.png)

#### MicroPython編程教學

```
Hall(pin)
value()
```

* value(): 有磁石時返回0，否則返回1

參考程式

```
from future import *
from sugar import *

hall = Hall('P1')

while True:
    if hall.value():
        buzzer.tone(440, -1)
    else:
        buzzer.stop()
```
