# Exercises Python

# Exercise 1
a = 2
a = 4
a = 6
print(a+a+a)

#Exercice 4
#The script generates an error. Please add the appropriate code that adds variables a and b without an error.
#A: The script generates an error saying that an integer object cannot convert to string implicitly.
#Please try to convert the integer to a string explicitly then or the string to an integer.
a = "1"
b = 2
print(int(a) + b)

# Exercise 5
#Complete the script so that it prints out the second letter of the list
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1])

# Exercise 6
#Complete the script so that it prints out a list containing letters d, e, f.
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[3:6])
# Exercise 7
#Complete the script so that it prints out a list containing the first three elements of list letters
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[::2])
my_lst= []
for i in range(20):
    my_lst.append(i)

print(my_lst)

my_range = range(1,21,2)
for i in my_range:
    print((i *10))

my_range = range(1,21)
r = (list(my_range))
print(r)   