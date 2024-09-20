# Makecode插件版本更換

***

我們在Makecode上使用Kittenbot的產品必須使用插件，而插件可能會不定時推出更新，改進功能。亦有時候我們可能需要轉用舊版插件才可使用某些功能。以下會講解一下檢查和更新插件版本的方法。

### 本教程使用KOI插件為例子，其他插件的做法與本教程相同。

### 我們先加載KOI插件：

{% content-ref url="kittenbotandmakecode.md" %}
[kittenbotandmakecode.md](kittenbotandmakecode.md)
{% endcontent-ref %}

### 檢查插件版本

檢查插件版本的方法如下：

1. 切換至JavaScript模式
2. 打開資源管理器
3. 檢查插件版本

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/check.gif" alt=""><figcaption></figcaption></figure>

### 更新插件版本

你可能正在使用舊版本的插件而需要更新，更新插件的方法如下：

1. 切換至JavaScript模式
2. 打開資源管理器
3. 點擊插件版本
4. 插件就會自動更新到最新版本

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/update.gif" alt=""><figcaption></figcaption></figure>

### 修改插件版本

你有時候可能會需要切換至之前版本的插件，更改插件版本的方法如下：

1. 打開專案設定
2. 點擊「以純文字模式編輯設定」
3.  在KOI的插件中，更改版本

    ```
     ( "koi" : "github:kittenbot/pxt-koi#v0.5.4" )->( "koi" : "github:kittenbot/pxt-koi#v0.2.4" )
    ```
4. 右擊然後儲存
5. 切換至Javascript模式
6. 檢查插件版本

<figure><img src="https://kittenbothk.readthedocs.io/en/latest/_images/modify.gif" alt=""><figcaption></figcaption></figure>
