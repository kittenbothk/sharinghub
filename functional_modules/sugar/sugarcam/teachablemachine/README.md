# Sugar Cam使用教學: AI模式(進階)

Sugar Cam亦都支援Teachable Machine驅動的AI圖像辨識功能，請參考以下介紹。

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Teachable Machine功能示範短片

{% embed url="https://www.youtube.com/watch?v=83YG8dMGKSw" %}

### 刷入Teachable Machine專用固件

首先下載固件更新程式與固件檔案。

{% hint style="info" %}
進行固件更新會清除原有檔案，有需要的話請保留文件。

更新固件後可逆轉為普通模式，不會永遠只停留在AI模式。
{% endhint %}

{% file src="../../../../.gitbook/assets/Klink_qt_win_aug3.zip" %}

將Sugar Cam連接到電腦。然後按一下Reset，再按一下A鍵，此時Sugar Cam會亮一下紅燈，然後電腦出現UF2\_Sugar的硬碟。

<div data-full-width="false"><figure><img src="../../../../.gitbook/assets/VideoToGif_08-11-2023-11-27.gif" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/image (6) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure></div>

打開資料夾裡的Klink.exe。

<figure><img src="../../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

選擇Modules\&Applications。然後選擇Teachable Machine的Load Plugin。

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

選擇Firmware的一欄然後按Update Firmware。

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

下載Teachable Machine小程式。

{% file src="../../../../.gitbook/assets/KittenBot_Teachable Machine.zip" %}

打開serial\_ws.exe。

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1).png" alt=""><figcaption></figcaption></figure>

點擊Connect，成功的話介面會出現Sugar Cam的畫面。

<div><figure><img src="../../../../.gitbook/assets/image (10) (1) (1).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/image (11) (1).png" alt=""><figcaption></figcaption></figure></div>

### 切換到普通模式

假如想將Sugar Cam切換到普通模式，只需按先前步驟連接Sugar Cam。

然後在固件刷新程式選擇Sugar Cam並Load Plugin，再按Update Firmware即可。

{% hint style="info" %}
注意：切換回到普通模式後，Teachable Machine模型也會一併清除。
{% endhint %}

<figure><img src="../../../../.gitbook/assets/Screenshot 2023-08-11 123415.png" alt=""><figcaption></figcaption></figure>

完成後就可以按照更新固件的方法刷入最新固件。

{% content-ref url="../" %}
[..](../)
{% endcontent-ref %}
