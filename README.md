# LineNotify

Python プログラム内から計算結果等をLineに通知するライブラリ


# 使い方

- 事前に[LINE Notifyのマイページ](https://notify-bot.line.me/ja/)にログインし,アクセストークンを取得してご使用ください．
- 通知したいプログラムと同じ階層のディレクトリに配置しimport する
  + `from line_notify import LineNotify as Line`
- アクセストークを引数にクラスを呼び出す．
  + `myLine = Line(token)`
- 通知を送りたい場所で以下の処理を追加する
  + 文字列を送るとき : `myLine.send("text")`
  + 画像を送るとき : `myLine.send("image","/path/to/image.jpeg")`
  
## 例
```
from line_notify import LineNotify as Line
token = 'xxxxxxxxxxxxxx' # 取得したトークン
myLine = Line(token)

do_something()

myLine.send("text") # 文字だけを送る場合
myLine.send("image","/path/to/image.jpeg") # 画像を送る場合
```
