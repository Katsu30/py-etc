taple = (1,2,3,4,5)
taple2 = (6,7,8,9,10)

# この表記が一行で記述できる
r = []
for i in taple:
  r.append(i)
print(r)

# forで取り出したiをそのままリストに足すイメージ
# forを回してappend()するよりも早い
r = [ i for i in taple if i % 2 == 0]
print(r)

r = []
for i in taple:
  for j in taple2:
    r.append(i * j)
print(r)

# リスト内包表記は書きすぎると可読性が著しく下がるので注意
r = [ i * j for i in taple for j in taple2 if (i * j) % 2 == 0 ]
print(r)