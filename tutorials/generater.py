# l = [ 'Good morning', 'Good afternoon', 'Good night' ]

# for item in l:
#   print(item)

def counter(num = 10):
  for _ in range(num):
    yield 'run'

print('################')

def greeting():
  yield 'Good morning'
  yield 'Good afternoon'
  yield 'Good night'

# 関数呼び出しでもfor文を回すことができる
# for g in greeting():
#   print(g)

# next()の形でyieldした値を一つずつ取り出すことが可能
g = greeting()
c = counter()

print(next(g))
print(next(c))
print(next(g))