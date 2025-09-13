# KOI 2在KittenBlock編程快速入門

## <mark style="color:orange;">**接線方法**</mark>

### **1. 與Robotbit EDU 組合使用**

使用隨盒附送的4pin 線, 白色大插頭插入KOI 中

Robotbit Edu上已經提供了4pin的通訊連供電接口，我們只需要將KOI連接到通訊接口(如下圖)就可以了。

由於Robotbit Edu的通訊接口使用了P2與P12，我們在MakeCode裡面就要相應地選擇引腳。

<mark style="background-color:yellow;">注:  如欲為KOI 2以USB 方式額外供電, 請拔走黑 (GND) 及 紅(5V) 2跟線。</mark>

<figure><img src="../../../.gitbook/assets/koi2_robotbit_edu_wiring.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
KOI的RX接口(黃色線)接到Robotbit的TX接口(P2)。

KOI的TX接口(藍色線)接到Robotbit的RX接口(P12)。
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### **2. 與Robotbit 2.2  組合使用**

使用隨盒附送的4pin 線, 白色大插頭插入KOI 中

另一端參考下方接線圖

&#x20;           黑 - GND

&#x20;           紅 - 5V

&#x20;           黃 - P2 (TX)

&#x20;           藍 - P12 (RX)

但用家<mark style="background-color:orange;">必須</mark><mark style="background-color:orange;">**注意**</mark>, 在接駁4條杜邦線時, 要格外留意**5V** 及**GND** 的插線,

## <mark style="color:red;">**xxx 切勿反接 xxx**</mark>

否則KOI 2有機會不能再運作了 >.<



```
黃色線只可以接類比引腳（Pin0-2）！使用Pin0的話請拔除蜂鳴器跳線帽。
```

<figure><img src="../../../.gitbook/assets/koi2_robotbit_2.2_wiring.png" alt=""><figcaption></figcaption></figure>

**重要事項: 黑 (GND) 及 紅(5V) 切勿反接!!!**

再&#x6B21;_&#x6AA2;查接線無誤_ 後, 就可以打開Robitbit 的開關, 便會看到KOI 的屏幕顯示鏡頭畫面。

<figure><img src="../../../.gitbook/assets/20240320_100258.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/20240320_100319.jpg" alt=""><figcaption></figcaption></figure>

### Kittenblock編程快速開始

在瀏覽器打開KittenBlock在線版。

{% embed url="https://kblock.kittenbot.cn/" %}

選擇未來板/未來板Lite。

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

連接未來板到Kittenblock。

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252FX0XzHETbS3L7bJDbYX8Y%252Fimage.png%3Falt%3Dmedia%26token%3Db8de9fd3-651c-407e-87c8-7fcb2bf8fc41&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=c9389bdd&#x26;sv=1" alt=""><figcaption></figcaption></figure>

<figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252F1LATCGLzqlXkurZaLVs6%252Fimage.png%3Falt%3Dmedia%26token%3D5be68715-ef55-4e4b-8002-efbfd4de6928&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=bf0660a4&#x26;sv=1" alt=""><figcaption></figcaption></figure>

<figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252Fz7mxlbjcq0fX4bCixoMK%252Fimage.png%3Falt%3Dmedia%26token%3D49076379-410b-473e-809d-696b0842bf3f&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=66860a28&#x26;sv=1" alt=""><figcaption></figcaption></figure>

Open Coding Mode to Uploadthe program onto your Futureboard.

<figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252Fzr0BV175aTPRboB9vxGC%252Fimage.png%3Falt%3Dmedia%26token%3D44bc6251-8d69-485d-8bb9-71aec444c60f&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=70de9fdf&#x26;sv=1" alt=""><figcaption></figcaption></figure>
