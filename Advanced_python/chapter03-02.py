# Chapter03-2
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, set -> 중복 허용 x
# Dict 및 Set 심화

# Dict 구조
print('EX1-1 -')
# print(__builtins__.__dict__)


print()
print()

# Hash 값 확인
t1 = (10, 20, (30,40, 50))
t2 = (10, 20, [30,40, 50]) # 리스트는 값을 변경할 수 있기 때문에 해쉬값 생성 불가능

print('EX1-2 -', hash(t1))
# print('EX1-3 -', hash(t2))

print()
print()

# 지능형 딕셔너리(Comprehending Dict
import csv

# 외부 CSV TO lIST of tuple

# with open('./resources/test1.csv', 'r',encoding='UTF-8') as f:
#     temp = csv.reader(f)
#     # Header Skip
#     next(temp)
#     #변환
#     NA_CODES = [tuple(x) for x in temp]

print('EX2-1 -',)
# print(NA_CODES)

# n_code1 = {country: code for country, code in NA_CODES}
# n_code2 = {country.upper() : code for country,code in NA_CODES}

print()
print()

print('EX2-3 -',)
# print(n_code2)

# Dict Setdefault 예제
# 딕셔너리는 키 중복이 안됨


source = (('k1', 'val1'),
            ('k1','val2'),
            ('k2','val3'),
            ('k2','val4'),
            ('k2','val5')
)

new_dict1 = {}
new_dict2 = {}

# No use setdefault
for k,v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print('EX3-1 -', new_dict1)


# Use setdefault
for k,v in source:
    new_dict2.setdefault(k,[]).append(v)

# 사용자 정의 dict 상속(UserDict 가능)

class UserDict(dict):# 딕셔너리 상속
    def __missing__(self,key):
        print('Called : __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called : __getitem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print('Called : __contains__')
        return key in self.keys() or str(key) in self.keys()


user_dict1 = UserDict(one=1,two=2)

user_dict2 = UserDict({'one':1,'two':2})

user_dict3 = UserDict([('one',1),('two',2)])



print()
print()


# 출력
print('EX4-1 -',user_dict1, user_dict2,user_dict3)
print('EX4-2 -',user_dict2.get('two'))
print('EX4-3 -', 'one' in user_dict3)
# print('EX4-4 -',user_dict3['three'])
print('EX4-5 -',user_dict3.get('three'))
print('EX4-5 -','three' in user_dict3)

print()
print()


# immutable Dict
from types import MappingProxyType

d = {'key1': 'TEST1'}

# Read Only
d_frozen = MappingProxyType(d) # MappingProxyType -> 수정 불가

print('EX5-1 -', d, id(d))
print('EX5-2 -', d_frozen, id(d_frozen))
print('EX5-3 -', d is d_frozen, d == d_frozen) # is -> id값이 같은지 판단, == -> 값(key,value)이 같은지 판단

# 수정 불가
# d_frozen['key1'] = 'TEST2'

d['key2'] = 'TEST2' # 원본은 수정 가능

print('EX5-4 -', d)


# Set 구조(FrozenSet)


print()
print()

s1 = {'Apple','Orange', 'Apple','Orange','Kiwi'}

s2 = set(['Apple','Orange', 'Apple','Orange','Kiwi'])

s3 = {3}
s4 = set() # Not {} 빈 set은 불가능
s5 = frozenset(['Apple','Orange', 'Apple','Orange','Kiwi']) # add 함수 사용 불가

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print('EX6-1 -', s1, type(s1)) # 순서가 유지되지 않음 # 중복 배제 # 잘못 사용하면 속도가 느려짐
print('EX6-1 -', s2, type(s2))
print('EX6-1 -', s3, type(s3))
print('EX6-1 -', s4, type(s4))
print('EX6-1 -', s5, type(s5))


# 선언 최적화

from dis import dis

print('EX6-5 -')
print(dis('{10}'))

print('EX6-6 -')
print(dis('set([10])'))

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name

print('EX7-1 -')

print({name(chr(i), '') for i in range(0,256)})

# 시퀀스형 설명
# 1) Dict Comprehension
# 2) Hashtable
# 3) setDefault
# 4) User Defined Dictionary
# 5) Immutable Dict
# 6) Set vs Frozenset



