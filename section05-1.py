# section05-1
# 파이썬 흐름제어(제어문)
# 조건문 실습

print(type(True))
print(type(False))

# 예1
if True:
    print("Yes")

# 예2
if False:
    print("no")

 # 예3
if False:
    print("no")
else:
    print("Yes2")

# 관계연산자
# >,>=, <,<=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print()
# 참 거짓 종류(True, False)
# 참 : "내용", [내용], (내용), {내용}, 1, True
# 거짓 : "", [], (), {}, 0, False

city = "1"

if city:
    print(">>>>True")
else:
    print(">>>>False")

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print('and : ', a > b and b >c)
print('or : ', a > b or c > b)
print('not : ', not a > b) # not 값의 반대
print(not False)
print(not True)

# 산수, 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용

print('ex1 : ', 5 + 10 >0 and not 7 + 3 == 10)

score1 = 90
score2 = 'A'

if score1 >=90 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("불합격입니다.")

# 다중 조건문

num =82 

if num >=90:
    print("num 등급 A", num)
elif num>=80:
     print("num 등급 B", num)
elif num >= 70:
     print("num 등급 c", num)
else:
    print("꽝")

# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height>=170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능")