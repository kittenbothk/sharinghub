# 未來板MicroPython編程12：取得開放API數據

未來板可以用urequests與ujson存取各款API的開放數據，詳情可以參閱urequests與ujson的官方教學。

### 導入未來板庫

需要先導入未來板的庫才可以使用未來板的硬件。

```
from future import *
```

### 12: 取得開放API數據

### 導入HTTP GET庫

```
import urequests
import ujson
```

#### 1. 取得數據

```
r=urequests.get(api_url)
data=ujson.loads(r.content)
```

請在api\_url裏填入API的GET指令。

請自行在data裡面抽出自己所要的數據。
