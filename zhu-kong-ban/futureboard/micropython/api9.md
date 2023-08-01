# 未來版MicroPython編程9：I2S麥克風

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 09: I2S麥克風

### 導入麥克風庫

```
import audio
```

#### 1. 初始化I2S麥克風

```
au=audio.Audio()
```

#### 2. 獲取聲音強度

```
au.loudness()
```

返回聲音強度，範圍由0\~4095。

#### 3. 雲端語音辨識(效果可能不準確，只建議高階用家使用)

```
au.recognize(sec=1,vid=1737)
```

進行語音辨識，需要網絡連線。

sec為語音長度，建議為1\~3秒。

vid為語言，現時支援4種語言：

1. 1537:普通話
2. 1737:英文
3. 1637:粵語
4. 1837:四川話

#### 聲音強度範例程式

```
import time
import audio
au = audio.Audio() 

while 1:
  time.sleep(0.1)
  print(au.loudness())
```

#### 語音辨識範例程式

```
from future import *

import audio
au = audio.Audio()

wifi.connect(wifiname), wifipw)
screen.clear()
screen.text(au.recognize(vid=1737, sec=2),5,10,1,(0, 119, 255))
```
