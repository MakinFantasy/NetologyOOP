class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def students_grade_count(self):
        average_grade = 0
        list_length = 0
        for key, value in self.grades.items():
            for el in value:
                average_grade += el
            list_length += len(value)
        result = 0
        if list_length != 0:
            result = average_grade / list_length
        return result

    def __str__(self):
        self.students_grade_count()
        result = f"""Имя: {self.name}\nФамилия: {self.surname}\nСр.оценка за д.з.: {self.students_grade_count()} \
        \nИзучаемые курсы:{",".join(self.courses_in_progress)}\
        \nЗавершенные курсы: {",".join(self.finished_courses)}"""
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка, указанное имя не найдено в списке студентов.")
            return 0
        return self.students_grade_count() < other.students_grade_count()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lecturer_grades_count(self):
        average_grade = 0
        list_length = 0
        for key, value in self.grades.items():
            for el in value:
                average_grade += el
            list_length += len(value)
            result = 0
            if list_length != 0:
                result = average_grade / list_length
        return result

    def __str__(self):
        self.lecturer_grades_count()
        result = f"Имя: {self.name}\nФамилия: {self.surname}\nСр.оценка за лекции:{self.lecturer_grades_count()}"
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка: Данное имя не обнаружено в списке лекторов")
            return
        return self.lecturer_grades_count() < other.lecturer_grades_count()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and (course in student.courses_in_progress or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}"
        return result





student_1 = Student('Mike', 'Vazovsky', 'man')
student_1.finished_courses.append('Git')
student_1.courses_in_progress += ['Python']



student_2 = Student('Iron', 'Man', 'man')
student_2.finished_courses.append('Git')
student_2.courses_in_progress += ['Python']


lecturer_1 = Lecturer('Oleg', 'Buligin')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Anna', 'Batitskaya')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Nikita', 'Galkin')
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Git', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
print(reviewer_1)

reviewer_2 = Reviewer('Ura', 'Zheltyakov')
reviewer_2.rate_hw(student_1, 'Git',10)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)

student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Git', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'Git', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 9)


student_2.rate_lecturer(lecturer_1, 'Git', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Git', 10)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Git', 7)
student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Git', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 9)

student_1.students_grade_count()
print(student_1)

student_2.students_grade_count()
print(student_2)

print(student_1 < student_2)

print(lecturer_1)

print(lecturer_2)

print(lecturer_1 < lecturer_2)


def student_average_grading(students, course):
    grade_sum = 0
    grade_num = 0
    result = 0
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                grade_num += len(value)
                for el in value:
                    grade_sum += el
    if grade_num !=0 :
        result = grade_sum / grade_num
    return result


def lecturer_average_grading(lecturer, course):
    grade_sum_lc = 0
    grade_num_lc = 0
    result = 0
    for lectur in lecturer:
        for key, value in lectur.grades.items():
            if key == course:
                grade_num_lc += len(value)
                for el in value:
                    grade_sum_lc += el
    if grade_num_lc != 0:
        result = grade_sum_lc / grade_num_lc
    return result


student_list = [student_1, student_2]
c_n = 'Git'
av_gr = student_average_grading(student_list, c_n)
print(f"Средняя оценка по курсу 'Git': {av_gr}")


student_list_2 = [student_1, student_2]
c_n_2 = 'Python'
av_gr_2 = student_average_grading(student_list_2, c_n_2)
print(f"Средняя оценка по курсу 'Python': {av_gr_2}")

lecturer_list = [lecturer_1, lecturer_2]
c_n_lc = 'Python'
av_gr_lc = lecturer_average_grading(lecturer_list, c_n_lc)
print(f"Средняя оценка лекторов по курсу 'Python': {av_gr_lc}")

lecturer_list_2 = [lecturer_1, lecturer_2]
c_n_lc_2 = 'Git'
av_gr_lc_2 = lecturer_average_grading(lecturer_list_2, c_n_lc_2)
print(f"Средняя оценка лекторов по курсу 'Git': {av_gr_lc_2}")




