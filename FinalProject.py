#FinalProject.py
#Rowan Patton
#CSCI 1103
#8/7/2021

#Program will, based on user determined start and end values, determine if value is divisible by 3, 5, or both evenly

again = 'y'
while again.lower() == "y":
    start_value = input('Please enter the starting value: ')
    while start_value.isnumeric() == False:
            start_value = input("That's not a valid response. Please enter the starting value: ")
    end_input = input('Please enter the end value: ')
    while end_input.isnumeric() == False:
            end_input = input("That's not a valid response. Please enter the end value: ")                            
#add one to end value input so it will be included in the printed range
    end_value = int(end_input) + 1

#function to check if each number is divisible by 3, 5, or both evenly
    def modulo_check():
        if i % 5 == 0 and i % 3 == 0:
            print(str(i) + ' -- both')
        elif i % 5 == 0:
            print (str(i) + ' -- 5')
        elif i % 3 == 0:
            print(str(i) + ' -- 3')
        else: print(str(i))

#in the user defined range, run the modulo check function from above
    for i in range(int(start_value), int(end_value)):
        modulo_check()

    again = input("Play again? (y/n): ")
    print()

print("Thanks for a great semester!")

    


