# Creating a list
my_list = [1, 2, 3]
print("Original list:", my_list)


# Modifying an element
my_list[1] = 99
print("Modified list:", my_list)


# Adding a new element
my_list.append(4)
print("List after adding an element:", my_list)
####################################################
# Creating a string
my_string = "hello"
print("Original string:", my_string)


# Attempting to modify the string
try:
    my_string[1] = 'a'
except TypeError as e:
    print("Error:", e)


# Proper way to modify a string
my_string = my_string[:1] + 'a' + my_string[2:]
print("Modified string:", my_string)