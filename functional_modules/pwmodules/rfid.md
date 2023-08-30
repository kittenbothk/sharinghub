---
description: RFID探測魔塊 (HKBM8012L) + RFID卡片 (HKBM8012M)
---

# RFID探測魔塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/10\_04.png)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/10\_05.png)

這是一個RFID探測魔塊，可以對套件附有的RFID卡或者空白RFID卡進行讀寫。

附有的RFID卡有1K內存，有16個分區，每個分區有3個區塊可以寫入資料。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/IMG\_2583.GIF)

### 詳細介紹

![](https://kittenbothk.readthedocs.io/en/latest/\_images/10\_03.png)

### 產品參數

* 支援電壓：3V-5V
* 尺寸：56mm X 56mm X 16mm
* 接口：4pin防反插接口
* 感應距離：大約3cm

### 使用注意事項

* RFID請勿在有強力磁場的環境下使用
* RFID卡與魔塊之間不能有金屬阻擋，否則無法進行讀寫。
* RFID卡寫入大量數據的速度比較慢，請靜待一下，等數據成功寫入再拿去RFID卡。
* 八達通卡身份證之類的卡因為資料被加密所以不能進行寫入數據，只可以讀取UID號碼（每張卡也有獨有的ID）。

### 接線方法

#### Armourbit

將RFID探測魔塊用4pin排線連接至Armourbit的I2C接口。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rfid\_wire.png)

#### Robotbit

將RFID探測魔塊連接至Robotbit的I2C接口。

```
藍色線（A）請接到SCL，綠色線（B）請接到SDA。
```

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rfid\_wire1.png)

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner13.png)

#### 加載PowerBrick插件：

#### 在擴展頁直接搜尋powerbrick (PowerBrick已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/powerbrick\_search.png)

#### 你亦可以用插件地址搜尋

PowerBrick插件地址：https://github.com/KittenBot/pxt-powerbrick

#### [詳細方法](../../programmingplatforms/makecode/kittenbotandmakecode.md)

#### RFID探測魔塊積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rfidblocks.png)

#### RFID卡片寫入

{% embed url="https://makecode.microbit.org/_XdP0Pye1rFA0" %}

[參考程式網址](https://makecode.microbit.org/\_XdP0Pye1rFA0)

#### RFID卡片讀取

{% embed url="https://makecode.microbit.org/_TEz6D45qgDaa" %}

[參考程式網址](https://makecode.microbit.org/\_TEz6D45qgDaa)

#### RFID讀取UUID

每張卡的UUID也不同，請自行抄下你自己卡片的UUID。

{% embed url="https://makecode.microbit.org/_a6wiKdUqWaXL" %}

[參考程式網址](https://makecode.microbit.org/\_a6wiKdUqWaXL)

#### UUID身份辨別

我們可以用UUID作身份辨別。

{% embed url="https://makecode.microbit.org/_c4rcrE76Tc6Y" %}

```
這裡請使用您卡片的UUID。
```

[參考程式網址](https://makecode.microbit.org/\_c4rcrE76Tc6Y)

### 插件版本與更新

插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。

詳情請參考: [Makecode插件版本更換](../../programmingplatforms/makecode/makecodeextupdate.md)

#### Makecode教學短片

{% embed url="https://www.youtube.com/watch?v=r1B6l7xK7So" %}

#### 示範短片

{% embed url="https://www.youtube.com/watch?v=oR1FwHu4lrM" %}

### KittenBlock編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbbanner7.png)

#### 加載PowerBrick插件

在左上角小貓logo旁邊的硬件欄選擇PowerBrick，加載Microbit與Powerbrick插件。

![](https://kittenbothk.readthedocs.io/en/latest/\_images/addextension1.png)

#### RFID積木塊

![](https://kittenbothk.readthedocs.io/en/latest/\_images/kbrfidblocks.png)

#### RFID卡片寫入

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rfidwrite1.png)

[參考程式下載](https://bit.ly/PowerbrickM8\_01sb3)

#### RFID卡片讀取

![](https://kittenbothk.readthedocs.io/en/latest/\_images/rfidread1.png)

[參考程式下載](https://bit.ly/PowerbrickM8\_02sb3)

#### RFID讀取UUID

![](https://kittenbothk.readthedocs.io/en/latest/\_images/uidread1.png)

[參考程式下載](https://bit.ly/PowerbrickM8\_03sb3)

#### UUID身份辨別

![](https://kittenbothk.readthedocs.io/en/latest/\_images/uididentify1.png)

```
這裡請使用您卡片的UUID。
```

[參考程式下載](https://bit.ly/PowerbrickM8\_04sb3)

### FAQ

1：為什麼我點擊積木塊沒有反應呢？

首先確保已經連接好Microbit，然後上載韌體再試一試。
