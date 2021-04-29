# 파이썬 데이터 베이스 연동
# 테이블 수정 및 삭제

import sqlite3

# db생성
conn = sqlite3.connect('C:/python_basic/resource/database.db')

# cursor
c = conn.cursor()

# 데이터 수정1
# c.execute("UPDATE users SET username = ? WHERE id = ?",('niceman',2))
# conn.commit()

# # 데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id = :id",{"name":'goodman',"id":5})
# conn.commit()

# # 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy',3))
# conn.commit()

# 중간 데이터 확인1
for user in c.execute("SELECT * FROM users"):
    print(user)

# Row Delete1
c.execute("DELETE FROM users WHERE id = ?",(2,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id",{"id": 5})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)

print()

# 중간 데이터 확인2
for user in c.execute("SELECT * FROM users"):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount," rows ")

#커밋
conn.commit()

# 접속해제 (with문을 쓰지 않았기 때문에 수동으로 해준다)
conn.close()