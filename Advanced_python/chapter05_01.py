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
tl3 = list(tl1) # 새로운 객체를 카피

print('EX4-1 -',tl1 == tl2)
print('EX4-2 -',tl1 is tl2)
print('EX4-3 -',tl1 == tl3)
print('EX4-4 -',tl1 is tl3)


# 증명

tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()


# print(id(tl1[2]))
tl1[1] += [110,120]
tl1[2] += (100,120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2) # 튜플 재 할당(객체 새로 생성)
print('EX4-10 -', tl3)
# print(id(tl1[2]))
# 튜플은 새로 생성
# 리스트 안에 튜플은 넣으면 불안정하다. 변하기 때문

print()
print()


# Deep Copy

# 장바구니
class Basket:
    def __init__(self,products=None) -> None:
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)
    
    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy
basket1 =  Basket(['Apple','Bag','TV','Snack','Water'])
basket2 =  copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print('EX5-1 -',id(basket1),id(basket2),id(basket3))                        .
print('EX5-2 -',id(basket1._products),id(basket2._products),id(basket3))

print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -',basket1._products)
print('EX5-4 -',basket2._products)          
print('EX5-5 -',basket3._products)

# 얕은 복사 : 보이는 데이터타입에 복사, 같은 객체 리스트 참조
# 깊은 복사 : 참조 레퍼런스 주소까지 복사

