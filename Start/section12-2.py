# 파이썬 데이텁이스 연동(SQLite)
# 테이블 조회

import sqlite3

# db파일 조회 (없으면 새로 생성)
conn = sqlite3.connect('C:/python_basic/resource/database.db') # 본인 db경로

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 불러올 때마다 변경
# 1개 로우 선택 (2번커서로 이동됨)
# print('One -> \n', c.fetchone())

# 지정 로우 선택(5번 커서로 이동됨)
# print('Three -> \n', c.fetchmany(size = 3))

# 전체 로우 선택
# print('All -> \n', c.fetchall())
# print('All -> \n', c.fetchall())

print()

# 순회1
rows = c.fetchall() # 이미 커서가 끝(아무것도 없는 부분)을 가리키기 때문에 주석처리함
for row in rows:
    print('retrieve 1 >', row)

# 순회2
# for row in c.fetchall():
#     print('retrieve 2 >', row)

# # 순회3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve 3 >', row)

print()

# WHERE Retrieve1
Param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?',Param1)
print('Param1',c.fetchone())
print('Param1',c.fetchall())

# WHERE Retrieve2
Param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % Param2)
print('Param2',c.fetchone())
print('Param2',c.fetchall())

# WHERE Retrieve3
c.execute('SELECT * FROM users WHERE id=:Id',{"Id":5})
print('Param3',c.fetchone())
print('Param3',c.fetchall())

# WHERE Retrieve4
param4 = (3,5)
c.execute("SELECT * FROM users WHERE id IN(?,?)",param4)
print('param4',c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3,4))
print('param5',c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2",{"id1":2, "id2":5})
print('param6',c.fetchall())

# Dump 출력 (덤브를 뜨다, 서버나 컴퓨터가 바뀌었을 때 해당 데이터를 가져오기 위함)
with conn:
    with open('C:/python_basic/resource/dump.sql','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump print Complete')
# f.close(),conn.close()함수도 같이 호출이 됐다 (with문에서)





















