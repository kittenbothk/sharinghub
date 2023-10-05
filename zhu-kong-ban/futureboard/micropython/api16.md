# 未來板MicroPython編程16：KOI

### 導入 KOI 庫

需要先導入KOI的庫才可以使用KOI。

```
from futureKOI import KOI
```

### KOI 基本應用

#### 初始化KOI

```
koi = KOI(tx='P2',rx='P12',id=1)
```

初始化KOI

* tx為模組藍色線，配合Robotbit Edu使用請填P2。
* rx為模組綠色線，配合Robotbit Edu使用請填P12。

#### 改變屏幕方向

```
# available modes
# 0,2

koi.screen_mode(mode, cmd='K6')
```

改變屏幕方向。

* mode：0代表前置鏡頭，2代表後置鏡頭。

#### 顯示字串

```
koi.text(x, y, delay, text, cmd="K4")
```

在屏幕顯示字串。

* x和y: 文字左上角的座標。
* text: 字串。
* delay: 延時，字串顯示時間。

#### 截圖

```
koi.screen_save(pic , cmd="K2")
```

用KOI拍照。

* pic: 檔案名稱(.jpg)

#### 顯示相片

```
koi.screen_show(pic, cmd="K1")
```

顯示相片。

* pic: 檔案名稱(.jpg)

### 人臉追蹤

#### 載入人臉模型

```
koi.face_yolo_load(cmd="K30")
```

載入人臉模型。

#### 運行人臉追蹤(單個人臉)

```
x = koi.face_detect(cmd="K31")
```

運行人臉追蹤。

#### 獲取人臉坐標

```
koi.get_re(cmd="K31")[0]  #x
koi.get_re(cmd="K31")[1]  #y
```

獲取人臉坐標。

#### 運行人臉追蹤(多個人臉)

```
koi.face_count(cmd="K32")
```

運行人臉追蹤。

#### 獲取人臉數量

```
koi.get_re(cmd="K32")[0]
```

獲取人臉數量。

### 人臉追蹤範例程式

```
from future import *
from futureKOI import KOI

screen.sync = 0
koi = KOI(tx='P2',rx='P12',id=1)
koi.screen_mode(2, cmd='K6')
koi.face_yolo_load(cmd='K30')
while True:
if koi.face_detect(cmd='K31'):
    screen.fill((0, 0, 0))
    screen.text("Face detected:",5,10,1,(255, 255, 255))
    screen.text("X:",5,20,2,(255, 255, 255))
    screen.text((koi.get_re(cmd='K31')[0]),5,40,3,(255, 255, 255))
    screen.text("Y:",5,70,2,(255, 255, 255))
    screen.text((koi.get_re(cmd='K31')[1]),5,90,3,(255, 255, 255))
    screen.refresh()
else:
    screen.fill((0, 0, 0))
    screen.text("No face",5,10,1,(255, 255, 255))
    screen.refresh()
sleep(0.5)
```

### 特徵分類器

#### 初始化分類器

```
koi.init_cls()
```

初始化特徵分類器。

#### 保存分類器模型

```
koi.cls_save_model(model,cmd="K43")
```

保存分類器模型。

* model: 檔案名稱(.json/.bin)

#### 載入分類器模型

```
koi.cls_load_model(model="abc.json",cmd="K44")
```

載入分類器模型。

* model: 檔案名稱(.json/.bin)

#### 添加標籤

```
koi.cls_add_tag(tag,cmd="K41")
```

提取特徵添加標籤。

* tag: 物件標籤

#### 執行特徵分類

```
koi.cls_run(cmd="K42")
```

返回特徵分類。

### KOI特徵分類器範例程式(模型訓練)

