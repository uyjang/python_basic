# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로, . : 절대 경로

# 파일 읽기
# 예제 1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
f.close() # 반드시 close를 통해 리소스를 반환해줘야 됨

print()
print()

# 예제2
# with구문과 함께 사용하면 f.close를 안해도 알아서 리소스를 반환해줌
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c)) # for문 가능

print()
print()

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print()
print()

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 커서가 단락의 끝으로 간 상태라서 읽어들일 내용이 없다.
    print(">", content)

print()
print()

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline() # 한문장 단위로 읽어오게 할 때
    # print(line)
    while line:
        print(line,end=' ')
        line = f.readline()

print()
print()

# 예제6
with open('./resource/review.txt', 'r') as f:
    content = f.readlines() # 엔터(\n)을 기준으로 리스트형태로 만든 것
    print(content)
    for c in content:
        print(c, end = ' ***** ')

print()
print()

# 예제7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)
print('average : {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기

# 예제1
with open('./resource/text1.txt','w') as f:
    f.write('niceman\n')

# 예제2
with open('./resource/text1.txt','a') as f:
    f.write('goodman\n') 

# 예제3
from random import randint
with open('./resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(1,50)))
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list = ['kim\n', 'park\n', 'cho\n']
    f.writelines(list)

# 예제5
with open('./resource/text4.txt','w') as f:
    print('Test contest1!', file = f) # file = f라는 파라미터때문에 콘솔창이 아니라 파일에 직접 입력됨.
    print('Test contest2!', file = f)


























