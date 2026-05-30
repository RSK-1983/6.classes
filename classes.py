class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress:
            if not isinstance(grade, (int, float)):
                print('Оценка должна быть числом')
                return
            if grade < 0 or grade > 10:
                print('Оценка должна быть в диапазоне [0, 10]')
                return
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        if len(self.grades.values()) != 0:
            grades_list = []
            for _, values in self.grades.items():
                grades_list += values
            return sum(grades_list)/len(grades_list)
        else:
            return 0

    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {Student.average_grades(self)}
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
        Завершенные курсы: {', '.join(self.finished_courses)}
        """

    def __eq__(self, other):
        if isinstance(other, Student):
            return Student.average_grades(self) == Student.average_grades(other)

    def __lt__(self, other):
        if isinstance(other, Student):
            return Student.average_grades(self) < Student.average_grades(other)

    def __gt__(self, other):
        if isinstance(other, Student):
            return Student.average_grades(self) > Student.average_grades(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        if len(self.grades.values()) != 0:
            grades_list = []
            for _, values in self.grades.items():
                grades_list += values
            return sum(grades_list) / len(grades_list)
        else:
            return 0

    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {Lecturer.average_grades(self)}
        """

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return Lecturer.average_grades(self) == Lecturer.average_grades(other)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return Lecturer.average_grades(self) < Lecturer.average_grades(other)

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return Lecturer.average_grades(self) > Lecturer.average_grades(other)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        """


lecturer1 = Lecturer('Иван', 'Иванов')
reviewer1 = Reviewer('Пётр', 'Петров')
student1 = Student('Алёхина', 'Ольга', 'Ж')

lecturer2 = Lecturer('Михаил', 'Сидоров')
reviewer2 = Reviewer('Сергей', 'Петров')
student2 = Student('Анна', 'Иванова', 'Ж')

student1.courses_in_progress += ['Python', 'Java']
lecturer1.courses_attached += ['Python', 'C++']
reviewer1.courses_attached += ['Python', 'C++']

student2.courses_in_progress += ['Python', 'Java']
lecturer2.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Python', 'C++']

student1.rate_lecture(lecturer1, 'Python', 6)
student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 5)

reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 5)
reviewer1.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 9)


print(student1)
print(student2)
print(student1 == student2)
print(lecturer1 == lecturer2)


def average_grades(grades):
    if len(grades) != 0:
        return sum(grades) / len(grades)
    else:
        return 0


def average_rate_student(student_list, course_name):

    for student in student_list:
        if isinstance(student, Student) and course_name in student.courses_in_progress:
            print(f"""
            Имя: {student.name}
            Фамилия: {student.surname}
            Средняя оценка за домашние задания: {average_grades(student.grades[course_name])}
            Курс: {course_name}
            """)
        else:
            'Ошибка'


def average_rate_lector(lector_list, course_name):

    for lector in lector_list:
        if isinstance(lector, Lecturer) and course_name in lector.courses_attached:
            print(f"""
            Имя: {lector.name}
            Фамилия: {lector.surname}
            Средняя оценка за лекции: {average_grades(lector.grades[course_name])}
            Курс: {course_name}
            """)
        else:
            'Ошибка'


average_rate_student([student1, student2], 'Python')
average_rate_lector([lecturer1, lecturer2], 'Python')
