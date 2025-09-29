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
