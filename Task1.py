# Student Management System with File Storage (Beautiful Table View)

# Function to calculate grade based on average marks
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "Fail"

# Function to add a student record
def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")
    marks = []
    for i in range(1, 4):
        mark = int(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    avg = sum(marks) / 3
    grade = calculate_grade(avg)

    # Save record in file
    with open("students.txt", "a") as f:
        f.write(f"{roll_no},{name},{marks[0]},{marks[1]},{marks[2]},{avg:.2f},{grade}\n")

    print("✅ Student record added successfully!\n")

# Function to view all students (in table form)
def view_students():
    try:
        with open("students.txt", "r") as f:
            records = f.readlines()
            if not records:
                print("⚠️ No records found.\n")
                return
            
            # Print header
            print("\n📋 All Student Records:")
            print("="*75)
            print(f"{'Roll No':<10}{'Name':<15}{'Sub1':<8}{'Sub2':<8}{'Sub3':<8}{'Average':<10}{'Grade':<6}")
            print("-"*75)

            # Print each record
            for record in records:
                data = record.strip().split(",")
                print(f"{data[0]:<10}{data[1]:<15}{data[2]:<8}{data[3]:<8}{data[4]:<8}{data[5]:<10}{data[6]:<6}")
            
            print("="*75 + "\n")
    except FileNotFoundError:
        print("⚠️ No records file found yet.\n")

# Function to search student by roll number
def search_student():
    roll_no = input("Enter Roll Number to search: ")
    found = False
    try:
        with open("students.txt", "r") as f:
            for record in f:
                data = record.strip().split(",")
                if data[0] == roll_no:
                    print("\n✅ Student Found:")
                    print("-"*40)
                    print(f"Roll No   : {data[0]}")
                    print(f"Name      : {data[1]}")
                    print(f"Subject 1 : {data[2]}")
                    print(f"Subject 2 : {data[3]}")
                    print(f"Subject 3 : {data[4]}")
                    print(f"Average   : {data[5]}")
                    print(f"Grade     : {data[6]}")
                    print("-"*40 + "\n")
                    found = True
                    break
        if not found:
            print("❌ Student not found.\n")
    except FileNotFoundError:
        print("⚠️ No records file found yet.\n")

# Main menu
while True:
    print("===== 📚 Student Management System =====")
    print("1. ➕ Add Student")
    print("2. 📋 View All Students")
    print("3. 🔍 Search Student by Roll No")
    print("4. ❌ Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, try again.\n")
