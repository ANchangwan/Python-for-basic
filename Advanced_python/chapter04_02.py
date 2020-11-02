# Chapter04-2
# 파이썬 심화
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# Decorator & Closure

# 파이썬 변수 범위(global)



# 예제1
def func_v1(a):
    print(a)
    print(b)

# 예외
# func_v1(5)

# 예제2

b=10 # 전역변수
def func_v2(a):
    print(a)
    print(b)

func_v2(5)

# 예제3



b=10 # 전역변수
def func_v3(a):
    print(a)
    print(b)
    b = 5
# 핵심 : 함수안에서 값이 할당 되기전에 출력 할려고 하니까 오류 발생
# 지역 변수 우선처리

#func_v3(5)

from dis import dis

print('EX1-1 -')
print(dis(func_v3))

# Closures(클로저)
# 반환되는 내부 함수에 대해서 선언된 연결을 가지고 참조하는 방식
# 반환 당시 함수 유효범위 벗어난 변수 또는 메소드에 직접 접근이 가능하다

a = 10

print("EX2-1 -",a + 10)
print('EX2-2 -', a + 100)

# 결과를 누적 할 수 없을까?
print('EX2-3 -', sum(range(1, 51)))
print('EX2-4 -', sum(range(51, 101)))

print()
print()


# 클래스 이용

class Averager():
    def __init__(self) -> None:
        self.series = []

    def __call__(self,v):
        self.series.append(v)
        print('class >>> {} / {}'.format(self.series, len(self.series)))
        return sum(self.series) / len(self.series)


# 인스턴스 생성
avg_cls = Averager()

# 누적 확인
print("EX3-1 -", avg_cls(15))
print("EX3-2 -", avg_cls(35))
print("EX3-3 -", avg_cls(40))

print()
print()

# 클로저(Closuer) 사용
# 전역변수 사용 감소
# 디자인 패턴 적용

def closure_avg1():
    # Free variable : 함수와 내부함수 사이에 공간 영역
    series = []
    # 클로저 영역
    def averager(v):
        # series = [] # check
        # 클로저 영역이 내부에서 변수를 선언하면 누적되지 않는다.
        # 주의 많이 사용하면 많은 리소스를 잡아먹음 
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager

avg_closure1 = closure_avg1()

print("EX4-1 -", avg_closure1(15))
print("EX4-2 -", avg_closure1(35))
print("EX4-3 -", avg_closure1(40))


print('EX5-1 -', dir(avg_closure1))
print()
print('EX5-2 -', dir(avg_closure1.__code__))
print()
print('EX5-3 -', avg_closure1.__code__.co_freevars) # co_freevars : 클로저 영역에 변수를 확인
print()
print('EX5-4 -', dir(avg_closure1.__closure__[0]))
print('EX5-4 -', dir(avg_closure1.__closure__[0].cell_contents))

