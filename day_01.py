'''
 Write a program which will find all such number that are divisible by 7 but ar enot the multiple of 5,
 between 2000 and 3200 (both included).
#  The numbers obtained should be printed in comma separated sequence on a single line.

# '''
# for i in range(2000, 3200):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i, end=",")

# # print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")

# '''
#     Write a program which can compute the factorial of a given numbers.
#     The results should be printed in a comma-separated sequence on a single line.
#     Suppose the following input is supplied to the program: 8 Then, the output should be:40320
# '''

# given_number = int(input("Enter the number"))
# factorial = 1
# while (given_number >= 1):
#     factorial = factorial * given_number
#     given_number -= 1

# print(factorial)


def printing_greetings():
    self = input()
    print(self)

printing_greetings()