```
from future import *
from futureKOI import KOI

items = []
i = 0

items.append('rock')
items.append('paper')
items.append('scissors')
i = 0
koi = KOI(tx='P2',rx='P12',id=1)
koi.init_cls()                                                      # init classifier
koi.screen_mode(2, cmd='K6')    
screen.sync = 0
while True:
screen.fill((0, 0, 0))
if sensor.btnValue("a") and sensor.btnValue("b"):
    koi.cls_save_model(model="model.json",cmd='K43')                # saves the classifier model
    buzzer.melody(1)
else:
    if sensor.btnValue("a"):
    sleep(0.2)
    if not sensor.btnValue("b"):
        koi.cls_add_tag(id=(items[int((i % 3 + 1) - 1)]),cmd='K41') # classifier add tag
        buzzer.melody(4)
    else:
    if sensor.btnValue("b"):
        sleep(0.2)
        buzzer.tone(440,0.2)
        if not sensor.btnValue("a"):
        i += 1
screen.text("Now training:",0,10,1,(255, 255, 255))
screen.text((items[int((i % 3 + 1) - 1)]),0,30,2,(255, 255, 255))
screen.text("Press A to add tag",0,60,1,(255, 255, 255))
screen.text("Press B for next tag",0,80,1,(255, 255, 255))
screen.text("Press A+B to save",0,100,1,(255, 255, 255))
screen.refresh()
```

### KOI特徵分類器範例程式(模型運行)

```
from future import *
from futureKOI import KOI

koi = KOI(tx='P2',rx='P12',id=1)
koi.screen_mode(2, cmd='K6')
koi.init_cls()
koi.cls_load_model(model="model.json",cmd='K44')                    # loads the classifier model
while True:
if sensor.btnValue("a"):
    screen.clear()
    screen.text((koi.cls_run(cmd='K42')),5,10,2,(255, 255, 255))    # displays the classified tag
    screen.refresh()
```

### 顏色追蹤

#### 顏色校正

```
koi.color_cali(name ,cmd="K16")
```

校正要追蹤的顏色。

* name: 顏色

#### 追蹤色塊

```
koi.color_tracking(name="name", cmd="K15")
# returns [cx,cy,w,h,name]
```

追蹤色塊，並返回色塊數值。

* name: 顏色

#### 獲取色塊數值

```
koi.get_re(cmd="K15")[0] #cx
koi.get_re(cmd="K15")[1] #cy
koi.get_re(cmd="K15")[2] #w
koi.get_re(cmd="K15")[3] #h
```

獲取色塊數值。

### 顏色追蹤範例程式

```
from future import *
from futureKOI import KOI

koi.screen_mode(2, cmd='K6')
koi = KOI(tx='P2',rx='P12',id=1)
while True:
if sensor.btnValue("a"):
    koi.color_cali(name="red" ,cmd='K16')
    sleep(0.3)
if sensor.btnValue("b"):
    if koi.color_tracking(name="red", cmd='K15'):
    screen.clear()
    screen.text((koi.get_re(cmd='K15')[0]),5,10,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K15')[1]),5,20,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K15')[2]),5,30,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K15')[3]),5,40,1,(255, 255, 255))
    screen.refresh()
    sleep(0.3)
```

#### 追蹤巡線

```
koi.line_tracking(name ,cmd="K12")
# returns [x1, y1, x2, y2, name]
```

追蹤巡線，並返回巡線數值。

* name: 顏色

#### 獲取巡線數值

```
koi.get_re(cmd="K12")[0] #x1
koi.get_re(cmd="K12")[1] #y1
koi.get_re(cmd="K12")[2] #x2
koi.get_re(cmd="K12")[3] #y2
```

獲取巡線數值。

### 追蹤巡線範例程式

```
from future import *
from futureKOI import KOI

koi.screen_mode(2, cmd='K6')
koi = KOI(tx='P2',rx='P12',id=1)
while True:
if sensor.btnValue("a"):
    koi.color_cali(name="red" ,cmd='K16')
    sleep(0.3)
if sensor.btnValue("b"):
    if koi.line_tracking(name="red" ,cmd='K12'):
    screen.clear()
    screen.text((koi.get_re(cmd='K12')[0]),5,10,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K12')[1]),5,20,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K12')[2]),5,30,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K12')[3]),5,40,1,(255, 255, 255))
    screen.refresh()
    sleep(0.3)
```

