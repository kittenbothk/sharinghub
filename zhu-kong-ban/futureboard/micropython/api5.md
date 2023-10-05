# 未來板MicroPython編程5：引腳

## 未來板MicroPython編程5：引腳

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 05: 引腳類

#### 1. 引腳初始化

```
MeowPin(pin,mode)
```

pin為引腳，例如P1，P2。

mode為模式，有4種模式：

1. 數位輸入：’IN’
2. 數位輸出：’OUT’
3. 模擬輸入：’ANALOG’
4. 模擬輸出：’PWM’

#### 2. 數位讀取

```
getDigital() 
```

#### 2使用範例

```
from future import *
# 數位讀取=['P0','P1','P2','P3','P8','P9','P12','P13','P14','P15','P16']
p0 = MeowPin('P0','IN')
print(p0.getDigital())
```

#### 3. 數位寫入

```
setDigital(val)
```

#### 3使用範例

```
from future import *
import time
# 數位寫入=['P0','P1','P2','P6','P7','P8','P10','P13','P3','P9','P14','P15','P16']
p0 = MeowPin('P0','OUT')
while 1:
    p0.setDigital(1)
    time.sleep(1)
    p0.setDigital(0)
    time.sleep(1)
```

#### 4. 模擬讀取

```
getAnalog(width)
```

width為解像度，可以選擇10位(0\~1023)或12位(0\~4095)。默認為12位。

#### 4使用範例

```
from future import *
# 模擬讀取=['P0','P1','P4','P12', 'P3', 'P14', 'P15', 'P16']

p0 = MeowPin('P0','ANALOG')
print(p0.getAnalog())
print(p0.getAnalog(width=10))
```

#### 5. 模擬寫入

```
setAnalog(val)
```

可以寫入0\~1023。

#### 5使用範例

```
from future import *
import time
# 模擬寫入=['P0','P1','P2','P3','P8','P13','P14','P15','P16']

p0 = MeowPin('P0','PWM')
while 1:
    for i in range(1023): 
        p0.setAnalog(i)
        time.sleep_ms(1)
    for i in range(1023,0,-1): 
        p0.setAnalog(i)
        time.sleep_ms(1)
```
