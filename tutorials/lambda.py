l = [ 'Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun' ]

def change_words(words, func):
  for word in words:
    print(func(word))

# 下記の記述がラムダを使用すると楽に書ける
# def sample_func(word):
#   return word.capitalize()

# JSで言うアロー関数のようなもの
# 'lambda'の表記の後に引数
# ':'で区切った後に返り値を設定する
sample_func = lambda word : word.capitalize()

change_words(l, sample_func)
# change_words(l, lambda word : word.capitalize())