### 幾何圖形識別

#### 圓形追蹤

```
koi.circle_detect(threshold, cmd="K10")
```

追蹤畫面裡的圓形。

* threshold: 臨界值，越高越難追蹤，一般建議4000。

#### 獲取圓形數值

```
koi.get_re(cmd="K10")[0] #cx
koi.get_re(cmd="K10")[1] #cy
koi.get_re(cmd="K10")[2] #r
```

獲取圓形數值。

#### 矩形追蹤

```
 koi.rectangle_detect(th=4000,cmd="K11")
```

追蹤畫面裡的矩形。

* threshold: 臨界值，越高越難追蹤，一般建議4000。

#### 獲取矩形數值

```
koi.get_re(cmd="K11")[0]
koi.get_re(cmd="K11")[1]
koi.get_re(cmd="K11")[2]
koi.get_re(cmd="K11")[3]
```

獲取矩形數值。

### 幾何圖形識別範例程式

```
from futureKOI import KOI
from future import *

koi.screen_mode(2, cmd='K6')
koi = KOI(tx='P2',rx='P12',id=1)
while True:
if sensor.btnValue("a"):
    if koi.circle_detect(th=4000, cmd='K10'):
    screen.clear()
    screen.text((koi.get_re(cmd='K10')[0]),5,10,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K10')[0]),5,20,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K10')[0]),5,30,1,(255, 255, 255))
    screen.refresh()
    sleep(0.3)
if sensor.btnValue("b"):
    if koi.rectangle_detect(th=4000,cmd='K11'):
    screen.clear()
    screen.text((koi.get_re(cmd='K11')[0]),5,10,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K11')[1]),5,20,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K11')[2]),5,30,1,(255, 255, 255))
    screen.text((koi.get_re(cmd='K11')[3]),5,40,1,(255, 255, 255))
    screen.refresh()
    sleep(0.3)
```

### 條碼識別

#### QR Code識別

```
koi.scan_qrcode(cmd="K20")
```

識別畫面裡的QR Code。

#### Barcode識別

```
koi.scan_barcode(cmd="K22")
```

識別畫面裡的Barcode。

#### AprilTag識別

```
koi.scan_Apriltag(cmd="K23")
```

識別畫面裡的AprilTag。

#### AprilTag數值

```
koi.get_re(cmd="K23")[0] #id
koi.get_re(cmd="K23")[1] #cx
koi.get_re(cmd="K23")[2] #cy
koi.get_re(cmd="K23")[3] #w
koi.get_re(cmd="K23")[4] #h
```

獲取AprilTag數值。

### 條碼識別範例程式

```
from future import *
from futureKOI import KOI

koi = KOI(tx='P2',rx='P12',id=1)
koi.screen_mode(2, cmd='K6')
while True:
if sensor.btnValue("a"):
    screen.clear()
    screen.text((koi.scan_qrcode(cmd='K20')),5,10,2,(255, 255, 255))
if sensor.btnValue("b"):
    screen.clear()
    screen.text((koi.scan_barcode(cmd='K22')),5,10,2,(255, 255, 255))
```

### 物聯網

#### 連接網絡

```
koi.connect_wifi(router ,pwd ,cmd="K50")
```

連接WiFi網絡。

* router: 網絡SSID
* pwd: 網絡密碼

#### 獲取IP地址

```
koi.get_ip(cmd="K54")
```

獲取IP地址。

### 百度AI

#### 百度AI人臉辨識

```
koi.baiduAI_face_detect(cmd="K75")
# returns [face token, age, sex, mask, emotion]
```

運行百度AI人臉辨識並返回人臉數值。

#### 獲取人臉特徵碼

```
koi.get_re(cmd="K75")[0]
```

獲取人臉特徵碼。

#### 添加人臉到組別

```
koi.baiduAI_face_add(face_token="token" ,groupName="group" ,faceName="name" ,cmd="K76")
```

添加人臉到組別。

