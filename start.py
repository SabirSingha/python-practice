# full_name = Aamon
# age = 20 
# is_new = True
# print(full_name)                                    #print is a function used to print in the output window

# name = input("What is your name? ")                 #input is a funtion used to take value from user
# color = input("What is your favourite color? ")     
# print(name + ' likes ' + color)                     #expression is a piece of code that produces a value... here I am combining three strings to give out one sentence

# pound = input('Enter the value in pounds: ')          
# print(type(pound))                                    #type function is used to show the type of the variable
# convert = float(pound)/2.20462                        #float(), int() etc are used for type conversion
# print(type(convert))
# print(f'Pound equivalent of kg is:{convert:2f}')            #f means formatted string literal for cleaner and faster string formatting

# message = ''' 
# Apparently three quotation is used for writing long strings "with this" or 'this'  #quotations that is
# included.
# '''
# print(message)

# first_name = 'Sabir'
# last_name = 'Singha'
# message = f"{first_name} [{last_name}] is learning python at the moment"
# print(message) 

# course = 'Python for Me'
# print(course)         # is a method, unlike function method are type specific, here  is specifically for strings
# print(course.lower())
# print(course)

# len()
# 
# .lower()
# .title()
# .find()
# .replace()
# '...' in variable

# Some mathematical functions
# x = -2.9
# print(abs(x))
# print(round(x))             #to import math module and use it's funciton like string using '.' - import math

#    If - statements

# price = 1000000

# good_credit = False

# if good_credit:
#     downpayment = 0.1 * price
# else: 
#     downpayment = 0.2 * price
# print(f"Downpayment: ${downpayment}")

#                                                           while statements (guessing game)

# secret_num = 9 
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_num:
#         print('You won!')
#         break
# else:
#     print('Sorry, you failed!')
    
#                                                          Creating a car game


# car_command = ""
# car_started = False
# while True:                                       #while true is used to loop the statements until we explicitly break out of it using break 
#     car_command = input('> ').upper()             #input().upper is used to dry (do not repeat) myself         
#     if car_command == 'HELP':
#         print('start - to start the car')
#         print('stop - to stop the car')
#         print('quit - to exit')
#     elif car_command == 'START':
#         if car_started:
#             print('The car is already started!')
#         else:
#             car_started = True
#             print('car started...Ready to go')
#     elif car_command == 'STOP':
#         if not car_started:
#             print('car is already stopped...')
#         else:
#             car_started = False
#             print('car has stopped')
#     elif car_command == 'QUIT':
#         break
#     else:
#         print("I don't understand that....")
        

#take an input from the user verify if it's positive, negative or zero

# number = int(input("Enter the number: "))

# if number > 0: 
#     print("The number is positive!")
# elif number < 0:
#     print("The number is negative!")
# else0:
#     print("You have entered 0!")

                                # For loops

# numbers = [5, 2, 5, 2, 2]

# count = 0 
# for number in numbers:
#     while count < number:
#         print(f"{count}")
#         count += 1

# numbers = [1, 1, 1, 1, 6]

# for count in numbers:
#     print('x' * count)

# numbers = [5, 3, 5, 2, 2]

# for x_count in numbers:
#     output = ''
#     for items in range(x_count):                #assuming we dont' have the feature to multiply string with variable for the times
#         output += 'x'
#     print(output)

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# print(names[2:5])


                                                #largest number in the list
# numbers = [3, 4, 5, 6, 7, 8, 10, 13]
# max = numbers[0]

# for number in numbers:
#     if number > max:
#         max = number
# print(max)
                                            # 2 x 2 lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     print(row)
                                            # useful methods for lists in numbers
# numbers = [5, 2, 4, 1, 7, 4, 5]
# # numbers.append(20)
# # numbers.insert(0, 10)
# # numbers.remove(5)
# # numbers.pop()
# # numbers.index(4)
# # print(5 in numbers) 
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers)
# print(numbers2)

# numbers = ['mosh', 'hamedani', 'crysantheum', 'balsam']
# numbers.sort()                                          #apparently sorting in list with letter happens alphabetically
# print(numbers)


                                                         # write a program to remove duplicates in a list

numbers = [1, 2, 2, 2, 2, 3, 4, 5, 5, 6, 6, 7]

# unique_numbers = list(set(numbers))
# unique_numbers.sort()
# print(unique_numbers)

# unique_list = []

# for number in numbers:
#     if number not in unique_list:
#         unique_list.append(number)

# print(unique_list)

# numbers = (1, 2, 3)                     # This is a tuple, it is immutable    
#
# flowers = ['roses', 'bluebell', 'chrysanthemum', 'daffodil']

# #                                                                 unpacking a list, tuple in python

# x, y, z, a = flowers

# print(x)
# print(y)
# print(z)
# print(a)

#                                                           Dictionary in python

# human_details = {
#     "name": "Sandaltree",
#     "contact_number": "123456789",
#     "address": "new zealand",
#     "nationality": "german"
# }

# print(human_details.get("colour", "Doesn't exist in human details"))


#                                                             code that asks your number and returns them in letters

# convert_number = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }

# user_number = (input("Enter your mobile number: "))


# print(user_number)

# for number in user_number:
#     print(convert_number.get(number))

# convert_number = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "0": "zero"  # Added 0 for completeness
# }

# user_number = input("Enter your mobile number: ")
# word = ""
# # The correct way to iterate and print
# for number in user_number:
#     # Use the variable `number` as the key, without quotes
#     word += convert_number.get(number)

# print(word)
 

 #                                                          emoji to word converter

# message = input("> ")

# emoji_mapping = {
#     ":)": "Happy face",
#     ":(": "sad face"
# }

# message.split()
# new_message = ""

# for char in message:
#     new_message += emoji_mapping.get(char, char)
# print(new_message)


#                                                           Functions


