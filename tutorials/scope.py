animal = 'cat'

def f():
  # globalスコープの値を変更する際は宣言が必要
  # global animal
  animal = 'dog'
  print('local : ', locals())
f()

print('global : ', globals())