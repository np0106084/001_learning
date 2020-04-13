import math


print ('My calculator' '\n' '---------------')
print ('Select from below:''\n''Press "1" for Addition' '\n''Press "2" for Subtraction''\n''Press "3" for Multiplication''\n''Press "4" for Division')

selection = input('Please select no between 1-4:')

print ('You have selected='+ selection)

if int(selection) == 1:
    print ('Welcome to Addition')
    print ('How many numbers you want to add?=')
    no_of_variable = input ()
    summation = 0
    initial = 0
    
    while int(no_of_variable) >= 1:
        if  True:
            var1 = input('Number' + str(int(initial) + 1) + '= ')
            summation = float(var1) + float(summation)
            no_of_variable = int(no_of_variable) - 1
            initial = int(initial) + 1

        else:
            print ('GL')

    print ('Summation=' + str(summation))

    

# if int(selection) == 2:
#     print ('Welcome to Subtraction')

# if int(selection) == 3:
#     print ('Welcome to Multiplication')

# if int(selection) == 4:
#     print ('Welcome to Division')

else: 
    print ('Good luck')