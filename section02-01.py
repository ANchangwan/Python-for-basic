# Section02 - 1
# 파이썬 기초 코딩
# Print  구문의 이해

#기본 출력

print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print() #프린트 함수는 안에 아무것도 없을 때 프린트 함수라고 한다.

# Separator 옵션 사용
print('T','E','S','T',sep='')
print('2019','02','19',sep='-') # sep 문자 사이에 공백의 내용을 삽입해준다.
print('niceman','google.com',sep=' @ ')

#end 옵션 사용
print('Welcome To', end=' ')
print('the black parade', end=' ') # end는 끝부분을 다음 문장과 연결해준다.
print(' piano notes')

print("Test")

print()


#format함수
# format 옵션 사용 # 개발할 때 많이 사용 (중요)

# 문자열의 대괄호 안에 함수 format을 이용해서 대괄호에  하나씩 삽입할 수 있다.
# 문자열의 대괄호 보다  함수 format이 많아도 에로가 발생하지 않는다. example)print('{}'.format(1,2))
# 문자열의 대괄호가 format보다 많으면 에러가 발생한다. example) print('{} {}'.format(1,2))-->에러

print('{} and {}'.format('you','me'))
print("{0} and {1} and {0}".format('you','me'))
print("{a} are {b}".format(a='you',b='me'))


print("%s's favorit number is %d" %('changwan',7))

print()
print()

welcome = '안녕하세요'
name = '안창완'
age = '26'
base = '이름 : {}, 나이 : {} '

print('나이 : ',age,'이름 : ',name)
print(base.format(name,age))
print('나이 : {}, 이름 : {}, {}'.format(age,name,welcome))

print("{} ".format(age,name,welcome))

print("Test1: %5d, price: %4.2f" %(776,6534.123))
print('Test1: {0: 5d}, price: {1: 4.2f}'.format(776,6534.123))
print('Test: {a:5d}, price : {b: 4.2f}'.format(a=776,b=1234.488))

