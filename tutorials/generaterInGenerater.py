def g():
  for i in range(10):
    yield i

g = g()
print(type(g))

g = (i for i in range(10))
print(type(g))
print(next(g))
print(type(g))
print(next(g))
print(type(g))
print(next(g))