# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.
# 2. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# 3.Write a Python program to display the current date and time.
# Developed by : Yamini Rathod C0796390
# Date : 22-05-2021

import welcome_qus1
import welcome_qus2
import welcome_qus3
import calculateArea
import reverseOrder
import currentDateTime

endOfProgram = 'No'

if __name__ == '__main__':
    while endOfProgram != 'Yes':
        print('-------------------- Menu ----------------------')
        print('1. Run program to find the area of circle')
        print('2. Run program to reverse the order of name')
        print('3. Run program to display current date and time')
        print('4. Exit the main program')
        print('------------------------------------------------')
        choice = input('Please enter your choice : ')
        if choice == '1':
            welcome_qus1.print_welcome()
            calculateArea.calculateAreaOfCircle()
        elif choice == '2':
            welcome_qus2.print_welcome()
            reverseOrder.reverseOrderName()
        elif choice == '3':
            welcome_qus3.print_welcome()
            currentDateTime.currentDateTimeDisplay()
        elif choice == '4':
            print('Thanks for running the program!')
            exit(0)
        endOfProgram = input("\nDo you want to end the program? Press 'Yes' to Exit the program. Press 'No' to run again : ")