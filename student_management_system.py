students = []

# Add Student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    students.append([roll, name])
    print("Student Added Successfully!")

# View Students
def view_students():
    if len(students) == 0:
        print("No Students Found.")
    else:
        print("\nStudent List")
        for student in students:
            print("Roll No:", student[0], " Name:", student[1])

# Search Student
def search_student():
    roll = input("Enter Roll No to Search: ")
    found = False

    for student in students:
        if student[0] == roll:
            print("Student Found")
            print("Roll No:", student[0])
            print("Name:", student[1])
            found = True

    if found == False:
        print("Student Not Found.")

# Update Student
def update_student():
    roll = input("Enter Roll No to Update: ")

    for student in students:
        if student[0] == roll:
            student[1] = input("Enter New Name: ")
            print("Student Updated Successfully!")
            return

    print("Student Not Found.")

# Delete Student
def delete_student():
    roll = input("Enter Roll No to Delete: ")

    for student in students:
        if student[0] == roll:
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found.")

# Main Program
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")