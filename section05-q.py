# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for v in q1.keys():
    if v =='가을':
        print("q1 : ", v)


print()

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for v in q2.values():
    if v == "사과":
        print("q2 : %s가 포함돼어있습니다." %v)




# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

#q3 = {'A' : 82, 'B' : 76, 'C': 55,'D':30, 'E' : 19}
#for v in q3.velus():
    #if v == q3.range(81,100):
     #   print("a학점입니다.")
    #elif v == q3.range(61,80):
     #   print('b학점입니다.')
    #elif v == q3.range(41,60):
     #   print('c학점입니다.')
    #elif v == q3.range(21,40):
     #   print('D학점입니다.')
    #elif v == q3.range(0,20):
     #   print("E학점입니다.")




# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
q4 = [12 , 6, 18]
max=0

for v in q4:
    if v>max:
        max=v
        
print("가장 큰수 : ", max)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)


# 6 ~ 10 반복문 사용(while 또는 for)

q6=6
while q6<=10:
    print("q6 : ",q6)
    q6+=1
    

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:    
    if v!='정':
        print("%s" %v)
    

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

q7 = 0
while q7<100:
    q7+=1
    if q7%2 != 0:
        print(q7)



# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for i in q4:
    if len(i)>=5:
        print(i)


# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q5:
    if i.isupper():
        print(i)


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for i in q6:
    if i.isupper() == True:
        print("소문자 :", i.lower())
        
for i in q6: 
    if i.islower() == True:
        print("대문자 : ", i.upper())