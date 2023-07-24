# 未來板與ThingSpeak編程快速入門

ThingSpeak作為免費的IoT平台，的確是方便大家可以實現IoT應用，不過ThingSpeak的設定可能比較繁複，對初學者來說可能比較麻煩，故此KittenBot特地為大家提供一個從0開始的教學，讓大家都可以輕易使用ThingSpeak實現IoT。

### ThingSpeak帳號申請

請大家首先按照以下教學，申請一個免費的ThingSpeak帳號。

[ThingSpeak 平台介紹](../iotplatform/thingspeak.md)

### ThingSpeak平台設置

申請帳號之後，我們還未可以開始編程，因為我們要先在ThingSpeak設置好平台。

#### 建立新頻道

在My Channel的頁面建立新頻道。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/127.png)

除了頻道名稱之外其他可以不用理會。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/29.png)

完成之後就可以按Save Channel。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/39.png)

進入Sharing。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/411.png)

最方便和簡單地使用ThingSpeak的方法是將頻道設為公開，所以我們選擇第二個選項。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/59.png)

當你看到Access由Private變為Public就代表頻道完成了。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/66.png)

#### 添加新裝置

然後請前往Devices，選擇MQTT。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/76.png)

添加一個新裝置。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/85.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/94.png)

選擇剛才建立的頻道，點擊Add Channel。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/106.png)

最後就可以點擊Add Device。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/1111.png)

添加裝置後，這一個頁面非常重要！這些是大家的未來板用來連接ThingSpeak的登入資料，請大家自行記下，或者下載登入資料，儲存在電腦。

![../../\_images/128.png](https://kittenbothk.readthedocs.io/en/latest/\_images/128.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/136.png)

### KittenBlock編程

對初學者而言，使用KittenBlock編程是最簡單的。

#### 連接ThingSpeak

搭建出以下程式，將未來板連接上網絡，然後連接到ThingSpeak的伺服器。

* 伺服器網址: mqtt3.thingspeak.com
* ID: 按照ThingSpeak裝置的ID
* 用戶名: 按照ThingSpeak裝置的username
* 密碼: 按照ThingSpeak裝置的Password

![](https://kittenbothk.readthedocs.io/en/latest/\_images/144.png)

#### 發佈到ThingSpeak頻道

在發佈上ThingSpeak頻道之前，我們需要先查看頻道的ID。 頻道ID是一個7位的數字。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/153.png)

搭建出以下程式，按下A鍵發布信息20到ThingSpeak頻道。

* MQTT主題: channels/\[頻道ID]/publish
* 信息: field\[欄位號碼]=\[數字信息]

![](https://kittenbothk.readthedocs.io/en/latest/\_images/162.png)

發佈成功的話，在ThingSpeak的頁面上會看到剛才發布的信息。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/174.png)

#### 讀取ThingSpeak頻道信息

使用頻道ID訂閱頻道之後，就可以收取到頻道的訊息。

按A鍵發布信息到頻道，未來板收到訊息之後會顯示出來。

* MQTT主題: channels/\[頻道ID]/subscribe/fields/field\[欄位號碼]

![](https://kittenbothk.readthedocs.io/en/latest/\_images/183.png)
