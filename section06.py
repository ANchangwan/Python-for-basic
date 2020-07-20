# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
# code
# 함수 호출
# 함수 명

# 함수 선언 위치 중요

# 예제1
def hello(world):
    print("Hello ", world)

hello("Python!")
hello(7777)

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!!!")
print(str)

# 예제3(다중 리턴)

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)   # 다중리턴할 값을 받을 변수들의 갯수 맞추기
print(val1,val2,val3)


# 예제 4 (데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return (y1, y2, y3) #리스트 또는 튜플로 반환 가능

it = func_mul2(100)
print(it, type(it))

# 예제4
# *args, *kwargs 

def args_func(*args): # 매개변수가 몇개가 넘어올지 알수 없을때, 또는 매개변수가 몇개가 넘어오느냐에 따라 함수에 작도을 달리 할 때
    #for t in args: # *가 하나이면 가변인자를 반환해준다.(튜플 반환)
     #   print(t)                 # 다양한 매개변수를 받을때, 함수의 흐름을 바꾸는 기능
    for i,v in enumerate(args): # enumerate(변수), 인덱스 반환
        print(i,v)


args_func('kim')
args_func('kim','park')
args_func('kim','park','Lee')


# kwargs
def kwargs_func(**kwargs): # *가 두개이면 딕션너리를 반환해준다.
    #print(kwargs) # 딕션너리 형태
    for k, v in kwargs.items():
        print(k,v)

kwargs_func(name1='Kim')
kwargs_func(name1='Kim',name2='park',name3 = 'Lee')


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs): #가변은 있어도 그만 없어도 그만이기 때문에 값을 두개만 넣어도 됨
    print(arg1,arg2, args, kwargs)


example_mul(10,20)
example_mul(10,20)
example_mul(10 ,20, 'park', 'kim', age1=35, age2=45)


# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(">>>>",num)
    print("in func")
    func_in_func(num + 10000)

nested_func(10000)



