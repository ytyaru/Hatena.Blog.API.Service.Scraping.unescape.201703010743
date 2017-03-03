# このソフトウェアについて

はてなブログAPIで取得したブログ記事本文のエスケープ(サニタイズ)を元に戻す。

# 開発環境

* Linux Mint 17.3 MATE
* Firefox 42.0
* Python 3.4.3

## Webサービス

* [はてなブログAPI](http://developer.hatena.ne.jp/ja/documents/blog/apis/atom)
    * サービス文書URI(`https://blog.hatena.ne.jp/{はてなID}/{ブログID}/atom`)

# 準備

1. [こちら](https://github.com/ytyaru/Hatena.Blog.API.Service.Get.201702281505)ではてなブログサービス文書を取得し、XMLファイル保存する
1. main.pyの以下の部分のパス`../resource....xml`を保存したパスに変更する

```python
soup = BeautifulSoup(self.__load_file("../resource/201702281505/ytyaru.ytyaru.hatenablog.com.Services.xml"), 'lxml')
```

# 実行

```sh
python3 main.py
```

# 結果

サービス文書XMLファイルから一部データを抜き取り、コンソールに表示される。

* ブログのタイトル
* `<link rel=next>`の`href`属性値
* `<entry><title>`のテキストノード値
* '<content>'のテキストノード値

エスケープ文字が元に戻っていることを確認する。たとえば`&lt;`が`<`になっていることを確認する。

# 要点

```python
import html
html.unescape('&lt;')
```

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

なお、使用させていただいたライブラリは以下のライセンスである。感謝。

Library|License|Copyright
-------|-------|---------
[xmltodict](https://github.com/martinblech/xmltodict)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (C) 2012 Martin Blech and individual contributors.](https://github.com/martinblech/xmltodict/blob/master/LICENSE)
[requests_oauthlib](https://github.com/requests/requests-oauthlib)|[ISC](https://opensource.org/licenses/ISC)|[Copyright (c) 2014 Kenneth Reitz.](https://github.com/requests/requests-oauthlib/blob/master/LICENSE)
[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright © 1996-2011 Leonard Richardson](https://pypi.python.org/pypi/beautifulsoup4),[参考](http://tdoc.info/beautifulsoup/)

