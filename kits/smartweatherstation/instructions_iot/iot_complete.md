# 完整氣象站

<figure><img src="../../../.gitbook/assets/complete_robotbit.png" alt=""><figcaption></figcaption></figure>

### 模型搭建說明書

{% content-ref url="../building/wan-zheng-qi-xiang-zhan-shuo-ming-shu.md" %}
[wan-zheng-qi-xiang-zhan-shuo-ming-shu.md](../building/wan-zheng-qi-xiang-zhan-shuo-ming-shu.md)
{% endcontent-ref %}

### 模型接線圖

<figure><img src="../../../.gitbook/assets/complete_wiring_robotbit_iot.png" alt=""><figcaption></figcaption></figure>

### MakeCode參考程式(MakerCloud)

{% hint style="info" %}
請自行填入MakerCloud的主題名稱和數據類型等資訊。
{% endhint %}

{% embed url="https://makecode.microbit.org/_TJYbX3bApWqr" %}

### MakeCode參考程式(ThingSpeak)

{% embed url="https://makecode.microbit.org/_Hrf9PpbLgb65" %}

#### 模型玩法

1. 可以按A和B切換多種模式，相關的數據會在OLED上顯示，同時會向IoT平台發佈有關的數據。
   1. 模式1:  風向與風速模式
   2. 模式2: 溫度與氣壓模式
   3. 模式3: 亮度與雨量模式
2. 在IoT平台上會看到天氣數據
