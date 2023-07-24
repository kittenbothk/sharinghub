# AI/AIoT 智能回收箱套件教學

## AI/AIoT 智能回收箱套件教學

### 資源下載

[音效檔下載](https://drive.google.com/file/d/1GEJpytMGa4GYDSfpvDlvfwSC0fG-qENg/view?usp=sharing)

[參考圖檔下載](https://drive.google.com/drive/folders/1l27lVZQ-IEcx-\_u2yh-VkV3N75coOGbE?usp=sharing)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/a4.png)

### 模型訓練參考程式

![](https://kittenbothk.readthedocs.io/en/latest/\_images/train\_code.png)

[Armourbit版參考程式](https://makecode.microbit.org/\_JrW0YiUai2r8)

[Robotbit版參考程式](https://makecode.microbit.org/\_Ew7AEaDzw78e)

#### 訓練方法

1. Micro:bit會顯示目前的分類。
2. 按A對現時分類進行訓練。
3. 按B跳到下一個分類。
4. 按A+B儲存模型。

### AI智能回收箱參考程式

![](https://kittenbothk.readthedocs.io/en/latest/\_images/offline\_code.png)

[Armourbit版參考程式](https://makecode.microbit.org/\_PY2KHcH7WHUg)

[Robotbit版參考程式](https://makecode.microbit.org/\_Kmi7b1JKW3sW)

#### 辨認方法

1. 按A啟動辨認功能。
2. KOI會說出辨認到的垃圾類別，然後打開相應的回收箱。

### AIoT智能回收箱參考程式

### MakerCloud平台版本

![](https://kittenbothk.readthedocs.io/en/latest/\_images/online\_code.png)

[Armourbit版參考程式](https://makecode.microbit.org/\_9M9VDt2xMPpi)

[Robotbit版參考程式](https://makecode.microbit.org/\_f6YdEkFRqWkF)

#### 辨認方法

1. 按A啟動辨認功能。
2. 按B確認KOI已成功連接網絡，並連接MakerCloud平台。
3. KOI會說出辨認到的垃圾類別，然後打開相應的回收箱。

#### MakerCloud平台設定教學

建立MakerCloud主題，並建立3個數據類型paper、can、bottle。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/makercloud1.png)

為每個數據類型建立圖表。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/makercloud2.png)

建立儀表板，將建立的3個圖表添加到裡面。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/makercloud3.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/makercloud4.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/makercloud5.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/makercloud6.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/makercloud7.png)

### ObjectBlocks平台版本

![](https://kittenbothk.readthedocs.io/en/latest/\_images/objectblock\_code.png)

[Armourbit版參考程式](https://makecode.microbit.org/\_cVo50M4YRWRP)

[Robotbit版參考程式](https://makecode.microbit.org/\_LD78gk4K7iud)

#### 辨認方法

1. 按A啟動辨認功能。
2. 按B確認KOI已成功連接網絡，並連接ObjectBlocks平台。
3. KOI會說出辨認到的垃圾類別，然後打開相應的回收箱。

#### ObjectBlocks平台設定

建立ObjectBlocks平台話題。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/objectblocks1.png)

建立3個渠道Paper、Plastic、Can。(必須剔選webhook選項)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/objectblocks2.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/objectblocks3.png)

建立儀表板。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/objectblocks4.png)

新增工具顯示渠道信息。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/objectblocks5.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/objectblocks6.png)

### ThingSpeak平台版本

![](https://kittenbothk.readthedocs.io/en/latest/\_images/thingspeak\_code.png)

[Armourbit版參考程式](https://makecode.microbit.org/\_f8eHEHJaT8MV)

[Robotbit版參考程式](https://makecode.microbit.org/\_Lo5grsEu8HeX)

#### 辨認方法

1. 按A啟動辨認功能。
2. 按B確認KOI已成功連接網絡，並連接ThingSpeak平台。
3. KOI會說出辨認到的垃圾類別，然後打開相應的回收箱。

#### ThingSpeak平台設定

設立新ThingSpeak頻道。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/thingspeak1.png)

將頻道設為公開。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/thingspeak2.png)

添加MQTT裝置存取話題訊息。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/thingspeak3.png)

在程式裡填入登入資料。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/thingspeak4.png)
