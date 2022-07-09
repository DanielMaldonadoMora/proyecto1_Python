import csv
from operator import ne
students = []
students_names = []


class Student:
    def __init__(self, name, last_name, acurracy, score, quizes):
        self.name = name
        self.last_name = last_name
        self.accuracy = acurracy
        self.score = score
        self.quizes = quizes


class Quizes:

    def __init__(self, files: list):
        self.files = files
        self.quizes_list = []

    def open_files(self):

        for file in self.files:
            with open(file, newline='') as file:
                content = csv.reader(file)
                CSV_toTuple = [list(row) for row in content]
                self.quizes_list.append(CSV_toTuple)
        return

    def set_students(self):

        for quiz in self.quizes_list:
            for student in quiz[1:len(quiz)]:
               # if student[1]
                student[4] = int(student[4])
                porcent = student[3].split()
                set_porcent = [int(porcent[0]), porcent[1]]

                student_name = f"{student[1]} {student[2]}"
                if student_name not in students_names:
                    students_names.append(student_name)
                    new_student = Student(
                        student[1], student[2], set_porcent, student[4], 1)
                    students.append(new_student)
                    print(
                        f"cree a {new_student.name}  {new_student.last_name} y actualmente tiene estos puntos {new_student.score} y tiene {new_student.accuracy[0]} %")
                else:
                    for student_it in students:
                        if student_it.name == student[1] and student_it.last_name == student[2]:
                            student_it.score = student_it.score+student[4]
                            student_it.quizes += 1
                            student_it.accuracy = [
                                (student_it.accuracy[0]+set_porcent[0])/student_it.quizes, set_porcent[1]]

                            print(
                                f"Acrualice los puntos de {student_it.name} {student_it.last_name} y ahora tiene {student_it.score} y {new_student.accuracy[0]} %")
        return

    # def add_up_points(self):


quiz1 = Quizes(["quiz_1.csv", "quiz_2.csv"])
quiz1.open_files()
quiz1.set_students()
