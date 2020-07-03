# 데이터 타입
# int 정수
# Float 실수
# String 문자열
# list 배열
# bool 참, 거짓
# complex : 복소수
# set : 집합 
# dict : 사전
# tuple : 튜플(시퀀스)






v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age " : 25
}
v_list= [3, 5, 7]
v_tuple = 3, 5, 7
v_set ={7, 8, 9}

print(type(v_tuple)) #type 어떤 자료형인지 알려준다.
print(type(v_set))
print(type(v_float))
print(type(v_str1))
print(type(v_int))
print(type(v_list))
print(type(v_str2))
print(type(v_dict))



i1 = 39
i2 = 939
big_int1 = 999999999999999999999999999999999999999999999
big_int2 = 777777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5 # =0.5
f4 = 10. # =10.0

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2) #자동으로 형변환

result = f3 + i2

print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b
print(result2, type(result2))

# 형변환
# int, float, complex(복소수)

print(int(result2), type(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))


y = 100
y +=100
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7)) # 절대값
n, m = divmod(100, 8)

print(n,m)

import math

print(math.ceil(5.1))
print(math.floor(5.456))