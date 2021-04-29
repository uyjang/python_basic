# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드실행 시 (런타임)프로세스에서 발생하는 예외처리는 중요
# linter : 코드 스타일 알려주고, 문법 체크

# SyntaxError : 잘못된 문법
# print('test) 
# if True
#     pass

# NameError : 참조 변수 없음

a = 10
b = 15

# print(c)

# ZeroDivisionError : 0으로 나누기 에러
# print(10/0)

# IndexError : 인덱스 범위 오버
x = [10,20,30]
print(x[0])
# print(x[3])

# KeyError
dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul' }

# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month())

# ValueError : 참조값이 없을때 에러
c = [1,5,9]
# c.remove(10)
# c.index(10)

# FileNotFoundError
# f = open('test.txt','r')

# TypeError

x = [1,2]
y= (1,2)
z = 'test'
# print(x+y)
# print(x+z) 
print(x + list(y))

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩한다.
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAEP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# except : 에러명3
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x =  name.index(z)
    print('{} Found it in name'.format(z,x+1))
except ValueError:
    print('Not found in! - Occurred ValueError!')
else:
    print('Ok! else!')

print()

# 예제2

try:
    z = 'Jin'
    x =  name.index(z)
    print('{} Found it in name'.format(z,x+1))
except:
    print('Not found in! - Occurred Error!')
else:
    print('Ok! else!')
print()

# 예제3

try:
    z = 'Jin'
    x =  name.index(z)
    print('{} Found it in name'.format(z,x+1))
except:
    print('Not found in! - Occurred Error!')
else:
    print('Ok! else!')
finally:
    print('finally ok!')

print()

# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok Finally!!!!')
print()

# 예제5

try:
    z = 'Jin'
    x =  name.index(z)
    print('{} Found it in name'.format(z,x+1))
except ValueError: # except ValueError as l 엘리아스 구문도 사용가능 , print(l)로 실행
    print('Not found in! - ValueError Error!')
except IndexError:
    print('Not found in! - IndexError Error!')
except Exception: # 모든 에러를 잡아내는 것이라서 맨 위에 놓게 되면 vlaue에러인지, index에러인지 모르게 된다.그래서 마지막에 나오는 것
    print('Not found in! - Occurred Error!')
else:
    print('Ok! else!')
finally:
    print('finally ok!')
print()

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = '333'
    if a == 'Kim':
        print('ok 허가!')
    else:
        raise ValueError
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('OK')