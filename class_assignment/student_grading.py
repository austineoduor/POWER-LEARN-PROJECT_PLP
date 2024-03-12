#!/usr/bin/pythom3

student_name = str(input("\n\nstudent name (strings only).. "))
student_marks = int(input("Enter student marks (digits only)..  "))
name = student_name.upper()
marks = student_marks

if student_name is not None and student_marks >= 0:
    if marks >= 80:
        print(f"\n{name}\'s Grade is Distinction")
    elif marks >= 60 and marks <= 79:
        print(f"\n{name}\'s Grade is Credit")
    elif marks >= 40 and marks <=59:
        print(f"\n{name}\'s Grade is Fair")
    else:
        print(f"\n{name}\'s Grade is Fail")
else:
    print(f"\nInvalid Marks or Student Name")
