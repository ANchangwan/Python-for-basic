# chapter01-1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 일반적인 코딩

# 학생 1
student_name_1 = 'kim'
student_number_1 = 1
student_grade_1 = 1
student_detail_1 = [
{'gender' : 'Male'},
{'score1':95},
{'score2':88}

] 

# 학생 2
student_name_2 = 'Lee'
student_number_2 = 2
student_grade_2 = 2
student_detail_2 = [
{'gender' : 'Male'},
{'score1':77},
{'score2':92}

] 

# 학생 3
student_name_3 = 'Park'
student_number_3 = 3
student_grade_3 = 4
student_detail_3 = [
{'gender' : 'Male'},
{'score1':99},
{'score2':100}

] 

# 리스트 구조

# 단점
# 관리하기 불편
# 데이터의 정확한 위치(인덱스) 매핑 해서 사용
student_names_list = ['kim', 'Lee','Park']
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 4]
student_details_list = [
    {'gender' : 'Male','score1':95,'score2':88},
    {'gender' : 'Female','score1':77,'score2':92},
    {'gender':'male','score1':99, 'score2': 100}
]


# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print (student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)


print()
print()


# 딕셔너리 구조
# 단점
# 코드 반복 지속, 중첩 문제

students_dicts = [
    {'student_name': 'Kim', 'student_number':1, 'student_grade': 1, 'student_detail':{'gender':'Male','score1':95,'score2':88}},
    {'student_name': 'Lee', 'student_number':2, 'student_grade': 2, 'student_detail':{'gender':'Female','score1':77,'score2':92}},
    {'student_name': 'Park', 'student_number':3, 'student_grade': 4, 'student_detail':{'gender':'Male','score1':99,'score2':100}}
]

del students_dicts[1]
print(students_dicts)