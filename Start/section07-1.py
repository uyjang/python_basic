# 파이썬 클래스 상세 이해
# self, 클래스, 인스턴스 변수

# 클래스와 인스턴스의 차이(중요)
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재 (park,kim 따로), 인스턴스 생성 후 사용(user1,user2)


# 선언

# class  클래스명:
#     함수
#     함수
#     함수

# 예제1
class UserInfo : # 클래스의 이름은 첫글자 대문자, 단어와 단어를 연결할 때도 대문자
    # 속성, 메소드(동작과 관련)
    def __init__(self, name, height, weight, address) : # 클래스 최초 초기화 할 때 꼭 필요한 함수
        self.name = name
        self.height = height
        self.weight = weight
        self.address = address
    def user_info_p(self):
        print("Info : ", self.name,self.height,self.weight,self.address)
 
user1 = UserInfo("Kim", 175, 73, "경기도")
user1.user_info_p()
user2 = UserInfo("Park", 180, 80, "경상도")
user2.user_info_p()

# 예제2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print('function2 callde!')
self_test = SelfTest()
SelfTest.function1() # 클래스 메소드
self_test.function2()  # 인스턴스 메소드
SelfTest.function2(self_test) # 인스턴스 메소드 호출방법2

# 예제 3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스는 공유한다. 즉 자기 네임스페이스에 없으면 클래스에 가서 찾는다.

del user1