# 7 無線通訊

## 7 無線通訊

### 7.1 構建對象

`class radio.Radio(channel)`

參數

* channel：int類型，通訊頻道，範圍1\~13

```python
from uwifi import Radio

radio = Radio(12)
```

### 7.2 發送無線消息

`send(message)`

參數

* message：str類型

### 7.3 接收無線消息

`read()`

* 返回值：str類型，未收到消息則為None

### 7.4 向指定話題發送消息

`sendForKey(topic,message)`

參數

* topic：str類型，話題名稱
* message：str類型，消息內容

### 7.5 接收指定話題的消息

`readForKey(topic)`

參數

* topic：str類型，話題名稱
