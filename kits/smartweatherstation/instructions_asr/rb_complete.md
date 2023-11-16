# 完整氣象站

<figure><img src="../../../.gitbook/assets/complete_robotbit (1).png" alt=""><figcaption></figcaption></figure>

### 模型搭建說明書

{% content-ref url="../building/wan-zheng-qi-xiang-zhan-shuo-ming-shu.md" %}
[wan-zheng-qi-xiang-zhan-shuo-ming-shu.md](../building/wan-zheng-qi-xiang-zhan-shuo-ming-shu.md)
{% endcontent-ref %}

### 模型接線圖

<figure><img src="../../../.gitbook/assets/complete_wiring_robotbit (1).png" alt=""><figcaption></figcaption></figure>

### MakeCode參考程式

{% hint style="info" %}
風向的數值需校正。
{% endhint %}

{% embed url="https://makecode.microbit.org/_YiVhbH0xb74u" %}

#### 模型玩法

1. 可以按A和B切換多種模式，相關的數據會在OLED上顯示。
   1. 模式1:  風向與風速模式
   2. 模式2: 溫度與氣壓模式
   3. 模式3: 亮度與雨量模式
2. 說出喚醒詞Hey Sugar / Hello Kittenbot，然後說出Check Temperature或Check Humidity，語音模組會報讀溫度或濕度

### 校正步驟

首先下載參考程式，OLED模組會一直顯示灰度感應器的讀數。

利用套件附帶的指南針，將指針撥向北的方位。記錄灰度感應器的讀數，這讀數就是北這個方位的校正數值。

<figure><img src="../../../.gitbook/assets/20231116_132248.jpg" alt=""><figcaption></figcaption></figure>

打開MakeCode，將北的校正數值填入程式裡面。

{% hint style="info" %}
例如，指針在北這個方位時讀數為443，將此數值填入程式中。
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

重複以上步驟，對其餘3個方位進行校正。

<figure><img src="../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>

完成後再次下載程式到Micro:bit。
