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

    @y.setter 
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
print('EX1-2 -', dir(v), v.__dict__)
print('EX1-3 -', v.x, v.y)







# Iter 확인
for val in v:
    print("EX1-4 -", val)


# __slot__
# 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕션너리 대신 Set 형태를 사용
# __slot__이 더 빠르다


class TestA(object):
    __slots__ = ('a',)

class TestB(object):
    pass

use_slot = TestA()
no_slot = TestB()

print('EX2-1 -', use_slot)              
#print('EX2-2 -', use_slot.__dict__)    # dic 대신 set를 사용하기 때문에 에러 발생
print('EX2-3 -', no_slot)
print('EX2-4 -', no_slot.__dict__)

# 메모리 사용량 비교
from random import Random
import timeit

# 측정을 위한 함수 선언

def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a
    return repeat_inner


print(min(timeit.repeat(repeat_outer(use_slot), number =1000)))
print(min(timeit.repeat(repeat_outer(no_slot), number =1000)))

print()
print()

# 객체 슬라이싱

class ObjecS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]
    
    def __len__(self):
        return len(self._numbers)
    
    def __getitem__(self, idx):
        return self._numbers[idx]

s = ObjecS()

print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s))
print('EX3-3 -', len(s._numbers))
print('EX3-4 -',s[1:100])
print('EX3-5 -', s[-1])
print('EX3-6 -', s[::10])


print()
print()

# 파이썬 추상클래스
# 참고 : http: // docs.python.org/3/library/collections.abc.html

# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스 생성해야 함
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것


# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contain__  기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜


class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

i1 = IterTestA()

print('EX4-1 -', i1[4])
print('EX4-2 -', i1[4:10])
print('EX4-3 -', 3 in i1[1:10])
# print('EX4-4 -',[i for i in i1])

print()
print()

# Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작

from collections.abc import Sequence

class IterTestB(Sequence): # 부모 : Sequence
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)
    
    def  __len__(self, idx):
        return len(range(1, 50, 2)[idx])


i2 = IterTestB()
print('EX4-5 -', i2[4])
print('EX4-6 -', i2[4:10])
print('EX4-7 -', 3 in i2[1:10])


print()
print()



# abc 활용 예제

import abc

class RandomMachine(abc.ABC): # metaclass=abc.ABCMeta(3.4 이하)
    # __metaclass__ = abc.ABCMeta

    # 추상 메소드
    @abc.abstractclassmethod
    def load(self, iterobj):
        '''Iterable 항목 추가'''


    # 추상 메소드
    @abc.abstractclassmethod
    def pick(self, iterobj):
        '''무작위 항목 뽑기'''
    
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))


import random

class CraneMachine(RandomMachine):
    def __init__(self, items) -> None:
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty crane Box')
    
    def __call__(self):
        return self.pick()


# 서브 클래스 확인
print('EX5-1 -', issubclass(RandomMachine, CraneMachine))
print('EX5-2 -', issubclass(CraneMachine, RandomMachine)) # issubclass(자식, 부모) 


# 상속 구조 확인
print('EX5-3 -', CraneMachine.__mro__)

cm = CraneMachine(range(1, 100)) # 부모클래스에 추상 메소드는 반듯이 자식클래스에 구현해야 한다.
                                 # 추상 메소드는 구현 안하면 에러

print('EX5-4 -', cm._items)
print('EX5-5 -', cm.pick())
print('EX5-6 -',cm())
print('EX5-6 -', cm.inspect()) # 자식메소드에 없지만 부모클래스에 있으면 실행가능하다.


# Private 속성 -> @property  데코라이터 이용해서 은닉 가능 직접접근해서 수정을 막을 수 있음
#__slot__
# 객체슬라이싱, 인덱싱 :