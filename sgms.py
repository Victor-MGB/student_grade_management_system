def add_student(student_dict,student_name):
    """adds a new student to the system"""
    student_dict[student_name] = {}
    print(f"Student {student_name} has been added.")
    
def add_grade(student_dict,student_name,subject,grade):
    """Adds or updates a grade for a student"""
    if student_name in student_dict:
        student_dict[student_name][subject] = grade
        print(f"Grade for {subject} has been added/updated for {student_name}.")
    else:
        print(f"Student {student_name} does not exist.")
        
def calculate_average(student_dict,student_name):
    """Calculate the average grade of a student"""
    if student_name in student_dict:
        grades = list(student_dict[student_name].values())
        if grades:
            return sum(grades)/len(grades)
        else:
            return 0
    else:
        print(f"Student {student_name} does not exist.")
        return None
    
def generate_report(student_dict):
    """Generates a report of students performance"""
    print("\n--- student Report ---")
    for student, subject in student_dict.items():
        print(f"\nStudent: {student}")
        for subject,grade in subject.items():
            print(f"Subject: {subject},Grade:{grade}")
        average = calculate_average(student_dict,student)
        print(f"Average Grade:{average:.2f}")
    
#Main Program 
def main():
    student_dict = {}
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Add or update a grade")
        print("3. Calculate average grade")
        print("4. Generate student report")
        print("5. Exit")
        
        choice = input("Enter your choice:")
        
        if choice == '1':
            student_name = input("Enter student name:")
            add_student(student_dict,student_name)
            
        elif choice == '2':
            student_name = input("Enter student name:")
            subject = input("Enter subject name:")
            grade = float(input("Enter grade:"))
            add_grade(student_dict,student_name,subject,grade)
            
        elif choice == '3':
            student_name = input("Enter student name:")
            average = calculate_average(student_dict,student_name)
            if average is not None:
                print(f"Average grade for {student_name}: {average:.2f}")
                
        elif choice == '4':
            generate_report(student_dict)
            
        elif choice == '5':
            print("Existing program")
            break             
                 
        else:
            print("@Invalid choice.please choose again")
            
if __name__ == "__main__":
    main()