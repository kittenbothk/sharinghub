# IoT物聯網

### WiFi須知

### 注意！KOI 2只能連接2.4GHz的網絡，請確保WiFi熱點支援2.4GHz的網絡。

### MakeCode編程

在MakeCode打開專案，點擊擴展一頁。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/16-1.png" alt=""><figcaption></figcaption></figure>

在搜尋欄輸入koi 2。

<figure><img src="../../../.gitbook/assets/koi2_ext.gif" alt=""><figcaption></figcaption></figure>

加載成功後，積木欄會新增koi2的積木。

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 編程積木

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FPTCn8iBkL2mRlll9o3sm%2Fimage.png?alt=media&#x26;token=d0f50193-99e4-4f16-8ea9-28322d35ccd6" alt=""><figcaption></figcaption></figure>

### 參考程式

### 連接WiFi網絡

{% hint style="info" %}
KOI 2需要使用2.4GHz的WiFi網絡，請注意。
{% endhint %}

{% hint style="info" %}
Armourbit用家請使用初始化Armourbit積木。
{% endhint %}

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6uJvpXC43onNIIwhMlWo%2Fuploads%2FPGyECwlPd2M3JqUBLDfO%2Fimage.png?alt=media&#x26;token=662ace3f-a8eb-4fbf-8a10-1d9643c88b1e" alt=""><figcaption></figcaption></figure>

{% embed url="https://makecode.microbit.org/_cEy78WKd6XVR" %}

[參考程式](https://makecode.microbit.org/_cEy78WKd6XVR)

#### 程式解說

1. 按A鍵連接WiFi。
2. 按B鍵顯示KOI的IP地址。

{% hint style="info" %}
在連接MQTT平台之前，請確保KOI 2能夠成功連接WiFi網絡並可以獲取IP地址。

假如KOI 2未能成功連線，KOI 2會顯示0.0.0.0。
{% endhint %}

<div><figure><img src="../../../.gitbook/assets/no_internet.png" alt=""><figcaption><p>未能連接Wifi網絡</p></figcaption></figure> <figure><img src="../../../.gitbook/assets/internet.png" alt=""><figcaption><p>成功連接WiFi網絡</p></figcaption></figure></div>

### 連接MQTT與收發信息

{% hint style="info" %}
Armourbit用家請使用初始化Armourbit積木。
{% endhint %}

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6uJvpXC43onNIIwhMlWo%2Fuploads%2FPGyECwlPd2M3JqUBLDfO%2Fimage.png?alt=media&#x26;token=662ace3f-a8eb-4fbf-8a10-1d9643c88b1e" alt=""><figcaption></figcaption></figure>

{% embed url="https://makecode.microbit.org/_CgYhzEgsX22E" %}

[參考程式](https://makecode.microbit.org/_CgYhzEgsX22E)

#### 程式解說

1. 按A鍵連接WiFi與MQTT平台。
2. 按B鍵向MQTT平台發送訊息。
3. Micro:bit會顯示MQTT平台收到的訊息。

### MakerCloud創客雲 參考程式

{% embed url="https://makecode.microbit.org/_DovYtzcEhbfk" %}

[參考程式](https://makecode.microbit.org/_DovYtzcEhbfk)

發送訊息的積木必須按照以下格式填寫，請將主題名稱填進話題，並且將話題的數據類型識別碼取代數據類型。

<figure><img src="../../../.gitbook/assets/path1361.png" alt=""><figcaption></figcaption></figure>
