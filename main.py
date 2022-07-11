import csv
# Variables Globales
students = []
students_names = []


class Student:
    def __init__(self, name, last_name, acurracy, score, quizes):
        self.name = name
        self.last_name = last_name
        self.accuracy = acurracy
        self.score = score
        self.quizes = quizes

    def update_score(self, new_score):
        self.score = self.score+new_score

    def update_accuracy(self, new_porcent):
        self.quizes.append(new_porcent)
        self.accuracy = round((sum(self.quizes) / len(self.quizes)), 2)


class Quizes:

    def __init__(self, files: list):
        self.files = files
        self.quizes_list = []

    def open_files(self):
        # Para cada archivo
        for file in self.files:
            # Lo abrimos y lo agragamos como una lista que contiene a cada estudiante en una lista con sus datos
            with open(file, newline='') as file:
                content = csv.reader(file)
                CSV_toTuple = [list(row) for row in content]
                self.quizes_list.append(CSV_toTuple)
        return

    def set_students(self):
        # Paraa cada lista revisamos cada estudiante
        for quiz in self.quizes_list:
            for student in quiz[1:len(quiz)]:
                # Procesamos sus datos y les damos el formato requerido
                student[4] = int(student[4])
                porcent = student[3].split()
                set_porcent = int(porcent[0])
                student_name = f"{student[1]} {student[2]}"

                # Si el estudiante  aun no ha sido creado y agregado su nombre completo a la lista entonces lo creamos
                if student_name not in students_names:
                    try:
                        students_names.append(student_name)
                        new_student = Student(
                            student[1], student[2], set_porcent, student[4], [set_porcent])
                        students.append(new_student)

                    except:
                        print("An error occurred while creating student")

                # En caso de que ya exista lo actualizamos
                else:
                    for student_it in students:

                        # Iteramos cada Objeto ya creado y si encontramos una coincidencia una coincidencia con el estudiante actual entonces se actualiza
                        if student_it.name == student[1] and student_it.last_name == student[2]:
                            student_it.update_score(student[4])
                            student_it.update_accuracy(set_porcent)
        return

    def winners(self, number_of_winners):
        # Ordenamos la lista de participantes de mayor a menor
        students.sort(reverse=True, key=lambda x: x.score)
        # Devolevemos la lista con la cantidad de ganadores seleccionados
        return students[0:number_of_winners]

    def min_accuracy(self, porcent):
        """"Aqui Verificamos  uno por uno que tenga el porcentaje minimo y lo incluimos en una lista que retornaremos"""
        aprovated = []
        for student in students:
            if student.accuracy >= porcent:
                aprovated.append(student)
        return aprovated


# Archivos para Abrir y formatear
quiz = Quizes(["quiz_1.csv", "quiz_2.csv", "quiz_3.csv", "quiz_4.csv"])
quiz.open_files()
quiz.set_students()
# Procesar ganadores
winners = quiz.winners(2)
aprobados = quiz.min_accuracy(70)

# Imprimir Ganadores
for winner in winners:
    print(
        f"El puesto numero {winners.index(winner)+1} es para: {winner.name} {winner.last_name} con {winner.score}")

print("\n")
# Imprimir Todos los que aprovaron el minimo de porcentaje
for aprobado in aprobados:
    print(f"{aprobado.name} {aprobado.last_name} obtuvo {aprobado.accuracy}% de precision")
