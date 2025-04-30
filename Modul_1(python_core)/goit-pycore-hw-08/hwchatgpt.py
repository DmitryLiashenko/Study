class Grade:
    def __init__(self, subject, score):
        self.subject = subject
        self.score = score

    def __str__(self):
        return f"{self.subject}: {self.score}"


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, subject, score):
        grade = Grade(subject, score)
        self.grades.append(grade)

    def __str__(self):
        grades_str = ", ".join(str(g) for g in self.grades)
        return f"{self.name} — {grades_str}"
    
    #def average_score(self):
    #    return sum(self.grades.values()) / len(self.grades)
    
    def average_score(self):
        return sum(grade.score for grade in self.grades) / len(self.grades)



class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        students_str = "\n  ".join(str(s) for s in self.students)
        return f"Class {self.class_name}:\n  {students_str}"


class School:
    def __init__(self, name):
        self.name = name
        self.classes = []

    def add_classroom(self, classroom):
        self.classes.append(classroom)

    def __str__(self):
        classes_str = "\n".join(str(c) for c in self.classes)
        return f"School: {self.name}\n{classes_str}"


# Пример использования:
my_school = School("Hogwarts")

class_1A = Classroom("1A")

harry = Student("Harry Potter")
harry.add_grade("Magic", 12)
harry.add_grade("Potions", 10)

ron = Student("Ron Weasley")
ron.add_grade("Magic", 9)

hermiona = Student("Hermiona")
hermiona.add_grade("Magic", 10)
hermiona.add_grade("Potions", 8)

class_1A.add_student(harry)
class_1A.add_student(ron)
class_1A.add_student(hermiona)

my_school.add_classroom(class_1A)

print(my_school)

print(hermiona.average_score())