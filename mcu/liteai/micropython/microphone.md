# 8 麥克風

## 8 麥克風

### 8.1 構建對象

`class audio.Audio()`

```python
from audio import Audio

au = Audio()
```

### 8.2 獲取聲音強度

`loudness()`

* 返回值：int類型，聲音強度

### 8.3 識別語音

{% hint style="info" %}
需要先連接wifi
{% endhint %}

`recognize(vid,sec)`

參數

* vid：int類型，語音類型
  * 1537：普通話
  * 1637：粵語
  * 1737：英文
  * 1837：四川話
* 返回值：str類型，識別結果
