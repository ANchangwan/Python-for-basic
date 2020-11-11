# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# Class 선언
class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # Generator -> 데이터가 많을 때는 Generator를 쓰는 편이 좋다.

    @property       # Getter # 데코레이터
    def x(self):
        print('Called Property X')
        return self.__x

    @x.setter # Getter을 먼저 만들어야한다. 그다음에  만든 함수에 setter을 붙어서 만든다
    def x(self,v): # 바꿀값을 매개변수로 설정한다.
        print('Called Property X')
        self.__x = v

    @property       # Getter
    def y(self):
        print('Called Property Y')
        return self.__y

    @x.setter 
    def y(self,v):
        if v < 30:
            raise ValueError('30 아래는 사용할 수 없습니다.')
        print('Called Property Y')
        self.__y = v

# 내가 의도한 클래스 구조를 회손하지 않고 사용할 수 있다.
# 값을 셋팅할 수 있다.




# 객체 선언
v = VectorP(20, 40)
#print("EX1-1 -",v.x,v.y) # __언더바 두개는 직접접근을 막아놓았다.

# 생성자 변수에 직접 접근해서  생성자 메소드의 조건을 무시하고 접근 될 수 있다.


# Getter : 삽입 
# Setter : 수정

print(v.x)


v.y = 20




# Iter 확인
for val in v:
    print("EX1-2 -", val)