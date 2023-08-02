# Sugar Cam功能示範: MP3播放

智能FPV鏡頭的出廠就已經是設定為指令模式。主要的功能，包括WiFi圖傳，二維碼掃碼，拍照等都是在這個模式裡進行。

### 接線教學

<figure><img src="../../../../.gitbook/assets/cam_edu_wire.png" alt="" width="563"><figcaption></figcaption></figure>

### MakeCode編程教學

![](https://kittenbothk.readthedocs.io/en/latest/\_images/mcbanner15.png)

#### 加載Sugar插件：

#### 在擴展頁直接搜尋sugar (sugar已經過微軟認證，可以直接搜尋)

![](https://kittenbothk.readthedocs.io/en/latest/\_images/sugar\_search.gif)

#### 你亦可以用插件地址搜尋

Sugar插件：https://github.com/KittenBot/pxt-sugar

#### [詳細方法](../../../../ge-bian-cheng-ping-tai-jie-shao/makecode/kittenbotandmakecode.md)

### 二維碼掃描

```
由於鏡頭沒有屏幕，所以掃描時可能需要多試幾次才能對焦清楚
```

{% embed url="https://makecode.microbit.org/_hgw6hb2wcMqz" %}

[參考程式](https://makecode.microbit.org/\_hgw6hb2wcMqz)

### 語音辨識

{% embed url="https://makecode.microbit.org/_bA7UEc9Aad9k" %}

[參考程式](https://makecode.microbit.org/\_bA7UEc9Aad9k)

### 拍照與播放mp3

{% embed url="https://makecode.microbit.org/_Hsj08VMRFgFz" %}

### 未來板KittenBlock編程教學

加載Sugar Cam插件。

<div>

<figure><img src="../../../../.gitbook/assets/cam_kb1.png" alt=""><figcaption></figcaption></figure>

 

<figure><img src="../../../../.gitbook/assets/cam_kb2.png" alt=""><figcaption></figcaption></figure>

</div>

<figure><img src="../../../../.gitbook/assets/cam_kb3.png" alt=""><figcaption></figcaption></figure>

### 未來板圖傳

編寫程式令未來板連上WiFi，並將Sugar Cam的IP和密鑰(在config.json中修改)填入以下程式。

<div>

<figure><img src="../../../../.gitbook/assets/cam_kb4 (1).png" alt=""><figcaption></figcaption></figure>

 

<figure><img src="../../../../.gitbook/assets/cam_kb5.png" alt=""><figcaption></figcaption></figure>

</div>

分別為未來板和Sugar Cam供電。

<div>

<figure><img src="../../../../.gitbook/assets/cam_kb6.png" alt=""><figcaption></figcaption></figure>

 

<figure><img src="../../../../.gitbook/assets/cam_kb7.png" alt=""><figcaption></figcaption></figure>

</div>

Sugar Cam的影像就會在未來板上顯示出來。

<div>

<figure><img src="../../../../.gitbook/assets/cam_kb8.jpg" alt=""><figcaption></figcaption></figure>

 

<figure><img src="../../../../.gitbook/assets/cam_kb9.jpg" alt=""><figcaption></figcaption></figure>

</div>

### 在Kittenblock中使用編程教學

首先在KittenBlock中加載Sugar Cam插件。

<figure><img src="../../../../.gitbook/assets/cam_ai1.png" alt=""><figcaption></figcaption></figure>

填入模組的IP地址，點擊積木，舞台就會出現模組畫面。

<div>

<figure><img src="../../../../.gitbook/assets/cam_kb4.png" alt=""><figcaption></figcaption></figure>

 

<figure><img src="../../../../.gitbook/assets/cam_ai2.png" alt=""><figcaption></figcaption></figure>

</div>

成功在Kittenblock顯示模組的畫面後就可以加載其他AI類插件使用。

有關KittenBlock內置AI插件的教學請參考以下篇章:

{% content-ref url="../../../../ge-bian-cheng-ping-tai-jie-shao/kittenblock/features/extensions/" %}
[extensions](../../../../ge-bian-cheng-ping-tai-jie-shao/kittenblock/features/extensions/)
{% endcontent-ref %}

<div>

<figure><img src="../../../../.gitbook/assets/cam_ai3.png" alt=""><figcaption></figcaption></figure>

 

<figure><img src="../../../../.gitbook/assets/cam_ai4.png" alt=""><figcaption></figcaption></figure>

</div>
