# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 공통적으로 쓸수 있는 속성을 부모로부터 물려받아서 사용하면 가독성, 유지보수, 코드 량이 줄어든다.

class Car: # 슈퍼클래스(부모)
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'


class BmwCar(Car): # 서브클래스(자식)
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # super() 부모라는 뜻
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name
        
class BenzCar(Car): # 서브클래스(자식)
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # super() 부모라는 뜻
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show()) # 부모의 메소드를 호출하고 싶을때 super(). 사용
        return 'Car Info : %s %s %s' %(self.car_name, self.type, self.color)

        


# 일반 사용
model1 = BmwCar('520d', 'sedan','red') # 변수에 넣으면 인스턴스 생성

print(model1.color) # Super
print(model1.type) # super
print(model1.car_name) #sub
print(model1.show()) #super
print(model1.show_model()) # sub
print(model1.__dict__)


# Method Overriding(오버라이딩)
model2 = BenzCar('220d','suv','black')
print(model2.show())


# Parent Method Call
model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show())

# Inheritance Info(상속 정보)
print(BmwCar.mro())
print(BenzCar.mro())


# 예제2
# 다중 상속

class X():
    pass

class Y():
    pass
class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
print(A.mro())    

# 복잡한 다중 상속은 코드를 해석하기 힘들다.