* face\_token: 人臉特徵碼
* groupName: 組別名稱
* faceName: 人臉名稱

#### 在組別搜尋人臉

```
koi.baiduAI_face_search(face_token="token" ,groupName="group" ,cmd="K77")[0]
```

在組別搜尋人臉並返回人臉名稱。

* face\_token: 人臉特徵碼
* groupName: 組別名稱

#### 文字轉語音

```
koi.baiduAI_tts(text ,cmd="K78")
```

文字轉語音。

\-text: 文字，不支援空白鍵

### 物聯網文字轉語音範例程式

```
from future import *
from futureKOI import KOI

koi = KOI(tx='P2',rx='P12',id=1)
koi.screen_mode(2, cmd='K6')
koi.connect_wifi(router="apname" ,pwd="password" ,cmd='K50')
while True:
if sensor.btnValue("a"):
    koi.baiduAI_tts(txt='"hello"' ,cmd='K78')
    sleep(0.2)
if sensor.btnValue("b"):
    screen.clear()
    screen.text((koi.get_ip(cmd='K54')),5,10,1,(255, 255, 255))
    screen.refresh()
    sleep(0.2)
```

### 語音辨識

#### 錄製wav音頻檔

```
koi.audio_record(name)
```

錄製wav音頻檔。

* name: 檔案名稱(.wav)

#### 播放wav音頻檔

```
koi.audio_play(name)
```

播放wav音頻檔。

* name: 檔案名稱(.wav)

#### 校正環境噪音

```
koi.audio_noisetap()
```

校正環境噪音，語音辨識前必須運行。

#### 語音辨識增加命令詞

```
koi.speech_add_tag(tag)
```

增加語音辨識命令詞。

* tag: 命令詞

#### 運行語音辨識

```
koi.speech_run(cmd="K65")
```

運行語音辨識，返回命令詞。

#### 儲存語音模型

```
koi.speech_save_model(file)
```

儲存語音模型。

* file: 檔案名稱(.json)

#### 載入語音模型

```
koi.speech_load_model(file)
```

載入語音模型。

* file: 檔案名稱(.json)

### 語音辨識模型訓練範例程式

```
from future import *
from futureKOI import KOI

items = []
i = 0


items.append('rock')
items.append('paper')
items.append('scissors')
i = 0
koi = KOI(tx='P2',rx='P12',id=1)
koi.audio_noisetap()
koi.screen_mode(2, cmd='K6')
screen.sync = 0
while True:
screen.fill((0, 0, 0))
if sensor.btnValue("a") and sensor.btnValue("b"):
    buzzer.melody(1)
    koi.speech_save_model("speech.json")
else:
    if sensor.btnValue("a"):
    sleep(0.2)
    if not sensor.btnValue("b"):
        koi.speech_add_tag((items[int((i % 3 + 1) - 1)]))
    else:
    if sensor.btnValue("b"):
        sleep(0.2)
        buzzer.tone(440,0.2)
        if not sensor.btnValue("a"):
        i += 1
screen.text("Now training:",0,10,1,(255, 255, 255))
screen.text((items[int((i % 3 + 1) - 1)]),0,30,2,(255, 255, 255))
screen.text("Press A to add tag",0,60,1,(255, 255, 255))
screen.text("Press B for next tag",0,80,1,(255, 255, 255))
screen.text("Press A+B to save",0,100,1,(255, 255, 255))
screen.refresh()
```

### 語音辨識模型運行範例程式

```
from future import *
from futureKOI import KOI


koi = KOI(tx='P2',rx='P12',id=1)
koi.audio_noisetap()
koi.speech_load_model("speech.json")
while True:
if sensor.btnValue("a"):
    screen.clear()
    screen.text((koi.speech_run(cmd='K65')),5,10,2,(255, 255, 255))
    screen.refresh()
```

### 雜項

#### 重設KOI

```
koi.reset(cmd='k99')
```

重設KOI

#### 停止分類器

```
koi.stop_kpu(cmd='k98')
```

停止分類器
