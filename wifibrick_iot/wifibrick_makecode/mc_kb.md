# Makecode 編程與Kittenblock內置IoT平台

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner8.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner5.png)

### 硬件準備

在編程前請確保硬件及接線沒有問題。

[硬件接線方法](../wifibrick/wifibrick\_intro.md)

### 前言：

在這節教程，我們將會學習使用WifiBrick和KOI與Kittenblock的程式溝通。

### 安裝KittenBlock

[下載KittenBlock](../../programmingplatforms/kittenblock/kttenblockgreen.md)

### 第一步：平台準備

#### 注意：電腦需要與Wifibrick/KOI連接在同一個網絡上。

啟動本地伺服器。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb43.png)

### 第二步：編寫程式

接下來我們會在Kittenblock編寫簡單的數據接收與發佈程式。

```
這個平台不只是容許與Kittenblock程式溝通的，這裡只是用作示範。

例如：如果你有多隻Wifibrick，只要你的Wifibrick都連接到同一個網絡，所有Wifibrick都可以連接到同一個本地內聯網伺服器。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb13.png)

首先加載IoT插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb52.png)

組合出以下程式，你本地伺服器的IP地址會自動填入。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb61.png)

#### 使用Wifibrick

打開MakeCode。

#### 加載Kittenbot插件：

#### 在擴展頁直接搜尋Kittenbot (Kittenbot已經過微軟認證，可以直接搜尋)

#### 選擇KittenWiFi和Powerbrick或Robotbit

![](https://kittenbothk.readthedocs.io/en/latest/\_images/wifi\_search.png)

```
  請按自己的硬件選擇Powerbrick或Robotbit插件。
```

組合出以下程式，填入你本地伺服器的IP地址和Wifi密碼。

我們在程式中廣播的話題需要與Kittenblock裏的話題一樣。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb71.png)

等待Wifibrick成功連接，然後按一下A，Kittenblock裏的小貓就會說出Micro:bit所探測到的環境亮度。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb81.png)

接下來我們稍微修改一下程式，在Kittenblock中發佈數據。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb9.png)

同樣地，在MakeCode中修改程式，使Wifibrick也能讀取IoT平台的數據。

我們在程式中訂閱的話題需要與Kittenblock裏的話題一樣。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb10.png)

現在大家可以在Kittenblock控制Micro:bit所顯示的圖案了。

[MakeCode參考程式網址](https://makecode.microbit.org/\_bi118xfRj5im)

#### 使用KOI

打開MakeCode。

#### 加載Kittenbot插件：

#### 在擴展頁直接搜尋Kittenbot (Kittenbot已經過微軟認證，可以直接搜尋)

#### 選擇KOI和Powerbrick或Robotbit

![](https://kittenbothk.readthedocs.io/en/latest/\_images/wifi\_search.png)

```
  請按自己的硬件選擇Powerbrick或Robotbit插件。
```

KOI的使用方法和WifiBrick類似，分別在於KOI不會自動讀取數據，需要我們運行MQTT讀取的積木才會讀取到數據。

組合出以下程式，填入你本地伺服器的IP地址和Wifi密碼。

我們在程式中廣播/訂閱的話題需要與Kittenblock裏的話題一樣。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kb111.png)

[MakeCode參考程式網址](https://makecode.microbit.org/\_3VA7DbDhj254)
