# Section05-2
# 파이썬 흐름제어(반복문)

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while
 # 시퀀스 타입 반복
 # continue, break
 # for - else 구문
 # 자료구조 변환


v1 = 1
while v1 < 11:
    print("v1 is : ", v1)
    v1 += 1

for v2 in range(10): # range 함수는 0부터 시작해서 값 미만까지
    print("v2 is : ", v2)

for v3 in range(1, 10):
    print("v3 is : ",v3)

# 1 ~ 100 합

sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1~100 : ', sum1 )
print('1~100 : ', sum(range(1,101)))
print('1 ~ 100 : ', sum(range(1,101, 2))) # range(시작값, 마지막값, 증가 값)

# 시퀀스(순서가 있는)자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# literable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ['kim','pakr','cho', 'choi', 'yoo']

for name in names:
    print(' you are name : ', name)


word = 'dreams'

for s in word:
    print('word : ',s)


my_info = {
    "name": "kim",
    "age" : 33,
    "city": "Seoul"
    }


for key in my_info.values():
    print("my_info : ", key)

for key in my_info.keys():
    print("my info : ", key)

for k,v in my_info.items():
    print('my_info',k,v)

name = "KennRy"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())


# break
# for - else 구문(반복문이 정상적으로  수행 된경우 esle 블럭 수행)
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 37, 15, 34, 36, 38]    

for num in numbers:
    if num == 33:
        print("found : 33!")
        break
    else:
        print("not found! : 33")    
else:
    print("not found : 33!........")

# continue

it = ["1",2,5, True, 4.3, complex(4)]

for v in it:
    if type(v) is float:
          continue
    print("타입 : ", type(v))


name = 'NiceMan'
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))