# Section08
# 파이썬 모듈과 패키지


# 패키지 예제
# 상대 경로
# ..: 부모 디렉토리
# . : 현재 디렉토리

# 사용 1(클래스)

from pkg.fibonacci import Fibonacci # ,를 통해서 여러개를 불러올 수 있음

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title) # 인스턴스초기화 후 사용

# 사용2(클래스),권장하지 않음
from pkg.fibonacci import * # import * 는 파일 불러옴

Fibonacci.fib(500)

print("ex2 : ", Fibonacci.fib2(600))
print("ex2 : ", Fibonacci().title) # 인스턴스초기화 후 사용
print()
# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb # 이름을 바꿀 수 있음

fb.fib(500)

print("ex3 : ", fb.fib2(600))
print("ex3 : ", fb().title) # 인스턴스초기화 후 사용
print()


# 사용 4(함수)
import pkg.calculations as c

print("ex4 : ", c.add(10,100))
print("ex4 : ", c.mul(10,100))


# 사용5(함수), 권장사항(내가 필요한 함수만 호출)
from pkg.calculations import div as d
print("ex5 : ",int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))


