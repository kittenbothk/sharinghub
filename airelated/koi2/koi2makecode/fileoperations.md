# 內存檔案操作

KOI 2現時可以將檔案放在內部儲存空間，如需刪除或複製內存的檔案，請參考以下教程。

### <mark style="color:green;">注意：此功能需要固件版本v4.0.7或以上</mark>

更新固件方法如下：

{% content-ref url="../koi-koi-1-2-gu-jian-sheng-ji/" %}
[koi-koi-1-2-gu-jian-sheng-ji](../koi-koi-1-2-gu-jian-sheng-ji/)
{% endcontent-ref %}

### <mark style="color:green;">MakeCode編程</mark>

在MakeCode打開專案，點擊擴展一頁。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/16-1.png" alt=""><figcaption></figcaption></figure>

在搜尋欄輸入koi 2。

<figure><img src="../../../.gitbook/assets/koi2_ext.gif" alt=""><figcaption></figcaption></figure>

加載成功後，積木欄會新增koi2的積木。

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 編程積木

<figure><img src="../../../.gitbook/assets/image (63).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 參考程式

{% hint style="info" %}
Armourbit用家請使用初始化Armourbit積木。
{% endhint %}

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F6uJvpXC43onNIIwhMlWo%2Fuploads%2FPGyECwlPd2M3JqUBLDfO%2Fimage.png?alt=media&#x26;token=662ace3f-a8eb-4fbf-8a10-1d9643c88b1e" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
KOI 2的SD卡要求比較高，請使用高速micro SD卡(class 10或以上)
{% endhint %}

{% embed url="https://makecode.microbit.org/_UMJXhTMz17Hc" %}

[參考程式](https://makecode.microbit.org/_UMJXhTMz17Hc)

#### 程式解說

1. 按A可以顯示KOI內部文件清單，5秒後會自動關閉清單
2. 按A+B可以將檔案複製到SD卡
3. 按B可以刪除檔案
