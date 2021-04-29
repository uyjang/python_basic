# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is : ", v1)
    v1 += 1
for v2 in range(10):
    print("v2 is : ", v2)

for v3 in range(1,11):
    print("v3 is : ", v3)

# 1부터 100까지 합
sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print('1 ~ 100의 합 : ', sum1)   
print('1 ~ 100의 합 : ', sum(range(1, 101)))
print('1 ~ 100 : ', sum(range(1, 101, 10)))

# 시퀀스(순서가 있는 자료형을 반복한다.)
# 문자열, 리스트, 튜플, 집합, 사전  *집합과 사전은 순서가 없지만 가능
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ["Kim", "Park", "cho", "choi", "Yoo"]

for name in names:
    print("You are : ", name)

word = "dreams"

for s in word:
    print("word : ", s)

my_info = {
    "name" : "kim",
    "age" : 33,
    "city" : "seoul"
}

for key in my_info:
    print("myinfo", key)

for key in my_info.keys():
    print("myinfo", key)
for key in my_info.values():
    print("myinfo", key)
for k, v in my_info.items():
    print("myinfo", k, v)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

# for num in numbers:
#     if num == 33:
#         print("found : 33!")
#         break
#     else:
#         print("not found : 33")

# for - else 구문 (반복문이 정상적으로 실행될 경우 else블럭 실행, break가 있으면 실행 안됨)

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found : 33")
else:
    print("Not found 33......")

# continue (컨티큐 조건에 만족하는 것은 스킵하고 계속 실행)

lt = ["1", 2,5,True,4.3,complex(4)]

for v in lt:
    if type(v) is float :
        continue
    print("타입 : ", type(v))

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))