class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calculate_av_grade(self):
        if self.grades:
            grade_sum = 0
            counter = 0
            for val in self.grades.values():
                grade_sum += sum(val)
                counter += len(val)
            return grade_sum/counter
        else:
            return 0

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \n'
                +f'Средняя оценка за домашние задания: {self.calculate_av_grade()} \n'+
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'+
                f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
    def __lt__(self, other):
        return self.calculate_av_grade() < other.calculate_av_grade()
    def __gt__(self, other):
        return self.calculate_av_grade() > other.calculate_av_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades ={}

    def rate_hw(self, student, course, grade):
        pass

    def calculate_av_grade(self):
        if self.grades:
            grade_sum = 0
            counter = 0
            for val in self.grades.values():
                grade_sum += sum(val)
                counter += len(val)
            return grade_sum/counter
        else:
            return 0

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} \n'
                +f'Средняя оценка за лекции: {round(self.calculate_av_grade()),2}\n')

    def __lt__(self, other):
        return self.calculate_av_grade() < other.calculate_av_grade()
    def __gt__(self, other):
        return self.calculate_av_grade() > other.calculate_av_grade()

class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java']

second_best_student = Student('Bim', 'Lan', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Java']

best_lecturer = Lecturer('Jon', 'Snow')
best_lecturer.courses_attached += ['Python']

second_best_lecturer = Lecturer('Jan', 'Sok')
best_lecturer.courses_attached += ['Python']


best_reviewer = Reviewer('Вася', 'Пупкин')
second_best_reviewer = Reviewer('Маня', 'Чашкина')

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 6)
cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(second_best_student, 'Python', 3)
# cool_mentor.rate_hw(second_best_student, 'Python', 5)
# cool_mentor.rate_hw(second_best_student, 'Python', 10)
best_student.rate_lec(best_lecturer,'Python', 5)
best_student.rate_lec(best_lecturer,'Python', 2)
best_student.rate_lec(best_lecturer,'Python', 10)
# second_best_student.rate_lec(best_lecturer,'Python', 5)
# second_best_student.rate_lec(best_lecturer,'Python', 2)
# second_best_student.rate_lec(best_lecturer,'Python', 10)

if best_student > second_best_student:
    print(f'Лучший студент \n{best_student}')
else:
    print(f'Лучший студент \n{second_best_student}')

if best_lecturer > second_best_lecturer:
    print(f'Лучший лектор \n{best_lecturer}')
else:
    print(f'Лучший лектор \n{second_best_lecturer}')

students =[]
lecturers =[]
students+=[best_student, second_best_student]
lecturers+=[best_lecturer, second_best_lecturer]

def av_grade_students(students, course):
    if students != 0:

        grades =[]
        for s in  students:
            if course in s.courses_in_progress and s.grades[course] != 0:
                grades += [sum(s.grades[course])/len(s.grades[course])]
        return sum(grades)/len(students)
    else:
        return 0
def av_grade_lecturers(lecturers, course):
    if lecturers != 0:
        grades =[]
        for l in  lecturers:
            if course in l.courses_attached and l.grades[course] != 0:
                grades += [sum(l.grades[course])/len(l.grades[course])]
        return sum(grades)/len(lecturers)
    else:
        return 0

# print(best_student.grades)
print("********************")
print(f'Студент\n{best_student}')
print(f'Лектор\n{best_lecturer}')
print(f'Ревьювер\n{best_reviewer}')
print(f'Студент\n{second_best_student}')
print(f'Лектор\n{second_best_lecturer}')
print(f'Ревьювер\n{second_best_reviewer}')
print("**************************")
print(f'Средняя оценка среди студентов: {round(av_grade_students(students,"Python")),2}')
print(f'Средняя оценка среди лекторов: {round(av_grade_lecturers(lecturers,"Python")),2}')