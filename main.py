import csv
students = []


class Student:
    def __init__(self, name, last_name, acurracy, score):
        self.name = name
        self.last_name = last_name
        self.accuracy = acurracy
        self.score = score


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
        quiz_index = 1

        for quiz in self.quizes_list:
            for student in quiz[1:len(quiz)]:
               # if student[1]
                student[4] = int(student[4])
                if students:
                    for it_student in students:
                        if student[1] == it_student.name and student[2] == it_student.last_name:
                            print("encontre una igualdad")
                        else:
                            new_student = Student(
                                student[1], student[2], student[3], student[4])
                            students.append(new_student)
                            print("cree un nuevo estudiante")
                else:
                    new_student = Student(
                        student[1], student[2], student[3], student[4])
                    students.append(new_student)
                    print("Cree el primer estudiante")

        return

    # def add_up_points(self):


quiz1 = Quizes(["quiz_1.csv", "quiz_2.csv"])
quiz1.open_files()
quiz1.set_students()
