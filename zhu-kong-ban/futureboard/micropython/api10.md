# 未來板MicroPython編程10：無綫通訊

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 10: 無綫通訊

### 導入無綫通訊庫

```
from radio import *
```

#### 1. 初始化無綫通訊

```
r=Radio(trigger)
```

可以在括號裏呼叫函數，每當收到訊息時會自動觸發。

#### 2. 設定通訊頻道

```
r.channel=1
```

需要雙方都在同一個頻道上才能通訊。

#### 3. 讀取訊息

```
r.read()
```

#### 4. 發佈信息

```
r.send(msg)
```

#### 範例程式1：直接讀取

```
import time
from radio import *

r = Radio()
print('channel', r.channel)
r.channel = 12 

while True:
    time.sleep(1)
    a = r.read()
    if a:
        print('get', a)
```

#### 範例程式2：自動觸發

```
from radio import *

def onmsg(msg, mac):
    print('get', msg, 'from', mac)

r = Radio(onmsg)
print('channel', r.channel)
r.channel = 12
r.send("hello world")
```

#### 進階範例程式：MESH無綫通訊(ESPNOW)

```
# 1. 啟動WiFi
import network
w0 = network.WLAN(network.STA_IF)
w0.active(True)

# 2. 取得自機的MAC地址
mac = w0.config('mac')
>>> mac
b'\xc4O3"\xdb\x89'

# 3. 導入espnow
from esp import espnow
e = espnow.ESPNow()
e.init()

# 4. 加入對方的MAC地址
# 注意： 不是自己的MAC地址
e.add_peer(b'\x8c\xaa\xb5\xb9\xf8\xf0')

# 5. 信息觸發
def rxcb(mac, msg):
    print("Recv:", mac, msg)
e.on_recv(rxcb)

# 6. 發佈信息
e.send(b'\x8c\xaa\xb5\xb9\xf8\xf0', 'hello world')

# 在接收端可以看到
# Recv: b'\xc4O3"\xdb\x89' b'hello world'
```
