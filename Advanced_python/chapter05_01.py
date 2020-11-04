#chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

print("Ex1-1 -")
print(dir())

# id vs __eq__(==) 증명

x = {'name': 'kim', 'age':33, 'city':'Seoul'}
y = x

print('EX2-1 -',id(x), id(y)) # 얕은 복사
print('EX2-2 -', x == y)
print('EX2-3 -', x is y)
print('EX2-4 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y)

z = {'name': 'kim', 'age':33, 'city':'Seoul','class' : 10}

print('EX2-6 -', x, z)
print('EX2-7 -', x is z)       # 같은 객체
print('EX2-7 -', x is not z)
print('EX2-7 -', x == z)        # 값이 같다

# 객체 생성 후 완전 불편 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__)는 값 비교

print()
print()

# 튜플 불변형의 비교

tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100,1000])
 
print('EX3-1 -', id(tuple1), id(tuple2)) # 별개의 객체
print("EX3-2 -", tuple1 is tuple2)
print("EX3-3 -", tuple1 == tuple2)
print("EX4-4 -", tuple1.__eq__(tuple2))


print()
print()

# Copy, Deepcopy(깊은 복사, 얕은 복사)

# Copy

tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -',tl1 == tl2)
print('EX4-2 -',tl1 is tl2)
print('EX4-3 -',tl1 == tl3)
print('EX4-4 -',tl1 is tl3)

