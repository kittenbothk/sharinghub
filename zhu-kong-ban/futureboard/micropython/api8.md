# 未來版MicroPython編程8：網絡時間

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 08: 網絡時間

### 導入網絡時間庫

```
from machine import RTC
import ntptime
```

#### 1. 初始化時鐘

```
rtc = RTC()
```

#### 2. 同步網絡時間

```
ntptime.settime(zone=8)
```

zone為時區，默認為8(北京上海香港時間)。

#### 3. 獲取時間

```
rtc.datetime()
```

返回一組列表，格式為年、月、日、星期、時、分、微秒。

#### 網絡時間範例程式

```
#/bin/python
from future import *

import ntptime

from machine import RTC
rtc = RTC()

from time import sleep

wifi.connect(str("wifi"), "password")
ntptime.settime(int(8))
screen.sync = 0
while True:
  screen.fill((0, 0, 0))
  screen.text("Time:",5,10,2,(0, 119, 255))
  screen.text(str(rtc.datetime()[int(4)])+str(str(":")+str(rtc.datetime()[int(5)])),5,40,3,(0, 119, 255))
  screen.refresh()
  sleep(1)
```
