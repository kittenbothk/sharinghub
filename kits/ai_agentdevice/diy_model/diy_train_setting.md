# 3.1 AI鑑別器模型訓練

## 準備訓練程式

### 數據線連接

使用USB線將未來板Lite連接到電腦，並將未來板Lite的電源開關撥向開。

<figure><img src="../../../.gitbook/assets/1_1x (1).png" alt="" width="563"><figcaption></figcaption></figure>

### 編程準備

首先前往KittenBlock編程平台。

{% embed url="https://kblock.kittenbot.cc/" %}

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

在硬件欄選擇未來板Lite AI。

<figure><img src="../../../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

電腦上面就會出現一個USB Drive，我們可以看到未來板Lite上面的檔案。

<figure><img src="../../../.gitbook/assets/image (226).png" alt=""><figcaption></figcaption></figure>

在右面的選項欄，可以看到代碼的切換鍵，點一下按鍵，頁面就會出現一個輕巧的Python編輯器。

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

我們可以載入Python檔案在平台編輯，打開未來板Lite上的diy\_train.py。

<figure><img src="../../../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (228).png" alt=""><figcaption></figcaption></figure>

首先我們需要輸入要訓練的分類名稱，讓KOI知道每個分類的名稱，大家只需將分類的名稱按指示輸入到第17行裡面items這個清單即可。

<figure><img src="../../../.gitbook/assets/image (229).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
* 記住每個分類都要使用雙引號 “” 包著
* 每個分類用逗號 , 分隔
* 而且分類不可以有空格

例如淮山的英文為Chinese Yam，我們就需要將空格去掉變成ChineseYam
{% endhint %}

以中藥材的專題為例子，完整的items就為：

```python
items = [“ChineseYam”, ”Chrysanthemum”, “Wolfberry”, “CodonopsisPilosula”, “WolfiporiaExtensa”]
```

<figure><img src="../../../.gitbook/assets/image (230).png" alt=""><figcaption></figcaption></figure>

然後我們需填寫模型的名稱，讓我們之後存取模型時更方便。

<figure><img src="../../../.gitbook/assets/image (231).png" alt=""><figcaption></figcaption></figure>

以中藥材的專題為例子，將第31行的diy.json改為herb.json。（或你自選的模型名稱）

我們可以每個主題都建立一個資料庫，這樣就不會每次都將之前的數據清空了。

<figure><img src="../../../.gitbook/assets/image (232).png" alt=""><figcaption></figcaption></figure>

最後將檔案儲存，放在未來板Lite上。

以中藥材的專題為例子，將檔案儲存為herb\_train.py。

<figure><img src="../../../.gitbook/assets/image (233).png" alt=""><figcaption></figcaption></figure>

## 使用訓練程式

以中藥材的專題為例子，打開未來板Lite的herb\_train.py。

<figure><img src="../../../.gitbook/assets/image (234).png" alt=""><figcaption></figcaption></figure>

未來板上顯示ChineseYam，代表現在要訓練的分類是淮山。

將KOI 2對準淮山的圖片，按下A鍵，KOI就會錄入淮山的數據。

試試在不同角度和距離錄入數據，提高辨認的準確度。

<figure><img src="../../../.gitbook/assets/image (235).png" alt=""><figcaption></figcaption></figure>

完成訓練淮山的圖片後，按一下B鍵，未來板就會顯示Chrysanthemum。

將KOI 2對準菊花的圖片，按下A鍵，KOI就會錄入菊花的數據。

重複以上步驟，完成訓練各款中藥的分類。

<figure><img src="../../../.gitbook/assets/image (236).png" alt=""><figcaption></figcaption></figure>

最後按下中間的M鍵，儲存模型。

成功儲存的話KOI 2會顯示Save Successfully的字樣。

<figure><img src="../../../.gitbook/assets/image (237).png" alt=""><figcaption></figcaption></figure>
