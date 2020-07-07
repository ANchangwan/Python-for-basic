# section 04 - 3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

#리스트(순서o, 중복o, 수정o, 삭제o)
# 선언

a = []
b = list() # 명시적 선언
c = [1,2,3,4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100,['Pen', 'Bnana', 'Orange']]


# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][0:3])

# 연산

print(c + d)
print(c * 3)
print(str(c[0])+'hi') #자료형이 다를 경우 형변환으로 자료형을 맞춰준다.

# 리스트 수정 , 삭제

c[0] = 77
print(c)
c[1:2] = [100 , 1000, 10000]
print(c)

c[1] = ['a','b','c']
print(c)

del c[1] # 삭제
print(c)
del c[-1]
print(c)
print()

# 리스트 함수

y = [5,2,3,1,4]
print(y)
y.append(6) # 추가함수
print(y) 

y.sort() # 정렬 함수
print(y)
y.reverse() # 역 정렬
print(y)
y.insert(2,7) # insert(인덱스, 삽입숫자)

print(y)

y.remove(2) 
y.remove(7)
print(y)


y.pop() # 마지막 값을 삭제, 
y.pop()
print(y)

ex = [88,77]
y.append(ex) 
#y.extend(ex) # append와 차이점은 extend는 값을 삽입하고 append 리스트를 삽입
print(y)



# 삭제 : del, remove, pop

# 튜플 (순서o,중복o, 수정x, 삭제x)
# 변경해서는 안되는 데이터에 사용

a = ()
b = (1, )
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(c[2])
print(c[3])
print(d[2][1])


print(d[2:])
print(d[2][0:2])


print(c + d)

print(c * 3)
print()
print()


# 튜플  함수


z = (5, 2, 1, 3, 4,1)
print(z)
print(3 in z)
print(z.index(3)) # 찾고자하는 인덱스 반환
print(z.index(5))
print(z.count(1))
