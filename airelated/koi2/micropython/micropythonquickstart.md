# KOI 2在MicroPython編程快速入門

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

<figure><img src="../../../.gitbook/assets/image (6) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

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

### MicroPython編程快速開始

Open KittenCode in browser.

{% embed url="https://codebeta.kittenbot.net/home" %}

建立新專案。(未來板/未來板Lite)

<figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252FjuMzmvTbEtaUvm2fXXkb%252Fimage.png%3Falt%3Dmedia%26token%3D087fb641-6f79-4b01-bec7-9bd101894bf8&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=a702aeb7&#x26;sv=1" alt=""><figcaption></figcaption></figure>

將未來板連接到KittenCode。

<div><figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252Fh73ckaGfH9QqZzd2QkNE%252Fimage.png%3Falt%3Dmedia%26token%3D373a864c-9907-46be-9385-9e992bb796e5&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=7b9cba5&#x26;sv=1" alt=""><figcaption></figcaption></figure> <figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252FvoRHKJKPsKlqWC87hf5f%252Fimage.png%3Falt%3Dmedia%26token%3Daeb4eabb-2f09-40ac-b2a6-bd222f9d91f7&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=8f7ced9d&#x26;sv=1" alt=""><figcaption></figcaption></figure> <figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252FjvEtQ3L5p6xxc8m4jdup%252Fimage.png%3Falt%3Dmedia%26token%3D4f6157d2-db1c-4edd-8ce8-7cffd06a9c85&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=71471968&#x26;sv=1" alt=""><figcaption></figcaption></figure></div>

按運行程式就可以在線運行程式或按上傳程式將程式上傳到未來板。

<figure><img src="https://sharinghub-eng.kittenbot.hk/~gitbook/image?url=https%3A%2F%2F686851495-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F7Bv9xBdKh3R9w6Vp7asd%252Fuploads%252FnHm7r8SgIGG5S1tuY6dh%252Fimage.png%3Falt%3Dmedia%26token%3Dee25b307-5a2d-4545-978c-8d77549d4318&#x26;width=768&#x26;dpr=1&#x26;quality=100&#x26;sign=bc1fad6f&#x26;sv=1" alt=""><figcaption></figcaption></figure>
