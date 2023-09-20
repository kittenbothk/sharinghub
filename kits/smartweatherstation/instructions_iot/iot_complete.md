# 完整氣象站

<figure><img src="../../../.gitbook/assets/complete_robotbit.png" alt=""><figcaption></figcaption></figure>

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

{% embed url="https://makecode.microbit.org/_57mhz2DX3afq" %}

#### 模型玩法

1. 可以按A和B切換多種模式，相關的數據會在OLED上顯示。
   1. 模式1:  風向與風速模式
   2. 模式2: 溫度與氣壓模式
   3. 模式3: 亮度與雨量模式
2. 說出Check Temperature或Check Humidity，語音模組會報讀溫度或濕度
