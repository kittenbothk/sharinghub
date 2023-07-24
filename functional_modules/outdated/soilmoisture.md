# 土壤濕度感應器模組

![](https://kittenbothk.readthedocs.io/en/latest/\_images/soil2.png)

這是一隻可以感應土壤濕度的模組，它返回的數值是類比形式。

數值範圍由0-1023，數值越大代表土壤越濕。

### 產品參數

* 工作電壓：3.3V\~5V
* 類型：類比模組
* 接口：3Pin防反插

### 接線教學

```
由於這是類比模組，所以只能使用robotbit的PIN0-2。（使用PIN0的話需要拔除蜂鳴器跳線帽）
```

#### Robotbit Shield

將土壤濕度感應器模組連接到Robotbit Shield的3PIN接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/soil\_wire2.png)

#### Robotbit

將土壤濕度感應器模組連接到Robotbit的針線和3V接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/soil\_wire1.png)

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner14.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/acbanner1.png)

#### 此模組可供Microbit和Meowbit使用。

**讀取土壤濕度數值編程**

#### Microbit:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/poten\_code.png)

#### Meowbit:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/poten\_codeMeow.png)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner8.png)

#### 加載Robotbit插件

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addRB2.png)

**讀取土壤濕度數值編程**

![](https://kittenbothk.readthedocs.io/en/latest/\_images/poten\_codekb.png)

### Mu Editor編程教學

#### 讀取土壤濕度數值編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/poten\_codemu.png)
