#objective: Collect and evaluate grades for multiple students


#setting a unique identifer for each students in the iteration
countn = 1

# Initializing counters for summary
pass_count = 0
fail_count = 0
excellent_count = 0

#collecting the range from the client end user
student_range = int(input("Enter an integer of how many many students to process below: \n "))

#creating a for loop that handles the instruction
for students in range(student_range):
    
    #asking for student name input
    student_name = input(f"Enter the {countn} student_name below: \n")

    #asking for the first subject input
    subject_score1 = float(input(f"Enter the {countn} student first suubject score below(minimum 0, maximum 100): \n"))
    
    #asking for the second subject input
    subject_score2 = float(input(f"Enter the {countn} student second suubject score below(minimum 0, maximum 100): \n"))
    
    #asking for the third subject input
    subject_score3 = float(input(f"Enter the {countn} student third suubject score below(minimum 0, maximum 100): \n"))

    #setting a condition to control invalid input by client
    if not all(0 <= score <= 100 for score in [subject_score1, subject_score2, subject_score3]):
        print("Invalid input detected. Please restart and ensure all scores are between 0 and 100.")
        break
    
    #performing an average on the subjects input
    average_score = (subject_score1 + subject_score2 + subject_score3) / 3


    #setting an if condition statement to display result based on categories
    if average_score < 50:
        result = "Fail"
        fail_count += 1
    elif average_score >= 80:
        result = "Excellent!"
        excellent_count += 1
    else:
        result = "Pass"
        pass_count += 1

    print(f"{countn} {student_name} Result: {result} (Average Score: {average_score})")

    #ensuring the students identifer update by 1 for each loop
    countn += 1
    
#creating an empty space
print()

#summarizing the loop
print(f"""======summary======  \n Total students processed {countn - 1} 
      \n Total students passed {pass_count} 
      \n Total students failed {fail_count} 
      \n Total students that got excellent {excellent_count}"""
      )