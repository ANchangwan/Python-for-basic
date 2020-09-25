# chapter03-1
# 파이썬 심화
# 시퀀스 형
# 컨테이너(Container) : 서로 다른 자료형 [list, tuple, collections.deque]
# Flat : 한 개의 자료형[str, byte, bytearray, array.array, memoryview] # 여러 자료형을 넣는거보다 한 개의 자료형이 성능이 더 좋다.
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes


# 지능형 리스트(Comprehending Lists)

# Non Comprehending Listsord

chars = '@#$@%#$@#^'
codes1 = []

for s in chars:
    if int(ord(s)) >= 40:
        codes1.append(ord(s))

# Comprehending Lists
codes2 = [ord(s) for s in chars] # 성능이 더 우세함

# Comprehending Lists + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) >= 40]
codes4 = list(filter(lambda x: x > 40,map(ord, chars)))

print('EX1-1 -', codes1) # 리스트로 변환
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)
print('EX1-5 -',[chr(s) for s in codes1 ])
print('EX1-6 -',[chr(s) for s in codes2 ])
print('EX1-7 -',[chr(s) for s in codes3 ])
print('EX1-8 -',[chr(s) for s in codes4 ])

print()
print()

# Generator

import array

# Generator : 한 번에 한개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)
# Array
array_g = array.array('I',(ord(s) for s in chars))


print('EX2-1 -',tuple_g)
print('EX2-2 -',next(tuple_g))
print('EX2-3 -',next(tuple_g))
print('EX2-4 -',array_g)
print('EX2-5 -', array_g.tolist())


# 제네레이터 예제

print('EX3-1 -',('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,11)):
    print('EX3-2 -',s)


print()
print()

# 리스트 주의 할 점

marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print('EX4-1 -',marks1)
print('EX4-2 -', marks2)

print()

marks1[0][1] = 'x'
marks2[0][1] = 'x'

print('EX4-1 -',marks1)
print('EX4-2 -', marks2)

# 증명
print('EX4-5 -', [id(i) for i in marks1])
print('EX4-5 -', [id(i) for i in marks2])