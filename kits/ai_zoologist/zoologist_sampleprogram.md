# 範例程式

## 接線教學

<figure><img src="../../.gitbook/assets/wiring.png" alt=""><figcaption></figcaption></figure>

## KOI 2圖像分類模型訓練

#### Kittenblock SB3

<figure><img src="../../.gitbook/assets/trainingprogram (1).png" alt=""><figcaption></figcaption></figure>

{% file src="../../.gitbook/assets/瀕危物種KOI Training (1).sb3" %}

#### Python

{% file src="../../.gitbook/assets/koi_train.py" %}

#### 範例圖片

{% file src="../../.gitbook/assets/瀕危動物圖片.pdf" %}

### 使用教學

1. 按A錄入分類數據
2. 按B跳至下一個分類
3. 按M儲存模型

## AI鑑別器

{% file src="../../.gitbook/assets/species_run.py" %}

{% file src="../../.gitbook/assets/wifi.txt" %}

### 設定教學

#### 1. 打開wifi.txt,填入wifi的登入資料

{% hint style="info" %}
使用逗號 , 分隔ssid和密碼,ssid和密碼不可以有空格
{% endhint %}

<figure><img src="../../.gitbook/assets/image (218).png" alt=""><figcaption></figcaption></figure>

#### 2. 在未來板Lite啟動species\_run.py

#### 3. 等待KOI載入模型後重新開機

#### 4. 打開未來板Lite的胖虎編程平台

{% content-ref url="../../mcu/liteai/bunfu.md" %}
[bunfu.md](../../mcu/liteai/bunfu.md)
{% endcontent-ref %}

#### 5. 在文件清單中打開expert.agt

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 6. 打開配置的頁面

<figure><img src="../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

#### 7. 在訪問令牌的一欄填入API Key

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

#### 8. 選擇語音模型為粵語

<figure><img src="../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

### 使用教學

完成設定後,可以按影片示範般使用AI鑒別器.

1. 按A鍵辨認動物
2. 按B鍵 AI就會講解一下這動物的資料
3. 按M鍵可以詢問AI更多問題

{% embed url="https://youtu.be/biYq0kSc5No" %}
