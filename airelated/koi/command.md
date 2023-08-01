# KOI指令API

假如你想使用KOI的指令碼，你可以參照以下列表。你只需要使用這些指令就可以與KOI溝通。

此處提供了Microbit的例子，假如你使用其他主控板請自行修改程式。

### 返回版本號

指令：K0

作用：獲得KOI目前的版本

返回：K0 目前版本號

```
from microbit import *

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)
uart.write('K0\r\n')
sleep(100)
ret_list = []

if uart.any():
    ret = str(uart.readline(), 'UTF-8')
    ret = ret.strip()
    ret_list = ret.split(' ')
    
if len(ret_list)>1:
    display.scroll(ret_list[1])
```

### 拍照與顯示圖片

指令：K1 name.jpg

作用：拍照將圖片儲存

指令：K2 name.jpg

作用：顯示圖片

```
from microbit import *

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K2 pic.jpg\r\n')
    if button_b.is_pressed():
        uart.write('K1 pic.jpg\r\n')
```

### KOI按鍵

指令：K3

作用：KOI按鍵檢測

返回：K3 A按鍵狀態 B按鍵狀態

```
from microbit import *

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)
ret_list = []

while True:
    uart.write('K3\r\n')
    sleep(1000)
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
    if len(ret_list)>1:
        display.scroll('A:')
        display.scroll(ret_list[1])
        display.scroll('B:')
        display.scroll(ret_list[2])
```

### 顯示字串

指令：K4 x y delay string

作用：在座標(x,y)顯示字串，delay代表時長

```
from microbit import *

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)
uart.write('K4 0 0 1000 KOI\r\n')
```

### 改變屏幕方向

指令：K6 direction

作用：改變屏幕方向，0代表前置；1代表橫置；2代表後置

```
from microbit import *

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        uart.write('K6 2\r\n')
    if button_a.is_pressed():
        uart.write('K6 0\r\n')
    if button_b.is_pressed():
        uart.write('K6 1\r\n')
```

### 圓形辨認

指令：K10 threshold

作用：辨認圓形，threshold代表臨界值，一般推薦2000(臨界值越高越難辨認，誤差會更少)

返回：K10 圓心X 圓心Y 半徑

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K10 3000\r\n')
        sleep(1000)
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        if len(ret_list)>1:
            display.scroll('X:')
            display.scroll(ret_list[1])
            display.scroll('Y:')
            display.scroll(ret_list[2])
            display.scroll('R:')
            display.scroll(ret_list[3])
```

### 矩形辨認

指令：K11 threshold

作用：辨認矩形，threshold代表臨界值，一般推薦6000(臨界值越高越難辨認，誤差會更少)

返回：K11 中心X 中心Y 長 闊

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K11 6000\r\n')
        sleep(1000)
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        if len(ret_list)>1:
            display.scroll('X:')
            display.scroll(ret_list[1])
            display.scroll('Y:')
            display.scroll(ret_list[2])
            display.scroll('W:')
            display.scroll(ret_list[3])
            display.scroll('H:')
            display.scroll(ret_list[4])
```

### 線條追蹤

指令：K16 color

作用：追蹤線條前必須要校正顏色，color代表校正的顏色，可以隨意更改

指令：K12 color

作用：追蹤線條，color代表追蹤的顏色

返回：K12 X1座標 Y1座標 X2座標 Y2座標

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)
flag=False

while True:
    if button_a.is_pressed():
        uart.write('K16 test\r\n')
        sleep(2000)
        flag=True
    if flag:
        uart.write('K12 test\r\n')
        sleep(500)
        if uart.any():
            ret = str(uart.readline(), 'UTF-8')
            ret = ret.strip()
            ret_list = ret.split(' ')
            if len(ret_list)>1:
                display.scroll('X1:')
                display.scroll(ret_list[1])
                display.scroll('Y1:')
                display.scroll(ret_list[2])
                display.scroll('X2:')
                display.scroll(ret_list[3])
                display.scroll('Y2:')
                display.scroll(ret_list[4])
            sleep(2000)
