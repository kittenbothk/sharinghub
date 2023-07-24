# 紅外線感應模組

![](https://kittenbothk.readthedocs.io/en/latest/\_images/infrared1.png)

這是一隻紅外線感應模組，它可以檢測黑線，它返回的數值是類比形式。

數值範圍由0-1023，數值越大代表越黑。

### 產品參數

* 工作電壓：3.3V\~5V
* 類型：類比模組
* 接口：3Pin杜邦線
* 檢測距離：10-60mm

### 接線教學

```
紅外線避障感應器是類比輸入類模組，只可使用P1、P8、P13、P14這4個引腳。
```

將紅外線感應模組連接到Robotbit的針線和3V接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/infrared\_wire.png)

### 調較靈敏度

感應的靈敏度可以透過電位器調較，請使用螺絲批轉動電位器。(向左調高，向右調低)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/infrared2.png)

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner14.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/acbanner1.png)

#### 此模組可供Microbit和Meowbit使用。

**讀取紅外線數值編程**

#### Microbit:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/poten\_code.png)

#### Meowbit:

![](https://kittenbothk.readthedocs.io/en/latest/\_images/poten\_codeMeow.png)

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner8.png)

#### 加載Robotbit插件

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addRB2.png)

**讀取紅外線數值編程**

![](https://kittenbothk.readthedocs.io/en/latest/\_images/poten\_codekb.png)

### Mu Editor編程教學

#### 讀取紅外線數值編程

![](https://kittenbothk.readthedocs.io/en/latest/\_images/poten\_codemu.png)
