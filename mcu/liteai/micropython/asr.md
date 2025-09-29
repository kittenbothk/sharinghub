# 14 串口模塊

## 14.1 語音識別模塊

### 14.1.1 構造對象

`class sugar.SugarASR()`

```python
from sugar import *

asr = SugarASR('uart0')
```

### 14.1.2 語音識別被觸發

`detected()`

* 返回值：bool類型

### 14.1.3 識別結果

`cmd`

* 返回值：str類型，返回識別結果的代號，具體參考

{% content-ref url="../../../airelated/asr/serial.md" %}
[serial.md](../../../airelated/asr/serial.md)
{% endcontent-ref %}

```python
#for example

if asr.cmd == '400':
```

### 14.1.4 播報語句

`tts_words(id)`

* id：int類型，播報tts語句，id具體參考

{% content-ref url="../../../airelated/asr/serial.md" %}
[serial.md](../../../airelated/asr/serial.md)
{% endcontent-ref %}

### 14.1.5 播報整數

`tts_int(number)`

* number：int類型

### 14.1.6 播報小數

`tts_double(decimal)`

* decimal：double類型

### 14.1.7 播報日期

`asr.tts_date(y,m,d)`

* y：int類型，年
* m：int類型，月
* d：int類型，日

### 14.1.8 播報時間

`asr.tts_clock(h,m)`

* h：int類型，時
* m：int類型，分



