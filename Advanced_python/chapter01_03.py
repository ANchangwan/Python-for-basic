# chapter01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드(class method, instance method, static method)
# 인스턴스 메소드 -> self로 인자를 받음


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
    @classmethod
    def raise_fee(cls, per):
        if per < 1:
            print('Please Enter 1 or More')
            return 
        cls.tuition_per = per  # cls = Student 클래스 인자가 넘어옴, Class과 같음 
        print('Succed! tuition increased!') 


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