#파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MongoDB

# 선언
a = {'name' : 'Kim', 'Phone' : '010-7777-7777', 'birth' : 870214}
# 키는 중복되면 안되지만 값은 중복 되도 됨.
b = {0: 'Hello python', 1:'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}

# print(type(a))

# 출력
print(a['name'])
print(a.get('addrerss'))
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1,2,3)
print(a)

# Keys, Values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))
print(2 in b)
print('name2' in a)
 
 # 집합(sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(b)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1.intersection(s2))
print(s1 & s2)
print(s1 | s2)
print(s1.union(s2))

print(s1-s2)
print(s1.difference(s2))



# 추가 제거 가능
s3 = set([7,8,10,15])
s3.add(18)
s3.add(7)
print(s3)

s3.remove(15)
print(s3)
