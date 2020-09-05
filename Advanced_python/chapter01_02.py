# chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언

class Student(): # 모든 클래스의 부모는 object
    """
    Student class
    Author : An
    Date : 2020-09-04
    """

    # 클래스 변수
    student_count = 0
    
    def __init__(self, name, number, grade, details, email = None):
        # 인스턴스 변수(self가 붙은 변수)
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details
        self.email = email
        
        Student.student_count += 1 # 클래스가 생성 될 때 마다 1 증가
                                    # 클래스 변수에 접근할때는 클래스이름.변수이름 식으로 접근
    

    def __str__(self):
        
        return 'str {}'.format(self.name)

    def __repr__(self):

        return 'repr {}'.format(self.name)

    def details_info(self):
        print('Current id : {}'.format(id(self)))
        print('Student Details Info : {} {} {}'.format(self.name, self.email, self.details))

    def __del__(self):
        Student.student_count -= 1 



# Self의 의미

student1 = Student('An', 2, 3, {'gender':'Male', 'score1':65, 'score2': 44}, 'studen1@naver.com')
student2 = Student('Kim', 4, 1, {'gender':'Female', 'score1':85, 'score2': 44})

# ID 확인
# student1 과 student2는 서로 다른 공간에 존재
print(id(student1))
print(id(student2))


# dir & __dict__ 확인

print(dir(student1)) # dir : 모든 속성값을 보여주는 함수
print(dir(student2)) # 전체 속성값 확인할 때 사용

print()
print()

print(student1.__dict__)
print(student2.__dict__)




# Doctring
# 클래스 주석 확인(권장사항)
print(Student.__doc__)
print()

# 실행
student1.details_info()
student2.details_info()

# 에러
# Student.details_info()

Student.details_info(student1)
print()
print()
# 클래스 이름으로 접근할때는 인스턴스화된 변수를 넣어서 사용하면 직접 접근이 된다.

# 비교
print(student1.__class__,student2.__class__) # 부모 클래스를 알려줌
print(id(student1.__class__) == id(student2.__class__))

print()

# 인스턴스 변수
# 직접 접근(PEP 직접 접근을 권장 x)
# 데이터는 캡슐화를 해서 은닉해야 됨

student1.name = 'changeName'
print(student1.name)

print()
print()


# 클래스 변수

# 접근
#---> 접근은 자유롭게 할 수 있다. 왜냐하면 클래스 변수는 공용이기 때문에 가능
# 단, 인스턴스 변수는 인스턴스변수로 접근해야된다.
print(student1.student_count)
print(student2.student_count)
print(Student.student_count)


print()
print()

# 공유 확인
print(Student.__dict__)
print(student1.__dict__) # 클래스 변수가 출력되지 않음
print(student2.__dict__)

print()
print()

# (중요)
# 인스턴스 네임스페이스 없으면 상위에서 검색(파이썬이 알아서 확인)
# 즉, 동일한 이름을 변수 생성 간으(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))


del student2

print(student1.student_count)
print(Student.student_count)

print(Student.name) # 역은 성립하지 않음. 클래스에 없는데 인스턴스 변수에는 존재하더라도 출력 되지 않는다.

# 클래스는 속성과 메소드로 구성
# 속성 : 인스턴스변수, 클래스 변수
# ---> 클래스 변수 : 모든 속성을 공유
# ---> 인스턴스변수 : 할당 된 인스턴스값에서만 사용가능