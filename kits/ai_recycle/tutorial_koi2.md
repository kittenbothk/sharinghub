# AI/AIoT 智能回收箱套件教學(KOI 2)

### 資源下載

[音效檔下載](https://drive.google.com/file/d/1GEJpytMGa4GYDSfpvDlvfwSC0fG-qENg/view?usp=sharing)

[參考圖檔下載](https://drive.google.com/drive/folders/1l27lVZQ-IEcx-_u2yh-VkV3N75coOGbE?usp=sharing)

![](https://kittenbothk.readthedocs.io/en/latest/_images/a4.png)

### 模型訓練參考程式

{% embed url="https://makecode.microbit.org/_4c99hoUu71bC" %}

[Armourbit版參考程式](https://makecode.microbit.org/_9cYWWg5kwJ2C)

[Robotbit版參考程式](https://makecode.microbit.org/_4c99hoUu71bC)

#### 訓練方法

1. Micro:bit會顯示目前的分類。
2. 按A對現時分類進行訓練。
3. 按B跳到下一個分類。
4. 按A+B儲存模型。

### AI智能回收箱參考程式

{% hint style="info" %}
KOI 2播放聲音檔案需要 class10 或以上的micro SD卡才可以播放。
{% endhint %}

{% embed url="https://makecode.microbit.org/_63ei2YUhoVzg" %}

[Armourbit版參考程式](https://makecode.microbit.org/_A465ksKCq4ia)

[Robotbit版參考程式](https://makecode.microbit.org/_63ei2YUhoVzg)

#### 辨認方法

1. 按A啟動辨認功能。
2. KOI會說出辨認到的垃圾類別，然後打開相應的回收箱。

### AIOT智能回收箱參考程式

### Kzone平台

{% embed url="https://makecode.microbit.org/_Wjd8xJW2x0EH" %}

[Robotbit版參考程式](https://makecode.microbit.org/_Wjd8xJW2x0EH)

#### 辨認方法

1. 按A啟動辨認功能。
2. KOI會說出辨認到的垃圾類別，然後打開相應的回收箱。

#### Kzone平台設定教學

首先前往Kzone建立免費帳號。

{% content-ref url="../../wifibrick_iot/wifibrick_makecode/koi_tutor/koi_kzone.md" %}
[koi\_kzone.md](../../wifibrick_iot/wifibrick_makecode/koi_tutor/koi_kzone.md)
{% endcontent-ref %}

建立3個MQTT話題：can, paper, bottle

<figure><img src="../../.gitbook/assets/image (362).png" alt=""><figcaption></figcaption></figure>

在參考程式填入MQTT話題。

<figure><img src="../../.gitbook/assets/image (363).png" alt=""><figcaption></figcaption></figure>

填入WiFi登入資料。

<figure><img src="../../.gitbook/assets/image (364).png" alt=""><figcaption></figcaption></figure>

#### 程式使用教學

1. 將程式下載到Microbit再打開Robotbit電源。
2. 等待Micro:bit顯示剔號圖案，程式就會進入辨認模式。
3. 辨認到can, bottle, paper這3種分類後舵機就會打開垃圾桶蓋。
4. IoT平台亦會即時更新3種分類的辨認數量。

<figure><img src="../../.gitbook/assets/image (365).png" alt=""><figcaption></figcaption></figure>
