# 파이썬 모듈과 패키지

# 패키지 예제
# 상대경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1
from pkg.fibonacci import Fibonacci
Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)
print()


# 사용2
from pkg.fibonacci import Fibonacci as fb
fb.fib(300)

print("ex2 : ", fb.fib2(400))
print("ex2 : ", fb().title)

# 사용3
import pkg.calculations as c
print("ex4 : ", c.add(10,100))
print("ex4 : ", c.mul(10,100))
print("ex4 : ", c.div(10,100))

# 사용4
from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))

# 사용5
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))