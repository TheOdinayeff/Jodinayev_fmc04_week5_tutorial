students = ["Aziza", "Bekzod"]

students.append("Diyor")

entered_student = "Aziza"
if entered_student in students:
    print(f"{entered_student} is in the list.")
    students.remove(entered_student)

