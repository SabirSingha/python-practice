'''
 Write a program which will find all such number that are divisible by 7 but ar enot the multiple of 5,
 between 2000 and 3200 (both included).
#  The numbers obtained should be printed in comma separated sequence on a single line.

# '''
# for i7 in range(2000, 3200):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=",")

# print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")

'''
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''

# def factorial(given_number):
#     given_number = int(input("Enter the number"))
#     factorial = 1
#     while (given_number >= 1):
#         factorial = factorial * given_number
#         given_number -= 1
#     return factorial

# print(factorial(4))

'''
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

# def square_dictionary(given_number):
#     dic = {}
#     for i in range(1, given_number + 1):
#         dic[i] =  i ** 2
#     print(dic)

# square_dictionary(3)

''' 
    Write a program which accepts a sequence of comma-separated numbers from console 
    and generate a list and a tuple which contains every number.
    Suppose the following input is supplied to the program:

34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

'''

given_string = input("Enter the numbers: ")
string_to_list = given_string.split(",")
tuple = tuple(string_to_list)
print(f"{string_to_list} {tuple}")



