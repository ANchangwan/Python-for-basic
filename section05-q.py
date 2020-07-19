# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for v in q1.keys():
    if v =='가을':
        print("q1 : ",q1[v])

for v,s in q1.items():
    if v == '가을':
        print("q1 : ",s)


print()

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for v in q2.values():
    if v == "사과":
        print("q2 : %s가 포함돼어있습니다." %v)
        break # 사과 있으면 else문이 수행이 안되고 없으면 수행됨
else:
    print("사과 없음")




# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

q3 = 77

if q3 >=81:
    print("A학점")
elif q3 >=61:
    print("B학점")
elif q3 >=41:
    print("C학점")
elif q3 >=21:
    print("D학점")
elif q3 >= 0 :
    print("E학점")        


# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
q4 = [12 , 6, 18]
max=0

for v in q4:
    if v>max:
        max=v
        
print("가장 큰수 : ", max)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
s = '891022-2473837'
if int(s[7]) % 2 == 1:
    print("남자")
else:
    print("여자")    

# 6 ~ 10 반복문 사용(while 또는 for)

q6=6
while q6<=10:
    print("q6 : ",q6)
    q6+=1
    

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:    
    if v!='정':
        print("%s" %v,end='')
    
print()

q5 = [x for x in q3 if x !='정']
print(q5)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

q7 = 0
while q7<100:
    q7+=1
    if q7%2 != 0:
        print(q7,end=',')
print()
print('-'*50)
q5 = [x for x in range(1,101) if x%2 != 0]
print(q5)


# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for i in q4:
    if len(i)>=5:
        print(i)


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q5:
    if i.islower():
        print(i)


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q6:
    if i.isupper() == True:
        print("소문자 :", i.lower())
        
for i in q6: 
    if i.islower() == True:
        print("대문자 : ", i.upper())


# 리스트 컴프리헨션


# 일반적이 방법
numbers = []

for n in range(1, 101):
    numbers.append(n)

print(numbers)

print()

numbers2 = [x for x in range(1,101)]
print(numbers2)
