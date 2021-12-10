# ファイルをオープンして、1行ずつその内容を読み込んで処理する
with open('test.txt',encoding='UTF-8') as f:
    for line in f:
        line = line.rstrip()  # 読み込んだ行の末尾には改行文字があるので削除
        print(line)
# 出力結果（4行目に空行が表示されるときとされないときがあるのを除き、以下同じ）

# テキストファイルをオープンして、その内容を全て読み込み、クローズする
f = open('test.txt',encoding='UTF-8')  # f = open('test.txt', 'rt'):
s = f.read()  # ファイルの全内容が1つの文字列として返される
print("総文字数は" + str(len(s)) +"文字")
f.close()

# with文と組み合わせると使い終わったとき（ブロック終了時）や
# 例外が発生したときにファイルが自動的にクローズされる
with open('test.txt',encoding='UTF-8') as f:
    s = f.read()

