#objective: Build a tool to analyze numbers entered by the user.
#defining the variables to be used in the summary statement
negative = 0
odd = 0
even = 0
positive = 0
zero = 0

#constructing a for loops that loops 5 times
for num in range(5):
    #handled valueerrror from customer as repeat when customer input other dtypes aside from int
    try:
        #asking for customer input
        number = int(input("Kindly input any number: "))
        #condition to be meet for negative number
        if number < 0:
            #storing the count when the condition is meet
            negative += 1
        #condition to be meet for zero number
        elif number == 0:
            #storing the count when the condition is meet
            zero += 1
        #condition to be meet for positive number
        elif number > 0:
            #storing the count when the condition is meet
            positive += 1
        #condition to be meet for odd number
        if number % 2 > 0:
            #storing the count when the condition is meet
            odd += 1
        #condition to be meet for even number
        elif number % 2 == 0:
            #storing the count when the condition is meet
            even += 1
    except ValueError:
        print("please don't enter a string, float or other data types, just number")
        continue

#summarizing the loop
print(f"""======summary======
      \n Total even number {even} 
      \n Total odd number {odd} 
      \n Total negative number {negative}
      \n Total postive number {positive}
      \n Total Zero number {zero}"""
      )