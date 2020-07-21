# # 클래스 선언 및 Self의 이해
# # 클래스 선언
# # 클래스 네임스페이스Self
# # 클래스, 인스턴스 변수
# # Self

# # 클래스를 사용하는 이유
# # 프로그램 덩치가 커지면 처리해야 할 메소드가 많아지기 때문에
# # 방대한 어플리케이셔을 관리하기 위해서 코드를 구조화해서 서로와의 결합을
# # 느슨하게해서 기능을 추가, 기능 개선, 유지 보수, 생산성을 높이기 위해서
# # 클래스를 사용.


# # Section07-1
# # 파이썬 클래스 상세 이해
# # Self, 클래스, 인스턴스 변수


# 클래스, 인스턴스의 차이 중요
# 클래스는 객체이고 클래스를 변수에 할당하면 인스턴스화(메모리할당) 한다고 한다.()
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용 한다.



# # 선언-
# class 클래스 명:
#     함수
#     함수 
#     함수 # 클래스와 관련있는 함수들 정의



# 예제 1
class UserInfo:
    # 속성, 메소드
    def __init__(self, name):
      self.name = name
    def user_info_p(self):
      print("Name: ",self.name)

# 네임스페이스 : 인스턴스가 가지고 있는 저장공간
user1 = UserInfo("kim") # 인스턴스 화는 할당한다는 의미
print(user1.name)
user1.user_info_p()
user2 = UserInfo("Park")
print(user2.name)
user2.user_info_p()

print(id(user1)) # id 메모리의 주소값 출력
print(id(user2))
print(user1.__dict__) # 네임스페이스출력 __dict__
print(user2.__dict__)

# 예제 2 
# self의 이해

class SelfTest():
    def function1(): # 클래스 메소드
        print("function1 called!!")
    def function2(self): # 인스턴스 메소드
        print(id(self))
        print("function1 called!!")


self_test = SelfTest()
SelfTest.function1() # self 인자가 없기 때문에 인스턴스화를 할 수 없다.
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test) # self 인자를 받아야 오류가 안생김

# self 없으면 class에서 직접 호출한다.
# 인스턴스가 있으면 self인자가 자동으로 넘어간다.

# 예제 3
# 클래스 변수(self 필요없음), 인스턴스 변수(self가 필요)

class WareHouse:
    # 클래스 변수
    stock_num = 0 # 클래스 변수는 모든 함수가 공유
     # 클래스변수는 self가 없기 때문에 직접 접근해야됨
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1
    
user1 = WareHouse("kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수 (공유) 

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # 클래스 네임스페이스에 찾고자하는 값이 없으면 클래스에서 찾음, 만약 클래스에도 없으면 에러발생
print(user2.stock_num)
print(user3.stock_num)

del user1

print(user2.stock_num)
print(user3.stock_num)







