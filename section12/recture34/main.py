# 書きこむ内容
text="""おはよう
こんにちは
こんばんは"""
#text = '追記'

# ファイルを開き、ファイルを扱うためのオブジェクト
#file = open('hello.txt', 'w', encoding='utf-8')
#file = open('hello.txt', 'x', encoding='utf-8')
# ファイルに書き込む
#file.write(text)
# ファイルを閉じる
#file.close()

# 処理が終れば自動で閉じられる。
with open('hello.txt', 'w', encoding='utf-8') as file:
    file.write(text)