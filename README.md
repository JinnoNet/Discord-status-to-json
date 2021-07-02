# What is this?

Discordのステータスを取得してjsonファイルを出力するPythonスクリプト。  
[これを使ったサイト。](https://jinno.ga)

自分の環境
![ex](/img/ex.png)

Discordのウィジェットからもjsonファイルが出力されてるが、「何時間前にオンライン」という情報がないのでつくった。

## How to use

### 必須条件

* gitをインストール済み
* gitでGitHubにログイン済み
* GitPythonをダウンロード済み

```console
pip install GitPython
```

### 手順

1. ForkしてローカルにCloneする。
2. Discordで自分しか入っていないサーバーをつくる。
3. サーバー設定からウィジェットを有効にする。
4. サーバーidをメモる。
5. 以下の内容の`api.json`を同じディレクトリに作成する。

```json
{"url": "https://discordapp.com/api/guilds/"サーバーid"/widget.json"}
```

6. `Python script.py`で実行。一時間ごとに自動更新。

注意：status-json.json及び、status-json.jsonの中身を消すと動かなくなります。

## 出力内容

```json
{   "status": "Online", 
    "duration": 2,
    "date":
    {"y": "2021", "m": "07", "d": "02", "H": "21", "M": "26", "S": "46"}}
```

* `status` そのままの意味。
* `duration` オンラインの場合「何時間オンラインか」、オフラインの場合「何時間前までオンラインだったか」。
* `date` そのままの意味。
