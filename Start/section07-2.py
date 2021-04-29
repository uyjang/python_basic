# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼 클래스(부모) 및 서브 클래스(자식) -> 자식은 모든 속성, 메소드 사용가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None :
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None :
        return "Your Car Name : %s" % self.car_name
    
    def show(self):
        print(super().show()) # 부모꺼에선 리턴문으로 받음. 리턴은 두개가 실행 될 수 없음
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')


print(model1.color) #super
print(model1.type) # super
print(model1.car_name) # sub
print(model1.show()) # super
print(model1.show_model()) # sub
print(model1.__dict__)
print()


# 메소드 오버라이딩
model2 = BenzCar("220d","suv", "black")
print(model2.show())
print(model1.show())
print()

# Parent Method Call
model3 = BenzCar("350s", "sedan", "silver")
print(model3.show())

# Inheritance Info 상속정보를 리스트 형태로 표시
print(BmwCar.mro())
print(BenzCar.mro())
print()

# 다중상속
class X(object):
    pass
class Y():
    pass
class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass
class M(B,A,Z):
    pass
print(M.mro())