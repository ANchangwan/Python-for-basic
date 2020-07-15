# 1번
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))
print("-"*100)
# 2번
print("2. \t","""apple;orange;banana;lemon""")
print()
print("-"*100)
# 3번
star = '*'
print('%s' %(star*100))
print("-"*100)
# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
num4 = '30'
print("4번문제")
print("{}".format(int(num4)))
print("{}".format(float(num4)))
print("{}".format(complex(num4)))
print("{}".format(num4))
print("-"*100)
# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.

str = "niceman"
str_idx = str.index("man")
print("5. ", str[str_idx:str_idx+3])
print("5. ",str[4:])
print("-"*100)

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
str1 = 'Strawberry'

print("6. ",str1[::-1])
print("-"*100)

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"

phoneNum = "010-7777-9999"
print("7. ", phoneNum[0:3]+phoneNum[4:8]+phoneNum[9:13] )


# 정규표현식
import re
print("7. ",re.sub('[^0-9]',"",phoneNum)) 
print("-"*100)
# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
q8 ="http://daum.net"
print("8. \t", q8[7:])
# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"

q9 = "NiceMan"
print("9. 대문자", q9.upper())
print("9. 소문자", q9.lower())
print("-"*100)

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"

str3 = "abcdefghijklmn"
print("10. %s" %str3[2:5])
print("-"*100)
# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
fruit =["Banana", "Apple", "Orange"]

fruit.remove("Apple")

print(fruit)
print("-"*100)
# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)

tp = (1,2,3,4)
print(list(tp))
print("-"*100)
# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>

person = {"성인" : 100000, "청소년" : 70000, " 아동 ":30000}
print(person)
print("-"*100)
# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.

person["소아"] =0
print(person)
print("-"*100)
 # 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.

print(person.keys())
print("-"*100)
# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(person.values())