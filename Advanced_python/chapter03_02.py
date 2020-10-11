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

with open('./resources/test1.csv', 'r',encoding='UTF-8') as f:
    temp = csv.reader(f)
    # Header Skip
    next(temp)
    #변환
    NA_CODES = [tuple(x) for x in temp]

print('EX2-1 -',)
print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper() : code for country,code in NA_CODES}

print()
print()

print('EX2-3 -',)
print(n_code2)

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