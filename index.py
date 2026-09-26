from studentModel import Student

DataBase = []

def AddStudent():

    student = Student(
    name=input("Enter student name: "),
    branch=input("Enter branch: "),
    department=input("Enter department: "),
    year=input("Enter year: ")
)

    DataBase.append(student)
    print(f"Student Registrations Succesfull!")
    return
print("Invalid Credentials!")

# print(student.name)
# print(student.branch)
# print(student.department)
# print(student.year)

