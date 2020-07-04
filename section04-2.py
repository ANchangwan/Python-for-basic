# 문자형 및 연산자
# 문자열 생성, 길이
# 이스케이프 문자
# 문자열 연산
# 문자열 형 변환
# 문자열 함수
# 문자열 슬라이싱 **(중요)

# Section04 - 2


str1 = "I am Boy."
str2 = 'NiceMan'
str3 = ' '
str4 = str() #형변환 함수에 빈공간도 공백으로 본다.

print(len(str1), len(str2), len(str3), len(str4)) #len : 문자열의 길이를 구할 때 사용 

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)


# Raw String

raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인

multi =\
"""
문자열 

멀티라인 

테스트 
"""
print(multi)


# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "Niceman" # 문자열은 한번 할 당이 되면 변경 불가능

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3) # 형이 다르기 때문에 결합 할 수 없음, 단 * 연산은 가능
print( 'a' in str_o4) # str_o4가 'a' 포함됬는지 묻는다는 뜻
print( 'f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4)) # 문자열로 형변환

# 문자열 함수
# 참고 : https: // www.w3shools.com/python/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'

# print(a.islower())
# print(b.endswith('e')) # 마지막 글자가 찾고자 하는 글자인지 참, 거짓을 확인해 줌
# print(a.capitalize()) # capitalize() : 첫글자를 대문자로 바꿔줌
# print(a.replace('nice','good')) # replace() : 특정 부분을 찾아서 교체해주는 함수 
# print(list(reversed(b)))


a = 'niceman'
b = 'orange'



print(a[0:4])
print(a[0:len(a)-1])
print(a[:]) # 전체출력
print(b[0:4:2]) # 인덱스 4번 뛰어서 2번 출력
print(b[1:-2]) # 역순으로 출력
print(b[::-1]) # 역순으로 -1부터 출력











