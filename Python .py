
teacher_name = input(" What is  your teacher name?: ")
student_name = input("What is your name?:  " )
year_level = int(input("What year are you?:  "))
if year_level == 11 :
    courses_11 = ["MAT1", "SCI1" ,"ENG1" ]
    print(courses_11)
    select = input("Select your course: ")
    print(f"{student_name} is year {year_level}, teacher name is {teacher_name}. Coursese selected : {select}")

elif year_level == 12 :
    courses_12 = ["MAT2", "SCI2" ,"ENG2" ]
    print(courses_12)
    select_2 = input("Select your course: ")
    print(f"{student_name} is year {year_level}, teacher name is {teacher_name}. Coursese selected : {select_2}")

elif year_level == 13 :
    courses_13 = ["MAT3", "SCI3" ,"ENG3" ]
    print(courses_13)
    select_3 = input("Select your course: ")
    print(f"{student_name} is year {year_level}, teacher name is {teacher_name}. Coursese selected : {select_3} ")
    


                   

    
