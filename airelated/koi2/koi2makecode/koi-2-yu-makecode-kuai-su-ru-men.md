# KOI 2與MakeCode快速入門

## <mark style="color:orange;">**接線方法**</mark>

### **1. 與Robotbit EDU 組合使用**

使用隨盒附送的4pin 線, 白色大插頭插入KOI 中

Robotbit Edu上已經提供了4pin的通訊連供電接口，我們只需要將KOI連接到通訊接口(如下圖)就可以了。

由於Robotbit Edu的通訊接口使用了P2與P12，我們在MakeCode裡面就要相應地選擇引腳。

<mark style="background-color:yellow;">注:  如欲為KOI 2以USB 方式額外供電, 請拔走黑 (GND) 及 紅(5V) 2跟線。</mark>

<figure><img src="../../../.gitbook/assets/edu_wiring.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/edu2.png" alt="" width="375"><figcaption></figcaption></figure>

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

<figure><img src="../../../.gitbook/assets/koi_robotbit_2.2.png" alt=""><figcaption></figcaption></figure>

**重要事項: 黑 (GND) 及 紅(5V) 切勿反接!!!**[**¶**](broken-reference)

再次_檢查接線無誤_ 後, 就可以打開Robitbit 的開關, 便會看到KOI 的屏幕顯示出開機畫面。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/robotbit_connection2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/robotbit_connection3-1.png" alt=""><figcaption></figcaption></figure>

### **3. 使用Armourbit**

接線系統上, Armourbit 相對簡易便捷, 只需把2頭都是白色4芯插頭的接線 (Cable C), 分別接到KOI 2 及Armourbit  (Port 2) 上便可以了。

註: Cable C 並非KOI 2 的標準配套件, 訂購時請註明需求。

<figure><img src="../../../.gitbook/assets/spaces_sN6MlwBFbL3P67FzMMyL_uploads_6SD3k38DJUYRYqf5hwXJ_4P to 4pin PH2.webp" alt=""><figcaption></figcaption></figure>



Armourbit與KOI配合使用時，KOI必須額外提供5V電。

大家可以從Armourbit的電池盒, 以USB介面進行引出(如下圖)。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/armourbit_connection1-1.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/armourbit_connection2-3.png" alt=""><figcaption></figcaption></figure>

## <mark style="color:orange;">MakeCode插件快速解說</mark>

### 加入MakeCode插件

成功接線後就可以準備編程。

插件地址：

## [**https://github.com/KittenBot/pxt-koi2**](https://github.com/KittenBot/pxt-koi2)

在MakeCode打開專案，點擊擴展一頁。

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/16-1.png" alt=""><figcaption></figcaption></figure>

將擴展地址貼到搜尋欄。

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2F0hI8FvrIyWTHfQgfJ1at%2FKOI%202%20extension.jpg?alt=media&#x26;token=2936c6bb-2d61-42fd-8ec6-d829c4e039a8" alt=""><figcaption><p>KOI 2 Extension 搜尋畫面</p></figcaption></figure>

加載成交後，積木欄會新增koi2的積木。

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FSkO076z0lrID98zSivpa%2Fimage.png?alt=media&#x26;token=41cbc34a-9933-49f6-a4ce-62c0af2e6822" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">1. 初始化</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FjPCDYYmTZPo2Jnzf1RyN%2Fimage.png?alt=media&#x26;token=fb13d3f5-af5e-4b57-9db6-6492ac512aaa" alt=""><figcaption></figcaption></figure>

初始化Micro:Bit與KOI 2的連接, 必須加入每個程式中。

#### &#x20;<mark style="background-color:yellow;">2. 基本積木</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2Fg8gveE0DC4idrYoORQEx%2Fimage.png?alt=media&#x26;token=97b18306-46f0-43d8-8aba-690e1ac10ca3" alt=""><figcaption></figcaption></figure>

KOI 2的基本功能，包括拍照錄音按鍵等。

#### &#x20;<mark style="background-color:yellow;">3. 模式選擇</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FekJiYjyUbxlSyxEZst79%2Fimage.png?alt=media&#x26;token=3ac5b3d8-231d-4815-a6f7-b0d4e7b5895c" alt=""><figcaption></figcaption></figure>

選擇KOI 2的運行模式，進行任何AI功能之前都必須選擇相應模式 (同時間只能運行1個模式, 可通過按鍵編程轉換模式)。

#### &#x20;<mark style="background-color:yellow;">4. 人面屬性類</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2F4NqJm2V0GxQz4VCrHMom%2Fimage.png?alt=media&#x26;token=ea871158-217c-4b7a-aa85-378910511885" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">5. 人面口罩追蹤</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FM8Wgv7SSdEBIsp8KvNYk%2Fimage.png?alt=media&#x26;token=14a13c24-be54-4cd2-819a-9caac5971deb" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">6. 色塊追蹤</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FqLOoRdzxjrDItARCGQoe%2Fimage.png?alt=media&#x26;token=9214c3d0-86fe-4a2f-adc3-8acde2705a1e" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">7. 線條追蹤</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FONDuKNPPQqvb0eUB6cmr%2Fimage.png?alt=media&#x26;token=35c455e1-e03d-4689-960e-ee8d64cfec35" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">8. 機器學習 圖像辨識</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FKJBCamCme1kOp87DZSyo%2Fimage.png?alt=media&#x26;token=86c63e73-8232-4693-9be0-9050a915bbc4" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">9. 預載模型 路牌追蹤</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2Fxwg4eGR6tbLqXPl1Uslk%2Fimage.png?alt=media&#x26;token=486a2258-d6e2-4ebb-8c2e-15a21bc17794" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">10. 預載模型 數字追蹤</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FcSBWcbLHC7EmzXJtVODY%2Fimage.png?alt=media&#x26;token=c7c88a1a-7230-40fa-aa77-7f670d635ea2" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">11. 預載模型 物件追蹤</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FcdrSY8oosgOkO5QZqcAJ%2Fimage.png?alt=media&#x26;token=a11b81a3-c3a4-4ea8-8213-57eed61585b0" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">12. 掃碼類</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2Flg1tHcVhYhBKet094EBH%2Fimage.png?alt=media&#x26;token=1ce40289-bc01-4e33-989c-ccd38bebe56a" alt=""><figcaption></figcaption></figure>

#### &#x20;<mark style="background-color:yellow;">13. WiFi物聯網類</mark>&#x20;

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FsN6MlwBFbL3P67FzMMyL%2Fuploads%2FPTCn8iBkL2mRlll9o3sm%2Fimage.png?alt=media&#x26;token=d0f50193-99e4-4f16-8ea9-28322d35ccd6" alt=""><figcaption></figcaption></figure>