```

### 顏色追蹤

指令：K16 color

作用：追蹤顏色前必須要校正顏色，color代表校正的顏色，可以隨意更改

指令：K15 color

作用：追蹤顏色，color代表追蹤的顏色

返回：K5 X座標 Y座標 長 闊

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)
flag=False

while True:
    if button_a.is_pressed():
        uart.write('K16 test\r\n')
        sleep(2000)
        flag=True
    if flag:
        uart.write('K15 test\r\n')
        sleep(500)
        if uart.any():
            ret = str(uart.readline(), 'UTF-8')
            ret = ret.strip()
            ret_list = ret.split(' ')
            if len(ret_list)>1:
                display.scroll('X:')
                display.scroll(ret_list[1])
                display.scroll('Y:')
                display.scroll(ret_list[2])
                display.scroll('W:')
                display.scroll(ret_list[3])
                display.scroll('H:')
                display.scroll(ret_list[4])
            sleep(2000)
```

### 辨識二維碼，條碼

指令：K20

作用：辨識二維碼

返回：K20 內容

指令：K22

作用：辨識條碼

返回：K22 內容

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K20\r\n')
        sleep(500)
    if button_b.is_pressed():
        uart.write('K22\r\n')
        sleep(500)
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        if len(ret_list)>1:
            display.scroll(ret_list[1])
            ret_list=[]
```

### 人臉追蹤

指令：K30

作用：加載人臉模型，必須加載才可以追蹤人臉

指令：K31

作用：人臉追蹤

返回：K0 ID 人臉X 人臉Y

指令：K32

作用：人臉數目

返回：K32 人臉數目

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K30\r\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K31\r\n')
        sleep(500)
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        if len(ret_list)>1:
            display.scroll('X')
            display.scroll(ret_list[2])
            display.scroll('Y')
            display.scroll(ret_list[3])
            ret_list=[]
```

### 分類器

指令：K40

作用：初始化模型分類器

指令：K41 className

作用：特徵提取 className代表這物件的名字

指令：K42

作用：特徵辨認

返回：K42 className

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K40\r\n')
sleep(1000)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        uart.write('K42\r\n')
        sleep(500)
    if button_a.is_pressed():
        uart.write('K41 rock\r\n')
        sleep(500)
    if button_b.is_pressed():
        uart.write('K41 paper\r\n')
        sleep(500)
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        if len(ret_list)>1:
            display.scroll(ret_list[1])
            ret_list=[]
```

指令：K43 name.json

作用：儲存模型分類器 可以儲存為json或bin

```
from microbit import *

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K40\r\n')
sleep(1000)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        uart.write('K43 test.json\r\n')
        sleep(500)
    if button_a.is_pressed():
        uart.write('K41 rock\r\n')
        sleep(500)
    if button_b.is_pressed():
        uart.write('K41 paper\r\n')
        sleep(500)        
```

指令：K44 name

作用：載入分類器

```
from microbit import *

ret_list=[]

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K40\r\n')
sleep(1000)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        uart.write('K44 test.json\r\n')
        sleep(500)
    if button_a.is_pressed():
        uart.write('K42\r\n')
        sleep(500)
        if uart.any():
            ret = str(uart.readline(), 'UTF-8')
            ret = ret.strip()
            ret_list = ret.split(' ')
            if len(ret_list)>1:
                display.scroll(ret_list[1])
                ret_list=[]
```

### WiFi與物聯網

指令：K50 SSID password

作用：加入wifi網絡，SSID代表網絡名稱，password代表網絡密碼

指令：K54

作用：KOI顯示IP地址

```
from microbit import *

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K50 SSID password\r\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K54\r\n')
        sleep(500)
```

指令：K51 mqttHost clientID port \[username] \[password]

作用：連接MQTT伺服器，請按照平台的指示填寫資料

```
假如你使用的平台不需要username和password，則不需要輸入。
```

指令：K52 topic

作用：訂閱MQTT話題

指令：K53 topic message

作用：對MQTT話題發布訊息

指令：K55 topic

作用：讀取MQTT話題

返回：K55 話題內容

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K50 SSID password\r\n')
sleep(500)
uart.write('K51 mqttHost clientID port [username] [password]\r\n')
sleep(500)
uart.write('K52 topic\r\n')
sleep(500)

while True:
    if button_a.is_pressed():
        uart.write('K53 topic message\r\n')
        sleep(500)
    if button_b.is_pressed():
        uart.write('K55 topic\r\n')
        sleep(500)
            if uart.any():
                ret = str(uart.readline(), 'UTF-8')
                ret = ret.strip()
                ret_list = ret.split(' ')
                if len(ret_list)>1:
                    display.scroll(ret_list[1])
                    ret_list=[]
```

