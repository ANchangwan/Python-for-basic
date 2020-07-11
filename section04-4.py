#section 04 -4
# 파이썬 데이터 타입(자료형)
#딕셔너리, 집합 자료형

#딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (json) -> MongoDB
#선언

#순서와 상관없이 출력

a = {'name' : 'kim', 'phone' : '010 - 0000 - 0000','birth' : 950204} #key : name, phone,birth... # value(값) : kim, 010-0000-0000, 950204
# key는 중복이 안되지만  value(값)은 중복 가능하고 순서 또한 상관없다.
#key는 숫자로 사용 가능하지만 보통 의미있는 이름의 키값을 사용한다.

b = {0:'Hello Python', 1 : 'Hello Coding'}
c = {'arr':[1,2,3,4,5]}
# 어떠한 데이터값도 사용가능
# 값으로 리스트,튜플도사용가능

# print(type(a))

# 출력
print(a['name']) # key 값으로 조회

# 없는 key 값으로 조회하면 에러발생
# 오류 발생을 막기 위해서 Get함수 사용

print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

# 딕셔너리 추가

a['address'] = 'seoul'
print(a)
a['rank'] = [1,2,3,4,5]
print(a)
a['rank2'] =(1,2,3,)
print(a)

# keys, values, item(keys,values의 한쌍)
print()
print(a.keys()) # key들의 모음을 리스트 형태로 출력 # 리스트 형태로 출력을 할 수 없음
# 리스트로 형변환을 해서 출력을 해야한다.
print(list(a.keys()))

temp = list(a.keys())
print(temp[0:3])


print(a.values())
temp = list(a.values())
print(temp[1:3])

print(a.items())
print(list(a.items())) # 리스트 형변환이 가능하고 튜플의 형태로 반환
print(1 in b)
print('name' in a)

# 집합(sets) 순서o, 중복x
a = set()
b = set([1,2,3,4])
c = set([1,4,6,6])

print(type(a))
print(c) # 집합은 중복을 허용하지 않기 때문에 중복된 값은 출력하지 않는다.

# 집합은 리스트와 튜플로 변환해서 슬라이싱 사용 가능

t = tuple(b)
print(t)
t = list(b)
print(t)
print()
print()

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9,10])
print(s1.intersection(s2)) # 교집합 함수
# Or

print(s1 & s2)

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합

print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7,8,9,15])

s3.add(18)
s3.add(7)
print(s3)
print( 15 in s3)
s3.remove(15)
print(s3)


print(type(s3))
