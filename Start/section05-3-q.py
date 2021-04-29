# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for k,v in q1.items() :
    if k == '가을':
        print(k + ' :',v)

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "연시"}
for k,v in q2.items() :
    if v == '사과':
        print(k + ' :',v)
        break
else:
    print("사과가 없음")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
a = 20
if a > 80 :
    print("A학점")
elif a > 60 :
    print("B학점")
elif a > 40 :
    print("C학점")
elif a > 20 :
    print("D학점")
else:
    print("E학점")
# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 3, 9, 16
best = a
if a < b:
    best = b
    if b < c:
        best = c
print(best)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '940502-4042110'
if int(s[7]) % 2 == 0 :
    print("여자입니다.")
else :
    print("남자입니다.")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for m in q3:
    if m == "정":
        continue
    else:
        print(m)

print()

q99 = [x for x in q3 if x != '정']
print(q99)


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
# for n in range(1,101):
#     if n % 2 != 0:
#         print(n,end=' ')

print()

q100 = [x for x in range(1,101) if x % 2 != 0]
print(q100)

print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
# for v in q4:
#     if len(v) >= 5 :
        # print(v,end=',')
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
# for n in q5:
#     if n.islower():
#         print(n,end=',')


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for c in q6:
    if c.islower():
        print(c.lower(),end=',')
    else:
        print(c.upper(),end=',')

# 리스트 컴프리헨션

# 1. 일반적인 방법
numbers = []
for n in range(1,101):
    numbers.append(n)
print(numbers)

# 2. 다른 방법
numbers2 = [x for x in range(1,101)]
print(numbers2)



