# Chapter 07 Worksheet
 
     
#     NOTE: In the following problems, if an error prevents an example from running, make
#     certain to mention that as part of the results. Also, be precise. If program prints [1],
#     doesn't say it prints 1.
 
     
#  1. List the four types of data we've covered, and give an example of each:

# Answer: 
# String is a string of characters fx "Hello World!"
# Int is an integer, this is a number fx 100
# Float is a floating point number fx 2.5
# Boolean is a a binary variable that can have one of two possible values, False or True

 
#  2. What does this code print out? For this and the following problems, make
#     sure you understand WHY it prints what it does. You don't have to explain it,
#     but if you don't understand why, make sure to ask.
#     Otherwise you are wasting your time doing these.
     
#     my_list = [5, 2, 6, 8, 101]
#     print(my_list[1])
#     print(my_list[4])
#     print(my_list[5])
     
# Answer: My best guess:
# 2
# 101
# an index out of bounds error
# The result was:
# 2
# 101
# Traceback (most recent call last):
# line 26, in <module>
#     print(my_list[5])
# IndexError: list index out of range


#  3. What does this code print out?
     
#     my_list=[5, 2, 6, 8, 101]
#     for my_item in my_list:
#         print(my_item)

# Answer: My best guess:
# 5
# 2
# 6
# 8
# 101
# Correct

#  4. What does this code print out?
     
# my_list1 = [5, 2, 6, 8, 101]
# my_list2 = (5, 2, 6, 8, 101)
# my_list1[3] = 10
# print(my_list1)
# my_list2[2] = 10
# print(my_list2)

# Answer: My best guess:
# 5
# 2
# 6
# 10
# 101
# 5
# 2
# 10
# 8
# 101
# Result: I over looked my_list2 was a tuple that cannot be reassigned values
# [5, 2, 6, 10, 101]
# Traceback (most recent call last):
#line 61, in <module>
#     my_list2[2] = 10
# TypeError: 'tuple' object does not support item assignment

#  5. What does this code print out?
     
# my_list = [3 * 5]
# print(my_list)
# my_list = [3] * 5
# print(my_list)

# Answer: My best guess:
# [15]
# [3,3,3,3,3]
# Correct
     
#  6. What does this code print out?
     
# my_list = [5]
# for i in range(5):
#     my_list.append(i)
# print(my_list)

# Answer: My best guess:
# [5,0,1,2,3,4]
# Correct


#  7. What does this code print out?
     
# print(len("Hi"))
# print(len("Hi there."))
# print(len("Hi") + len("there."))
# print(len("2"))
# print(len(2))

# Answer: My best guess:
# 2
# 9
# 9
# 1
# 1
# Result: I missed that there was no space in the concatenated strings and len() requires an object like a string or a list
# len() doesnt work on int
# 2
# 9
# 8
# 1
# line 112, in <module>
#     print(len(2))
# TypeError: object of type 'int' has no len()

#  8. What does this code print out?
     
# print("Simpson" + "College")
# print("Simpson" + "College"[1])
# print( ("Simpson" + "College")[1] )

# Answer: My best guess:
# SimpsonCollege
# IndexError
# Result: I missed that you can print the index of a single string and also you can print the index of a concatenated string
# SimpsonCollege
# Simpsono
# i
     
#  9. What does this code print out?
     
# word = "Simpson"
# for letter in word:
#     print(letter)

# Answer: My best guess:
# S
# i
# m
# p
# s
# o
# n
# Correct

# 10. What does this code print out?
     
# word = "Simpson"
# for i in range(3):
#     word += "College"
# print(word)

# Answer: My best guess:
# SimpsonCollegeCollegeCollege
# Correct

# 11. What does this code print out?
     
# word = "Hi" * 3
# print(word)

# Answer: My best guess:
# HiHiHi
# Correct


# 12. What does this code print out?
     
# my_text = "The quick brown fox jumped over the lazy dogs."
# print("The 3rd spot is: " + my_text[3])
# print("The -1 spot is: " + my_text[-1])

# Answer: My best guess:
# e
# .
# Result: I missed the leading text in both lines and also miscounted [3] - forgot to count the [0]
# The 3rd spot is:  
# The -1 spot is: .

# 13. What does this code print out?
     
# s = "0123456789"
# print(s[1])
# print(s[:3])
# print(s[3:])

# Answer: My best guess:
# 1
# 012
# 3456789
# Correct

# 14. Write a loop that will take in a list of five numbers from the user, adding
#     each to an array. Then print the array. Try doing this without looking at the
#     book.

# Answer: My best guess:
# arr = [0]
# for add in range(5):
#     add = float(input("Please enter a number: "))
#     arr.append()=[add]
# print(arr)
# # Result:
# arr.append()=[add]
#     ^
# SyntaxError: can't assign to function call
# Below is a code that works with no assignment to a function call and accepts floats but prints ints
# arr = []
# for add in range(5):
#     add = float(input("Please enter a number: "))
#     arr.append(int(add))
# print(arr)


# 15. Write a program that take an array like the following, and print the average.
#     Use the len function, don't just use 15, because that won't work if
#     the list size changes.
#     (There is a sum function I haven't told you about. Don't use that.
#     Sum the numbers individually as shown in the chapter.)
#     (Also, a common mistake is to calculate the average each time through the
#     loop to add the numbers. Finish adding the numbers before you divide.)
     
#     my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]

# Answer: My best guess:
my_list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
average = 0
for item in range(len(my_list)):
    average += my_list[item]
print(average/len(my_list))
# Result: Correct
# 4.8

