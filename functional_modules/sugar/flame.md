# Sugar 火焰感應模組

![](https://kittenbothk.readthedocs.io/en/latest/\_images/flame1.png)

這是一隻火焰感應模組，可以檢測火焰的強度。背後亦設有塑膠積木孔，可以完美配搭塑膠積木使用。

### 產品參數

* 尺寸：24 x 24 x 23 mm
* 重量：6.7g
* 訊號：模擬信號0\~1023/0\~4095

### 產品接線

#### Robotbit Edu

用3Pin 連接線將模組與Robotbit Edu連接起來。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/flame\_wire.png)

#### Robotbit 2.2

用3Pin 連接線將模組與Robotbit 2.2連接起來。

<figure><img src="../../.gitbook/assets/flame_wiring_2.2.png" alt=""><figcaption></figcaption></figure>

### 編程教學

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner15.png)

#### 加載Sugar插件：

#### 在擴展頁直接搜尋sugar (sugar已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/sugar\_search.gif)

#### 你亦可以用插件地址搜尋

Sugar插件：https://github.com/KittenBot/pxt-sugar

#### [詳細方法](../../programmingplatforms/makecode/kittenbotandmakecode.md)

{% embed url="https://makecode.microbit.org/_X7zfCJ3cD6rf" %}

[參考程式](https://makecode.microbit.org/\_X7zfCJ3cD6rf)

#### Kittenblock 編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/flame3.png)

#### MicroPython 編程教學

```
Flame(pin)
value()
```

* value(): 模擬信號0\~1023/0\~4095

參考程式

```
from future import *

from sugar import *

flame_P0 = Flame('P0')

x = 0

screen.sync = 0
while True:
  screen.fill((0, 0, 0))
  screen.text(flame_P0.value(),5,10,2,(0, 119, 255))
  screen.refresh()
```
