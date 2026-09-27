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
    print("-" * 40)
    print(student.name)
    print(student.branch)
    print(student.department)
    print(student.year)
    print("-" * 40)
    return
print("Invalid Credentials!")

def DelStudent():

    student = Student(
    name=input("Enter student name: "),
    branch=input("Enter branch: "),
    department=input("Enter department: "),
    year=input("Enter year: ")

)
    DataBase.remove(student)
    print(f"Student Deleted Succesfull!")
    print("-" * 40)
    print(student.name)
    print(student.branch)
    print(student.department)
    print(student.year)
    print("-" * 40)
    return
print("Invalid Credentials!")




