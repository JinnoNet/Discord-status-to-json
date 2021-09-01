# What is this?

Discord のステータスを取得して json ファイルを出力する Python スクリプト。  
[これを使ったサイト。](https://jinno.ga)

自分の環境
![ex](/img/ex.png)

Discord のウィジェットからも json ファイルが出力されてるが、「何時間前にオンライン」という情報がないのでつくった。

## How to use

### 必須条件

- git をインストール済み
- git で GitHub にログイン済み
- GitPython をダウンロード済み

```console
pip install GitPython
```

### 手順

1. Fork してローカルに Clone する。
2. Discord で自分だけのサーバーをつくる。(Botも入れてはいけない)
3. サーバー設定からウィジェットを有効にする。
4. サーバー id をメモる。
5. 以下の内容の`api.json`を同じディレクトリに作成する。

```json
{"url": "https://discordapp.com/api/guilds/"サーバーid"/widget.json"}
```

6. `Python script.py`で実行。1分間隔で自動更新。

注意：status-json.json 及び、status-json.json の中身を消すと動かなくなります。

## 出力内容

1 分間隔で出力。

```json
{
  "status": "Online",
  "changeDateTime": { "y": 2021, "m": 7, "d": 3, "H": 16, "M": 31, "S": 7 },
  "timeLag": "12",
  "upDateTime": {
    "y": "2021",
    "m": "07",
    "d": "03",
    "H": "16",
    "M": "31",
    "S": "07"
  }
}
```

- `status` そのままの意味。
- `changeDateTime` オンライン、オフラインが切り替わった時間。
- `timeLag` オンライン、オフライン時の長さ(分)。
- `upDateTime` そのままの意味。
