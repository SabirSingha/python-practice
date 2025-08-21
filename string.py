#                                                       start of the list
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
# print(numbers)#
# print(numbers2)
#                                                       end of the list



# text = 'Hello World'
# print(text[4:7])                                #space is also a part of the character in the string

# text = 'hello World'
# print(text[3:2])

# text = 'piece of text'

# print(text.capitalize())
# text.endswith(text)
# print(text.endswith(text))


#                                               Program that counts the vowels in the string

# text = input("Enter a piece of text: ".lower())
# vowels = "aeiou"
# vowel_count = 0

# for vowel in vowels:
#     vowel_count += text.count(vowel)

# print(f"The total count of vowels in the given text is {vowel_count}")


#                                               Program that reverses the string

# string = input("Enter a string: ")
# i = -1
# while i >= -len(string):
#     print(string[i])
#     i = i - 1

# string = input("Enter a string: ")
# print(string[::-1])\

# string = input("Enter a string: ")
# reversed_string = ""

# for char in string:
#     reversed_string = char + reversed_string
# print(reversed_string)

#                                               program to check whether the given string is palindrome or not

# text = input("Enter the text: ")
# reversed_text = text[::-1]

# if (text == reversed_text):
#     print("The given text is palindrome")
# else:
#     print("The given text is not palindrome")



# text = input("Enter the text: ")
# reversed_text = text[::-1]

# is_palindrome = (text == reversed_text)

# print(is_palindrome)

#                                                 To count the words in a given string & letter of words of the sentence


# text = input("Enter a sentence: ")
# print(text.split())

# word_count = len(text.split())
# print(word_count)

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# letter_count = 0

# for word in words:
#     print(f"The word {word} has {len(word)} letters")   
# for word in words:
#     letter_count += len(word)
# print(letter_count)

#                                                           To remove the vowels

# sentence = input("Enter your sentence: ")
# vowels = "aeiouAEIOU"
# vowelless = ""

# for char in sentence:
#     if char not in vowels:                                  #spaces are also characters so the output isn't just a long string without spaces
#         vowelless += char

# print(sentence)
# print(vowelless)

    
#                                                     a function to print the longest word in a sentence

# def find_longest_word():
    
#     sentence = input("Enter the sentence: ")

#     word = sentence.split()
#     longest_word = word[0]
#     max_length = len(word[0])

#     if not word:
#         print("please enter a sentence")
#         return
    
#     for current_word in word[0:]:
#         if len(current_word) > max_length:
#             longest_word = current_word
#             max_length = len(current_word)
    
#     print(sentence)
#     print(longest_word)
#     print(f"it's length is {len(longest_word)}")

# find_longest_word()


#                                              function that replaces character according to the user

# sentence = input("Enter a sentence: ")
# word_to_replace = input("Enter a word to replace: ")
# word_to_beplaced = input("Enter the word to be placed: ")

# new_sentence = sentence.replace(word_to_replace, word_to_beplaced)

# print(new_sentence)


# def my_replace(word_to_replace, word_to_beplaced):
#     return word_to_beplaced

# sentence = "this is a sentence"
# words = sentence.split()
# new_words = []
# word_to_replace = "this"
# word_to_beplaced = "that"

# for word in words: 
#     if word == word_to_replace:
#         new_words.append(my_replace(word_to_replace, word_to_beplaced))
#     else:
#         new_words.append(word)

# new_sentence = " ".join(new_words)
# print(new_sentence)


#                                                                                to check if a substring exists in the main string

sentence = input("> ")
sub_sentence = input("enter a sub string to find within the string: ")
sentence_tolist = sentence.split(sub_sentence)
list_tosentence = ""

new_sentence = list_tosentence.join(sentence_tolist)

if sentence == new_sentence:
    print("the specified sub string was not found")
else:
    print("the specified string does exist in the sentence")
    index_substring = sentence.index(sub_sentence)
    print(f"The index of substring is {index_substring}")


#                                            


















    
    























#                                                   Capitalize first letter

# text = input("Enter a word: ")

# print(f"{text[0].capitalize()}{text[1:]}")


#                                                       program to access dictionary and change values

# emoji_mapping = {   
#     ":)": "happy face",
#     ":(": "sad face"
# }

# sentence = input("> ")
# words = sentence.split(" ")

# new_word = "" 

# for word in words:
#     new_word += emoji_mapping.get(word, word) + " "
# print(new_word)