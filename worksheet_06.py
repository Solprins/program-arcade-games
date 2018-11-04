# Chapter 06 Worksheet
 
    
#    For each of the first two questions, write out your best guess as to what the
#    code will print. Clearly label this as your guess. Then run the code and look at
#    the output. Write if your guess was correct. If it was not, briefly describe what
#    was different and why.
 
#    Predicting what the code will do is important in writing programs, and
#    figuring out why programs don't run the way expected.
    
# 1. What does this program print out?
#    (Remember: TWO answers. Your guess and the actual result. Label both.)
    
x = 0
while x < 10:
    print(x)
    x = x + 2

# Best guess:
# 0
# 2
# 4
# 6
# 8
# Actual result:
# 0
# 2
# 4
# 6
# 8

 
# 2. What does this program print out?
    
x = 1
while x < 64:
    print(x)
    x = x * 2

# Best guess:
# 1
# 2
# 4
# 8
# 16
# 32
# Actual result:
# 1
# 2
# 4
# 8
# 16
# 32



# 3. Why is the ``and x >= 0'' not needed?
    
x = 0
while x < 10 and x >= 0:
    print(x)
    x = x + 2

# Answer:
# Because the value of x will be bigger than or equal to 0 all the time.


# 4. What does this program print out? (0 pts) Explain. (1 pt)
    
x = 5
while x >= 0:
    print(x)
    if x == "1":
        print("Blast off!")
    x = x - 1

# Answer:
# The program will count down to 0, but not print "Blast off!" because x is an int
# and "1" is a string so the condition will never be true. To correct the code remove the "" around 1 and insert a break:
x = 5
while x >= 0:
    print(x)
    if x == 1:
        print("Blast off!")
        break
    x = x - 1


# 5. Fix the following code so it doesn't repeat forever, and keeps asking
#    the user until he or she enters a number greater than zero: (2 pts)
    
x = float(input("Enter a number greater than zero: "))

while x <= 0:
    print("Too small. Enter a number greater than zero: ")

# Answer:
x=0
while x <= 0:
    x = float(input("Enter a number greater than zero: "))
    if x <=0:
        print("Too small. Enter a number greater than zero: ")


# 6. Fix the following code:
    
x = 10

while x < 0:
    print(x)
    x - 1

print("Blast-off")

# Answer: Reverse the lesser than symbol with a greater than symbol and make -1 assigned to x with =
x = 10

while x > 0:
    print(x)
    x -= 1

print("Blast-off")


# 7. What is wrong with this code? It runs but it has unnecessary code.
#    Find all the unneeded code. Also, answer why it is not needed. (1 pt)
    
i = 0
for i in range(10):
    print(i)
    i += 1

# Answer:
# i = 0 is not needed because the default value of i is 0
# i += 1 is not needed because this for loop will start at value 0 and end at value 9 because of the argument 10
for i in range(10):
    print(i)


# 8. Explain why the values printed for x are so different. (2 pts)
    
# Sample 1
x = 0
for i in range(10):
    x += 1
for j in range(10):
    x += 1
print(x)

# Answer:
# Sample 1 will print 20
# The i loop will increment x to the value 10
# The j loop will follow the i loop and will increment the value to 20
# The i and j loop are not nested, so they will each run 10 times for a total of 20 times

# Sample 2
x = 0
for i in range(10):
    x += 1
    for j in range(10):
        x += 1
print(x)

# Answer:
# Sample 2 will print 110
# The i loop will run 10 times and increment x with 1 each time
# The j loop will run 10*10=100 times and increment x with 100

# Sample 1 and 2 give very different results because in sample 2 the j loop is nested inside the i loop and will run 90 times
# more than the j loop that is not nested in sample 1