# chapter01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드(class method, instance method, static method)
# 인스턴스 메소드 -> self로 인자를 받음
# 클래스 메소드 -> 클래스변수를 인자로 받음


# 기본 인스턴스 메소드

class Student(object):
    """
    Student Class
    Author : An
    Date : 2020.09.07
    Description : Class, Static, Instance Method
    """
    # Class Variable
    tuition_per = 1.0
    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.grade = grade
        self.tuition = tuition
        self.gpa = gpa

    # Instance Method
    #  self가 있으면 인스턴스 메소드이다.
    def full_name(self):
        return '{}, {}'.format(self.first_name, self.full_name)
    
    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self.id,self.full_name(),self.email,self.grade,self.tuition,self.gpa)

    # Instance Method
    def get_fee(self):
        return 'Before Tuition -> id : {}, fee : {}'.format(self.id,self.tuition)

    # Instance Method
    def get_fee_culc(self):
        return 'After Tuition -> id: {}, fee : {}'.format(self.id,self.tuition * Student.tuition_per)

    
    def __str__(self):
        return 'Student Info ->name : {} grade: {} email: {}'.format(self.full_name(),self.grade,self.email)
    
    # Class Method
    # Class Method가 받는 인자는 클래스 자체를 받음
    # 클래스변수에도 접근가능, 클래스를 생성할 수 있는 인스턴스할 수있고 로직을 만들 수 도 있다.
    # 권장방식 : 의미전달을 확실하게 해줄 수 있기 때문
    # cls = class Student
    @classmethod
    def raise_fee(cls, per):
        if per < 1:
            print('Please Enter 1 or More')
            return 
        cls.tuition_per = per  # cls = Student 클래스 인자가 넘어옴, Class과 같음 
        print('Succed! tuition increased!') 

    # Class Method
    @classmethod
    def student_cont(cls,id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    # Static Method
    # 공통적으로 사용하고 싶을 때 사용
    # static으로 할 수 있는건 인스턴스로 할 수 있고 클래스로도 사용할 수 있음
    @staticmethod
    def is_scholarship_st(inst):
        if inst.gpa >= 4.3:
            return '{} is a scholarship recipient.'.format(inst.last_name)
        return 'Sorry. Not a scholarship recipient'    


# 학생 인스턴스
student_1 = Student(1, 'Kim','Sarang','student1@naver.com','1', 400, 3.5)
student_2 = Student(2, 'Lee', ' Myungho','student2@naver.com','2', 500, 4.3)

# 기본정보
print(student_1)
print(student_2)

# 전체 정보
print(student_1.detail_info())
print(student_2.detail_info())


# 학비 정보(인상 전)
print(student_1.get_fee())
print(student_2.get_fee())

print()

# 학비 인상(클래스 메소드 미사용)
# Student.tuition_per = 1.2 # 직접 접근 해서 수정은 좋지 않음 
                          # 캡슐화해야됨


# 학비 인상(클래스 메소드 사용) 
Student.raise_fee(1.5)

# 학비 정보(인상 후)
print(student_1.get_fee_culc())
print(student_2.get_fee_culc())

# 클래스 메소드 인스턴스 생성 실습
# 의미 전달이 확실해서 권장
student_3 = Student.student_cont(3, 'Park','Minji','Student3@gmail.com','3', 550, 4.5)
student_4 = Student.student_cont(4, 'Cho','Sunghan','Student4@gmail.com','4', 600, 4.1)

# 전체 정보

print(student_3.detail_info())
print(student_4.detail_info())
print()

# 학생 학비 변경 확인
print(student_3.tuition)
print(student_4.tuition)
print()

# 장학금 혜택 여부(스테이틱 메소드 미사용)
# inst => 인스턴스 변수 삽입
def is_scholarship(inst):
    if inst.gpa >= 4.3:
        return '{} is a scholarship recipient.'.format(inst.last_name)
    return 'Sorry. Not a scholarship recipient'


# 함수로 접근
print(is_scholarship(student_1))
print(is_scholarship(student_2))
print(is_scholarship(student_3))
print(is_scholarship(student_4))

print()

# 장학금 혜택 여부(스테이틱 메소드 사용)
# 클래스로 접근
print(Student.is_scholarship_st(student_1))
print(Student.is_scholarship_st(student_2))
print(Student.is_scholarship_st(student_3))
print(Student.is_scholarship_st(student_4))

print()

# 인스턴스 변수로도 사용가능
# 인스턴스로 접근
print(student_1.is_scholarship_st(student_1))
print(student_1.is_scholarship_st(student_2))
print(student_1.is_scholarship_st(student_3))
print(student_1.is_scholarship_st(student_4))