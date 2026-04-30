# KOI 2 x Teachable Machine 模型訓練方法

KOI 2已經新增支援Teachable Machine圖像分類模型的功能，有興趣的用家可以參考以下教程。

## 示範短片

{% embed url="https://youtu.be/f_h8oTreSnc" %}

## 詳細玩法教學

### 1. 更新KOI 2固件

首先確認KOI 2的固件版本，固件版本必須為4.2.0或以上。

如何檢查固件版本或更新的詳情可以參考：

{% content-ref url="../koi-koi-1-2-gu-jian-sheng-ji/" %}
[koi-koi-1-2-gu-jian-sheng-ji](../koi-koi-1-2-gu-jian-sheng-ji/)
{% endcontent-ref %}

### 2. 在Kittenblock完成圖像分類模型訓練

前往Kittenblock.

[https://kblock.kittenbot.cc/](https://kblock.kittenbot.cc/)

打開插件頁，加入機器學習插件。

{% content-ref url="../../../programmingplatforms/kittenblock/online/" %}
[online](../../../programmingplatforms/kittenblock/online/)
{% endcontent-ref %}

<figure><img src="../../../.gitbook/assets/image (250).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (252).png" alt=""><figcaption></figcaption></figure>

打開訓練工具，選擇圖像分類

<figure><img src="../../../.gitbook/assets/image (253).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (254).png" alt=""><figcaption></figcaption></figure>

選擇嵌入式圖片模型

<figure><img src="../../../.gitbook/assets/image (255).png" alt=""><figcaption></figcaption></figure>

可以使用webcam、上傳圖片或KOI 2作為圖像數據來源。

由於使用Webcam和上傳圖片和基本的圖像分類教學重疊，以下會集中以KOI2作為數據來源作範例。

使用Webcam和上傳圖片的教學請參考:

{% content-ref url="../../../programmingplatforms/kittenblock/online/aifunctions/ml.md" %}
[ml.md](../../../programmingplatforms/kittenblock/online/aifunctions/ml.md)
{% endcontent-ref %}

首先將KOI2用USB線連接至電腦按『裝置』

<figure><img src="../../../.gitbook/assets/image (256).png" alt=""><figcaption></figcaption></figure>

按連接裝置

<figure><img src="../../../.gitbook/assets/image (257).png" alt=""><figcaption></figcaption></figure>



在彈出式清單中選擇JTAG Serial Debug Unit

{% hint style="info" %}
注意: COM的數字不一定一樣
{% endhint %}

<figure><img src="../../../.gitbook/assets/Screenshot 2026-04-15 125050.png" alt=""><figcaption></figcaption></figure>

成功的話，KOI 2會顯示"Camera Mode"，然後頁面會顯示KOI的鏡頭畫面。

此時就可以使用KOI作為數據來源，錄入圖片數據。

<figure><img src="../../../.gitbook/assets/image (258).png" alt=""><figcaption></figcaption></figure>

### 3. 錄入數據及訓練模型

錄入數據及訓練模型的教學已經詳細寫在以下篇章，本篇章將會略過。

{% content-ref url="../../../programmingplatforms/kittenblock/online/aifunctions/ml.md" %}
[ml.md](../../../programmingplatforms/kittenblock/online/aifunctions/ml.md)
{% endcontent-ref %}

### 4. 將模型上傳到KOI 2

訓練好模型後按下載模型

<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

下載時可以選擇匯出模型或直接上傳到KOI2

匯出模型：模型需要放在SD卡，好處是可以儲存多個模型檔案，壞處是必須使用SD卡(Class10 或以上)

上傳到設備：模型會直接輸送到KOI內部，好處是比較方便，編程時不用指定載入模型名稱，壞處是同時間只能夠儲存一個模型

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 匯出模型

下載kmodel模型後，將kmodel檔案放在SD卡上然後將SD卡插入KOI即可

<figure><img src="../../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 上傳到設備

{% hint style="info" %}
上傳前可能需要拔除KOI再連接電腦
{% endhint %}

按上傳到設備，模型就會直接傳輸到KOI

在傳輸過程中切勿拔除KOI

<figure><img src="../../../.gitbook/assets/image (261).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

等待模型傳輸完成後就可以拔除KOI

<figure><img src="../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

## 編程教學

此功能暫時可以在Microbit和Lite AI上使用，編程教學可以參考以下頁面:

### Micro:bit 編程教學

{% content-ref url="koi2-x-teachable-machine-microbit-bian-cheng-jiao-xue.md" %}
[koi2-x-teachable-machine-microbit-bian-cheng-jiao-xue.md](koi2-x-teachable-machine-microbit-bian-cheng-jiao-xue.md)
{% endcontent-ref %}

### Futureboard Lite AI 編程教學

{% content-ref url="koi2-x-teachable-machine-lite-ai-bian-cheng-jiao-xue.md" %}
[koi2-x-teachable-machine-lite-ai-bian-cheng-jiao-xue.md](koi2-x-teachable-machine-lite-ai-bian-cheng-jiao-xue.md)
{% endcontent-ref %}
