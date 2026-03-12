# 3.2 生成式AI模型設定

## 準備辨認程式

### 數據線連接

使用USB線將未來板Lite連接到電腦，並將未來板Lite的電源開關撥向開。

<figure><img src="../../../.gitbook/assets/1_1x (1).png" alt="" width="563"><figcaption></figcaption></figure>

### 編程準備

首先前往KittenBlock編程平台。

{% embed url="https://kblock.kittenbot.cc/" %}

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

在硬件欄選擇未來板Lite AI。

<figure><img src="../../../.gitbook/assets/image (154).png" alt=""><figcaption></figcaption></figure>

電腦上面就會出現一個USB Drive，我們可以看到未來板Lite上面的檔案。

<figure><img src="../../../.gitbook/assets/image (226).png" alt=""><figcaption></figcaption></figure>

在右面的選項欄，可以看到代碼的切換鍵，點一下按鍵，頁面就會出現一個輕巧的Python編輯器。

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

訓練完成後可以修改辨認程式，設定好生成式AI。

打開未來板Lite上的diy\_run.py。

<figure><img src="../../../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (238).png" alt=""><figcaption></figcaption></figure>

首先修改prompt，讓生成式AI知道自己的角色和規則。

<figure><img src="../../../.gitbook/assets/image (239).png" alt=""><figcaption></figcaption></figure>

例如，這次我們的主題為中藥，我們可以賦予AI一個“本草綱目”的角色，讓AI知道自己要回答的是有關中藥的知識。

{% hint style="info" %}
你是一個AI本草綱目，你的職責是介紹小朋友提供的中藥材的資訊。回答盡量精簡，控制在90字之內。盡量以繁體字回答。
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (240).png" alt=""><figcaption></figcaption></figure>

最後更改KOI載入的模型名稱即可。

<figure><img src="../../../.gitbook/assets/image (241).png" alt=""><figcaption></figcaption></figure>

將diy.json更改為herb.json。（或你自選的模型名稱）

因為我們在訓練時將模型儲存為herb.json，因此我們在這裡載入同一個模型即可使用訓練好的模型。

<figure><img src="../../../.gitbook/assets/image (242).png" alt=""><figcaption></figcaption></figure>

最後不要忘記將檔案儲存，並放在未來板Lite上。

將檔案儲存為herb\_run.py。

<figure><img src="../../../.gitbook/assets/image (243).png" alt=""><figcaption></figcaption></figure>

## 使用辨認程式

以中藥材的專題為例子，打開未來板Lite的herb\_run.py。

<figure><img src="../../../.gitbook/assets/image (245).png" alt=""><figcaption></figcaption></figure>

首先試試辨認，看看KOI能否辨認5種藥材。

<figure><img src="../../../.gitbook/assets/image (244).png" alt=""><figcaption></figcaption></figure>

然後試試要AI為我們介紹這款藥材，試試我們的輸入的指令詞能否令AI回答我們特定的資料。

<figure><img src="../../../.gitbook/assets/image (246).png" alt=""><figcaption></figcaption></figure>

試試按M鍵，當未來板顯示Listening時，說出你的問題，語音辨識會識別你的問題然後交給生成式AI回答。

<figure><img src="../../../.gitbook/assets/image (247).png" alt=""><figcaption></figcaption></figure>