### 錄音與播放

指令：K61 sound.wav

作用：錄取一段大約3秒的錄音並儲存下來

指令：K62 sound.wav

作用：播放音頻檔

```
from microbit import *

uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')

while True:
    if button_a.is_pressed():
        uart.write('K61 hello.wav\r\n')
        sleep(500)
    if button_b.is_pressed():
        uart.write('K62 hello.wav\r\n')
        sleep(500)
```

### 語音辨識

指令：K63

作用：設定噪音基準，語音辨認前必須運行

指令：K64 id

作用：添加命令詞，id就是命令詞的名字，成功會顯示綠色

指令：K65

作用：命令詞辨認，成功會顯示綠色

返回：K65 命令詞id

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K63\r\n')
sleep(1000)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        uart.write('K65\r\n')
        sleep(500)
    if button_a.is_pressed():
        uart.write('K64 hi\r\n')
        sleep(500)
    if button_b.is_pressed():
        uart.write('K64 bye\r\n')
        sleep(500)
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        if len(ret_list)>1:
            display.scroll(ret_list[1])
            ret_list=[]
```

指令：K66 sound.json

作用：儲存語音模型

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K63\r\n')
sleep(1000)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        uart.write('K66 greeting.json\r\n')
        sleep(500)
    if button_a.is_pressed():
        uart.write('K64 hi\r\n')
        sleep(500)
    if button_b.is_pressed():
        uart.write('K64 bye\r\n')
        sleep(500)
```

指令：K67 sound.json

作用：讀取語音模型

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
uart.write('K63\r\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K65\r\n')
        sleep(500)
    if button_b.is_pressed():
        uart.write('K67 greeting.json\r\n')
        sleep(500)
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        if len(ret_list)>1:
            display.scroll(ret_list[1])
            ret_list=[]
```

### 人臉辨識

指令：K75

作用：運行人臉辨識(需要網絡連接)

返回：K75 人臉token 年齡 性別 戴口罩 表情

指令：K76 token groupName faceName

作用：將這個人臉token命名為faceName並加到人臉組別groupName(需要網絡連接)

指令：K77 token groupName

作用：在人臉組別用人臉token在人臉組別groupName搜尋(需要網絡連接)

返回：K77 faceName

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)
uart.write('K50 SSID password\r\n')
sleep(1000)

def faceHandle(flag):
    if uart.any():
        ret = str(uart.readline(), 'UTF-8')
        ret = ret.strip()
        ret_list = ret.split(' ')
        if len(ret_list)>1:
            if flag=='add':
                token=ret_list[1]
                uart.write('K76 %s myFriends Mary\r\n' % token)
                sleep(500)
                ret_list=[]
            if flag=='search':
                token=ret_list[1]
                uart.write('K77 %s myFriends\r\n' % token)
                sleep(500)
                faceHandle('return')
            if flag=='return':
                display.scroll(ret_list[1])
                ret_list=[]

while True:
    if button_a.is_pressed():
        uart.write('K75\r\n')
        sleep(500)
        faceHandle('add')
        
    if button_b.is_pressed():
        uart.write('K75\r\n')
        sleep(500)
        faceHandle('search')
```

### 文字轉語音

指令：K78 string

作用：將string變成語音讀出來（支援英文單字或數字，需要網絡連接）

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)
uart.write('K50 SSID password\r\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K78 hello\r\n')
        sleep(500)
        
    if button_b.is_pressed():
        uart.write('K78 9999\r\n')
        sleep(500)
```

### 停止KPU(分類器與人面追蹤)

指令：K98

作用：停止KPU(分類器與人面追蹤)

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K98\r\n')
        sleep(500)
```

### KOI重啟

指令：K99

作用：KOI重啟

```
from microbit import *

ret_list=[]
uart.init(baudrate=115200, tx=pin1, rx=pin2)
uart.write('\n\n')
sleep(1000)

while True:
    if button_a.is_pressed():
        uart.write('K99\r\n')
        sleep(500)
```
