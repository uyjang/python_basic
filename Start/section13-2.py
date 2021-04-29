# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time
import winsound # 소리 출력관련 모듈
import sqlite3
import datetime

# db생성 및 auto commit 설정
# 본인 db경로 설정
conn = sqlite3.connect('C:/python_basic/resource/records.db', isolation_level=None)

# Cursor 설정
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")

words = []    # 영어 단어가 들어갈 리스트( 1000개 )

n = 1        # 게임 시도 횟수 처음
cor_cnt = 0  # 정답 갯수

with open('./resource/word.txt','r') as f :
    for c in f:
        words.append(c.strip()) # 양쪽 공백을 제거하는 스트립 함수

print(words) # 단어 리스트 확인용

input("Ready? Press Enter Key!") # input함수는 사용자가 내용을 입력하고 엔터를 쳐야 밑에 있는 코드들이 실행
                                 # input함수는 무조건 string형이다.
start = time.time()

while n <= 5:
    random.shuffle(words) # 셔플이란 함수는 안에 들어가 있는 단어들을 무작위로 섞어주는 기능
    q = random.choice(words) # 초이는 랜덤으로 한개의 데이터를 뽑아온다

    print()

    print("*Question # {}".format(n))
    print(q)    # 문제 출력

    x = input() # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip() : # 입력값과 strip(공백제거 함수)
        print("Pass!")
        # 정답 소리 재생
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("Wrong!")
        # 오답 소리 재생
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
    n += 1 # 다음 문제

end = time.time() # End Time
et = end - start  # 총 게임시간
et = format(et,".3f") # 소수 셋째 자리까지 출력(시간)

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# 기록 db 삽입
cursor.execute("INSERT INTO records('cor_cnt','record','regdate') VALUES(?,?,?)", (cor_cnt,et,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

# 수행 시간 출력
print("게임시간 : ", et,"초", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass