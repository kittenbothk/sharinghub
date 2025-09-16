# 3 音樂

## 3 音樂

### 3.1 構建對象

`class future.Buzz()`

```python
from future import *

buzzer = Buzz()
```

### **3.2** 頻率播放

`tone(hz,sec)`

參數

* hz：int類型，蜂鳴器頻率
* sec，int類型，持續時間，為-1時持續播放

### **3.3 音符播放**

`note(note,beat)`

參數

* note：int類型，以音符為單位來設置
* beat：double類型，以節拍為單位設置延時

### **3.4 播放旋律**

`melody(music,bpm)`

參數

* music：str類型，音符組
  * 以c4:2為例子    \
    c：英式命名法，代表音調，分別對應著do\~xi，一個八度大致分為cdefab這7個調子。    \
    4：八度，比如4，為第四八度    \
    :2：持續時間，以bpm=120且四分音符為一拍的默認情況下，1秒2拍=>0.5秒/拍，2則代表著4分音符的一半，所以該c4:2的時長持續為0.25s    \
    每個音符之間通過空格分隔
* bpm：int類型，節拍

### 3.5 播放預置旋律

`melody(music,bpm)`

參數

* bpm：節拍
* music：str類型

{% hint style="info" %}
CORRECT, NOTICE, ERROR, BA\_DING, JUMP\_UP, JUMP\_DOWN, POWER\_UP, POWER\_DOWN, DADA, PUNCHLINE, ENTERTAINER, ODE, WEDDING, BIRTHDAY, CHASE, BLUES, PRELUDE, NYAN, RING, FUNK, FUNERAL, BADDY, WAWA
{% endhint %}

### **3.6 停止播放**

`stop()`
