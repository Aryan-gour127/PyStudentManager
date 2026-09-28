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

def SearchStudent():

    while True:

        Search = input("Enter Student Name : ")

        for item in Student:
            if Search != Student('name'):
                print("Student not found!1")
                return

            print("-" * 40)
            print("\nStudent Found : ")
            print(item.name)
            print(item.branch)
            print(item.department)
            print(item.year)
            break



while True:

    print("-" * 50)
    print("🎓 PyStudentManager")
    print("-" * 50)
    print("1. Add student ")
    print("2. Delete student")
    print("3. Search student")



    opt = input("Enter options number : ")

    if opt == "1":
        AddStudent()

    elif opt == "2":
        DelStudent()

    elif opt == "3":
        SearchStudent()

    elif opt == "4":
        print("See you Goodbye!")
        break
print("invalid input")