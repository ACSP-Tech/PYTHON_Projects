#objective:  Build a program to store student names and their scores using lists/dictionaries.

mang_dict = {
            'student_name': [],
            'first_subject_score': [],
            'second_subject_score': [],
            'third_subject_score': [],
            'average_performance_score': []
        }

username = input("please enter a username below to kickstart your student management platform: \n")



def Stud_mang_program(existing_dict):
    
    while True:
        try:
            students_name = input(f"Welcome to {school_name} Student management system \nKindly enter the Student Name: \n")
            subject1st = float(input(f"Kindly enter {students_name} first subject score \n"))
            subject2nd = float(input(f"Kindly enter {students_name} second subject score \n"))
            subject3rd = float(input(f"Kindly enter {students_name} third subject score \n"))
            average_performance_stat = (subject1st + subject2nd + subject3rd) / 3

            existing_dict['student_name'].append(students_name)
            existing_dict['first_subject_score'].append(subject1st)
            existing_dict['second_subject_score'].append(subject2nd)
            existing_dict['third_subject_score'].append(subject3rd)
            existing_dict['average_performance_score'].append(average_performance_stat)

            repeat = input("Would you like to exit the app? Type(Exit) \nOr would you like to Enter another student record? Type(Enter): \n").strip().lower()
            if repeat == "exit":
                print("Kindly view your student management database below")
                break
            elif repeat == "enter":
                continue
            else:
                print(f"I can't understand {repeat}, you are now been prompted to enter a new student record")
                continue
        except ValueError:
            print(f"Kindly restart {students_name} record entry and enter a number for the subject score")
            continue
        except:
            print(f"Error with the code, kindly restart {students_name} record entry")
            continue

    print(mang_dict)
    return mang_dict

student_mang_sys = Stud_mang_program(mang_dict)

dict_student = student_mang_sys

def searchdb():
    name_to_search = input("Enter the student name to search the platform: ").strip().lower()
    found = False
    for i, student_name in enumerate(dict_student['student_name']):
        if name_to_search.lower() == student_name.lower():
            print(f"""
                  Student Name: {student_name}
                  First Subject Score: {dict_student['first_subject_score'][i]}
                  Second Subject Score: {dict_student['second_subject_score'][i]}
                  Third Subject Score: {dict_student['third_subject_score'][i]}
                  Average Performance Score: {dict_student['average_performance_score'][i]}
                """)
            found = True
    if not found:
        print("Student not found.")

while True:
    search_prompt = input( "would you like to search the database?: (Yes/No): " ).strip().lower()
    if search_prompt == "yes":
        searchdb()
        continue
    elif search_prompt == "no":
        continue_prompt = input("Would you like to exit the app? Type(Exit) \nOr would you like to continue entering another student records? Type(Enter): \n ").strip().lower()
        if continue_prompt == "exit":
            break
        elif continue_prompt == "enter":
            student_mang_sys_two = Stud_mang_program(dict_student)
            continue
        else:
            print("I can't understand your input, kindly input Yes or No")
            continue
    else:
        print("I can't understand your input, kindly input Yes or No")
        continue