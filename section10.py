# Section 10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실해(런타임)프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('Test)
#if True
#    pass
# x =>y

# NameError : 참조변수 없음

a = 10
b = 15

#print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)


# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3]) #예외 발생


# KeyError

dic = {'name': 'kim', 'Age': 33, 'City': 'Seoul'}
#print(dic['hobby'])
print(dic.get('hobby'))


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
# print(time.month())

# ValuError : 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)

# FileNotFoundError

#f = open('test.txt','r') # 예외발생 
 

# TypeError
x = [1,2]
y = (1,2)
z = 'test'
# print(x + y) # 예외
# print(x + z)

print(x + list(y)) # 예외


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행


# 예제3

name = ['Kim', 'Lee','Park']

try:
    z='kim' # cho 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x+1))
except ValueError: # 어떤 에러가 발생할지 모를 때는 except로 두기
    print('Not found it! - Occurred ValueError')
else: # 정상적인 실행만 수행
    print('Ok! else')
finally: # 에러가 발생하든 안하든 상관없이 실행
    print('finally ok!')

# 예제4

# 예외처리는 하지 않지만 , 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok Finally!!!!')


# 예제5
try:
    z='kim' # cho 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l: # 어떤 에러가 발생할지 모를 때는 except로 두기
    print('Not found it! - ValueError Error')
    print(l) # Alianc를 줄수도 있음
except IndexError: 
    print('Not found it! - IndexError Error')
except Exception: # Exception은 항상 마지막으로 코딩해야됨. 왜냐하면 첫번째로 하면 모두 Exception 구문에서 처리함
                   # 순서대로 except를 해야됨
    print('Not found it! - Occurred Error')        
else: # 정상적인 실행만 수행
    print('Ok! else')
finally: # 에러가 발생하든 안하든 상관없이 실행
    print('finally ok!')


# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = '333'
    if a == 'Kim':
        print('ok 허가!')
    else:
        raise ValueError # 예외를 직접 규정

except ValueError:
    print('문제발생!')
except Exception as f:
    print(f)
else:
    print("ok!")

# Exception 클래스 상속을 이용한 예외처리

class MyError(Exception): # 예외처리 메시지를 만들 수 있음
    def __str__(self):
        return '오류가 발생했습니다.'

def say_nick(nick):
    if nick == 'hi':
        raise MyError()
    print(nick)


try:
    say_nick('hello')
    say_nick('hi')

except MyError as e:
    print(ellipsis)



