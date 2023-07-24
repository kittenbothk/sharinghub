# 未來板MicroPython編程14：Sugar模組與Powerbrick魔塊

### 導入Sugar庫

需要先導入Sugar的庫才可以使用Sugar模組與Powerbrick魔塊。

```
from sugar import *
```

### 14: Sugar模組與Powerbrick魔塊

### PIR人體紅外模組

```
# pin=['P0','P1','P2','P3','P8','P9','P12','P13','P14','P15','P16']

value=PIR(pin).value()
```

* pin為模組引腳。

### 紅外線巡線模組

```
# pin=['P0','P1','P2','P3','P8','P9','P12','P13','P14','P15','P16']

value=Tracker(pin).value()
```

* pin為模組引腳。

### 磁力感應模組

```
# pin=['P0','P1','P2','P3','P8','P9','P12','P13','P14','P15','P16']

value=Hall(pin).value()
```

* pin為模組引腳。

### 按鍵模組

```
# pin=['P0','P1','P2','P3','P8','P9','P12','P13','P14','P15','P16']

value=Button(pin).value()
```

* pin為模組引腳。

### LED模組

```
# pin=['P0','P1','P2','P3','P8','P13','P14','P15','P16']
# state=['ON','OFF']

LED(pin).state(state) #ON/OFF
LED(pin).brightness(brightness) #亮度
```

* pin為模組引腳。
* state為狀態。
* brightness為亮度，0\~100。

### 火焰模組

```
# pin=['P0','P1','P2','P3','P12','P14','P15','P16']

value=Flame(pin).value()
```

* pin為模組引腳。

### 旋轉電位器模組

```
# pin=['P0','P1','P2','P3','P12','P14','P15','P16']

value=Angle(pin).value()
```

* pin為模組引腳。

### 光敏感應模組

```
# pin=['P0','P1','P2','P3','P12','P14','P15','P16']

value=Light(pin).value()
```

* pin為模組引腳。

### 光敏感應模組

```
# pin=['P0','P1','P2','P3','P12','P14','P15','P16']

value=Light(pin).value()
```

* pin為模組引腳。

### 土壤濕度模組

```
# pin=['P0','P1','P2','P3','P12','P14','P15','P16']

value=Soil(pin).value()
```

* pin為模組引腳。

### 雨滴水位模組

```
# pin=['P0','P1','P2','P3','P12','P14','P15','P16']

value=WaterLevel(pin).value()
```

* pin為模組引腳。

### 環境溫濕度模組(Sugar)

```
temperature=ENV().update()[0]
humidity=ENV().update()[1]
```

### 激光測距模組

```
value=TOFDistance().value()
```

### 搖桿模組

```
# position=['up', 'down', 'left', 'right', 'pressed']

position=Joystick().state() #搖桿位置
x_value=Joystick().value('x') #搖桿X值
y_value=Joystick().value('y') #搖桿Y值
```

### 時鐘模組

```
# field=['all','year','month','day','week','hour','minute','second']

Clock().setTime((year,month,day,weekday,hour,min,sec)) #設置時鐘時間
Clock().modeSet(state=mode) #啟動或暫停時鐘
Clock().refreshTime(8) #時鐘設為網絡時間
value=Clock().getTime(field) #獲取時間信息
```

### 貓耳超聲波

```
# pin=['P0','P1','P2','P3','P8','P9','P12','P13','P14','P15','P16']

value=MeowSonar(pin).ping()
```

* pin為模組引腳。

### RFID探測魔塊

```
RFID().probe() #RFID探測
RFID().uuid() #獲取UUID
RFID().stop() #結束RFID探測
RFID().write(SECTOR, BLOCK, DATA) #RFID寫入數據
RFID().read(SECTOR, BLOCK) #RFID讀取數據
```

* SECTOR為RFID分區，1\~16。
* BLOCK為RFID區塊，0\~2。
* DATA為寫入的數據。

### 顏色手勢魔塊

```
#type=[1,2,3,4]

ColorGes().mode(type) #顏色手勢設定模式

hue = ColorGes().read(0) #獲取色環HUE
brightness = ColorGes().read(1) #獲取亮度
distance = ColorGes().distance() #獲取距離
gesture = ColorGes().gesture() #獲取手勢

ColorGes().ledpwm(0) #LED亮度
ColorGes().led((0,0,0,0)) #LED控制
```

* type為顏色手勢魔塊模式。
  * 顏色模式: 1
  * 距離模式: 2
  * 手勢模式: 3
  * LED模式: 4
* LED亮度: 0\~100。
* LED控制: 0為關，1為開。

### MP3魔塊

```
# op=[MP3().PLAY, MP3().STOP, MP3().NEXT, MP3().PREV]

MP3().operate(op) #MP3模組控制
MP3().vol(volume) #MP3模組音量
MP3().playIndex(index) #MP3播放序號
MP3().playName(name) #MP3播放名稱
```

* op為MP3的指令，包括播放、停止、下一首、上一首。
  * MP3播放: MP3().PLAY
  * MP3停止: MP3().STOP
  * MP3下一首: MP3().NEXT
  * MP3上一首: MP3().PREV
* volume為音量，0\~30。
* index為歌曲在SD卡上的序號。
* name為歌曲名稱，最長8個字。

### 環境溫濕度模組(Powerbrick)

```
pin=['P0','P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16']

dht11 = DHT11(pin) #初始化環境溫濕度模組
dht11.measure() #環境溫濕度模組測量
temperature = dht11.temperature() #環境溫度
humidity = dht11.humidity() #環境濕度
```

* pin為模組引腳。

### 水溫感應器

```
# pin=['P0','P1','P2','P3','P8','P9','P12','P13','P14','P15','P16']

value=DS18B20(pin).read()
```

* pin為模組引腳。
