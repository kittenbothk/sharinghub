# 未來板MicroPython編程6：彩燈

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 06: 彩燈類

#### 1. 初始化彩燈

```
NeoPixel(pin, num)
```

pin為彩燈的引腳，未來板上面的彩燈為P7。

num為燈的數量，未來板上的彩燈為3粒。

#### 2. 設置單顆彩燈

```
setColor(i, color)
```

i為燈的序號，由0開始。

color為顏色，可以使用RGB數值或者預設顏色。

#### 3. 設置全部彩燈

```
setColorAll(color)
```

color為顏色，可以使用RGB數值或者預設顏色。

#### 4. 刷新顯示

```
update()
```

所有效果需要刷新才會顯示。

#### 1\~4使用範例

```
from future import *
import time
""" 預設顏色
RED=(255,0,0)
YELLOW=(255,255,0)
PINK=(255,105,180)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
PURPLE=(148,0,211)
CYAN = (0,255,255) 
"""
np = NeoPixel('P7', 3)
color = [RED,GREEN,BLUE]
for i in range(3):
    np.setColorAll(color[i])
    np.update() # 所有效果需要刷新才會顯示
    time.sleep(1)
for i in range(3):
    np.setColor(i,BLACK)
    np.update() # 所有效果需要刷新才會顯示
    time.sleep(1)
```

[Next ](https://kittenbothk.readthedocs.io/en/latest/futureboard/micropython/api7.html)[ Previous](https://kittenbothk.readthedocs.io/en/latest/futureboard/micropython/api5.html)\
