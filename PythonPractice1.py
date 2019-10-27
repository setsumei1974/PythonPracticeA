'''
#Practice 1
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2019 - age)+100)
print(name + " will be 100 years old in the year " + year)
'''

'''
#Practice 2
number = int(input("What is your number?  "))

if number % 2 == 0:
    print("I see that your number is even!")
else:
    print("I see that your number is odd!")
'''

'''
#Practice 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

for item in a:
    if item < 10:
        b.append(item)
        print(b)
    if item >= 10 and item < 20:
        c.append(item)
        print(c)
'''

'''
#Practice 4
number = int(input("What is your number?  "))
range = list(range(1, number + 1))
divisor_list = []

for value in range:
    if number % value == 0:
        divisor_list.append(value)
        print(divisor_list)
'''

'''
#Practice 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
common_values = []

for x in a:
    if x in b and x not in common_values:
        common_values.append(x)
        print(common_values)
'''

'''
#Practice 6A
word = input("Please enter a word.  ")
word = str(word)
reverse = word[: : -1]
print(reverse)
if word == reverse:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")
'''