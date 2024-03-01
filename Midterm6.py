def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# Options provided
options = [
    "0974101607733149676776769413377061014790",
    "7798338247658278460338648728567428338977",
    "4257304920394478392772938744930294037524",
    "2704702208931031198668911301398022074072"
]

# Iterate through the options and check each one
for option in options:
    if not palindrome(option):
        print(option, "is NOT a palindrome.")
    else:
        print(option, "is a palindrome.")