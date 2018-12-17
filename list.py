'''Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.'''


print('1. Conversion in inches')
print('2. Conversion in yards')
print('3. Conversion in miles')
print('4. Conversion in millimeters')
print('5. Conversion in centimeters')
print('6. Conversion in kilometers')
conversion_choice = int(input('Enter your choice conversion: ')) #The user chooses which conversion it wants
value= int(input('Enter a value in feet: '))

L=[0, value*12, value/3, value/5280, value*304.8, value*30.48, value/3280.84]
for i in range(len(L)):

    if conversion_choice==L[i]:
        print('Your answer is loading...........')
print(L[conversion_choice])














