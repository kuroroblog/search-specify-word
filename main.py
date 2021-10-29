# ファイルを開く。
# 参考 : https://note.nkmk.me/python-file-io-open-with/
fp = open('sample.txt', "r", encoding="utf-8")

# 特定の文字列を設定する。hogeとする。
specify_word = 'hoge'

# ファイルをリスト型で読み込む。
# 今回(sample.txt)の場合、['hoge', 'fuga', 'piyo', 'aiueo', 'kakikukeko', 'hogepiyo']で読み込む。
# 参考 : https://note.nkmk.me/python-file-io-open-with/
# for文を回すことで、wordの中へ順に'hoge', 'fuga', ...が格納される。
for word in fp.readlines():
    # strip : wordの前後に含まれる、空白文字を削除する。
    # 参考 : https://note.nkmk.me/python-str-remove-strip/
    word = word.strip()

    # 特定の文字列と一致する、wordを探し出す。
    # 参考 : https://note.nkmk.me/python-in-basic/
    if specify_word in word:
        print(word)
