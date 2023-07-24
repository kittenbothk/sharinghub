# Sugar 人體紅外感應模組

![](https://kittenbothk.readthedocs.io/en/latest/\_images/pir1.png)

這是一隻人體紅外感應模組，可以感測附近是否有人走過。背後亦設有塑膠積木孔，可以完美配搭塑膠積木使用。

### 產品參數

* 尺寸：24 x 24 x 19 mm
* 重量：5.6g
* 訊號：有人靠近時返回0，否則返回1
* 感測距離：5m

### 產品接線

用3Pin 連接線將模組與Robotbit Edu連接起來。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/pir\_wire.png)

### 編程教學

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner15.png)

#### 加載Sugar插件：

#### 在擴展頁直接搜尋sugar (sugar已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/sugar\_search.gif)

#### 你亦可以用插件地址搜尋

Sugar插件：https://github.com/KittenBot/pxt-sugar

#### [詳細方法](../../makecode/kittenbotandmakecode.md)

{% embed url="https://makecode.microbit.org/_D5XF7hEPf489" %}

[參考程式](https://makecode.microbit.org/\_D5XF7hEPf489)

#### Kittenblock 編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner9.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/pir3.png)

#### Micropython 編程教學

```
PIR(pin)
value()
```

* value(): 有人靠近時返回0，否則返回1

參考程式

```
from future import *
from sugar import *

pir = PIR('P1')

neopix=NeoPixel("P7",3)

while True:
    if pir.value():
        neopix.setColorAll((103, 0, 0))
    else:
        neopix.setColorAll((0,0,0))
```
