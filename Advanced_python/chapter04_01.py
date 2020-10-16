# Chapter 04-1
# 파이썬 심화
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화(실행 중 초기화 가능)
# 2. 변수 등에 할당 가능
# 3. 함수 인수 전달 가능 sorted(keys=len)
# 4. 함수 결과로 반환 가능 return funcs

# 함수 객체 예제

def factorial(n):
    
    '''Factorial Function -> n: int'''
    if n == 1:  # n < 2
        return 1
    return n* factorial(n-1)

class A:
    pass

print('EX1-1 -', factorial(10))
print('EX1-2 -', factorial.__doc__)
print('EX1-3 -', type(factorial),type(A))

print('EX1-4 -', set(sorted(dir(factorial)))- set(sorted(dir(A)))) # 함수가 가지고 있는 속성에서 클래스 속성을 빼면 남는게 함수 속성만 남음
print('EX1-5 -', factorial.__name__) # __name__ : 함수에 이름 출력 
print('EX1-6 -', factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial
# 함수를 변수에 할당해서 사용가능

print('EX2-1 -', var_func) # == factorial
print('EX2-2 -', var_func(5)) # == factorial(5)
print('EX2-3 -',map(var_func, range(1,6)))
print('EX2-4 -',list(map(var_func, range(1,6)))) # map : 함수 인자를 받아서 연속적인 이터레이터 갯수만큼 함수 실행 

print()
print()

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order Function)
# 함수 안에 함수 전달 가능
# 가독성 측면에서는 List Comprehensive
print('EX3-1 -',list(map(var_func, filter(lambda x: x % 2,range(1,6)))))
print('EX3-2 -', [var_func(i) for i in range(1, 6) if i % 2])

print()
print()


# reduce()
# reduce(함수, 순서형 자료), * 순서형 자료 : List, 문자열, 튜플


from functools import reduce
from operator import add

print('EX3-3 -', reduce(add, range(1,11))) # 누적
print('EX3-4 -', sum(range(1,11)))

# 익명 함수 (lambda)
# 가급적 주석 사용
# 가급적 함수 사용
# 주의 : 주석을 사용하지 않고 익명함수를 많이 쓰면 가독성이 떨어짐
# 일반 함수 형태로 리팩토링 권장

print('EX3-5 -', reduce(lambda x, t: x+t, range(1,11))) # add함수 부분을 lambda함수로 대체

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인



