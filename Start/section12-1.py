# 파이썬 데이터베이스 연동 (SQLITE)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print(now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# sqlite3 버전
print('sqlite3.version: ', sqlite3.version)
print('sqlite3.sqite_version : ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit (Rollback)
conn = sqlite3.connect('C:/python_basic/resource/database.db',isolation_level=None)
print()
# cursor
c = conn.cursor()
print(type(c))

# 테이블 생성(data type : text, numeric, integer, real, blob)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1,'Kim','Kim@naver.com','010-0000-0000', \
    'Kim.com', ?)", (nowDatetime,)) # nowDatetime을 그대로 적어 넣으면 오류가 나오기 때문에 튜플형태로 집어 넣는다.
                                    # ?가 튜플이 들어갈 자리고 ,뒤에 튜플에 들어갈 변수를 넣는다
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",(2,'Park','Park@daum.net','010-1111-1111','Park.com',nowDatetime))

# many 삽입(대용량, 튜플, 리스트 형태 삽입가능)
userList = (
    (3,'lee', 'lee@naver.com','010-2222-2222','lee.com',nowDatetime),
    (4,'cho','cho@naver.com','010-3333-3333','cho.com',nowDatetime),
    (5,'jang','jang@naver.com','010-4444-4444','jang.com',nowDatetime),
) 

c.executemany("INSERT INTO users(id,username,email,phone,website,regdate) \
    VALUES(?,?,?,?,?,?)",userList)

# 테이블, 데이터 삭제
# conn.execute("DELETE FROM users")
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동으로 반영(오토 커밋)
# conn.commit()
# conn.rollback()

# 접속해제
# conn.close()

