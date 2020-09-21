# Chapter02-2
# 파이썬 심화

# 매직메소드 
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 참조1 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조2 : https://www.tutorialsteacher.com/python/magic-methods-in-python

# 매직메소드 기초 설명

# 기본형
# 파이썬은 모든 데이터구조를 객체로 받아드림
print(int)

# 모든 속성 및 메소드 출력
print(dir(int))
print()
print()

n = 100

# 사용
print('EX1-1 -', n + 200)
print('EX1-2 -',n.__add__(200))
print('EX1-3 -', n.__doc__)
print('EX1-4 -', n.__bool__(),bool(n))
print('EX1-5 -', n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    # def __str__(self):
    #     return 'Student Class Info : {}, {}'.format(self.name,self.height)

    def __ge__(self, x):
        print('Called >> __ge__Method.')
        if self.height >= x.height:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called >> __ge__Method.')
        if self.height <= x.height:
            return True
        else:
            return False

    def __sub__(self, x):
        print("Called >> __sub__Method.")
        return abs(self.height - x.height)

# 인스턴스 생성

s1 = Student('James', 181)
s2 = Student('Min', 165)

# 매직메소드 출력

print("Ex2-1 -",s1 >= s2) # self = s1 , x = s2
print("EX2-2 - ", s1<=s2)
print()
print("EX2-3 -", s1 - s2)
print("EX2-4 -", s2 - s1)
print("EX2-5 -", s1)
print("EX2-6 -", s2)

print()
print()