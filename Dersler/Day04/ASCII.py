
# LOWERCASE

lowercaseLetters = []
for i in range(97,123):
    lowercaseLetters.append(chr(i))
print(lowercaseLetters)

# UPPERCASE
alfabe = []
for i in range(65,91):
    alfabe.append(chr(i))
print(alfabe)


# or

import string
abc = list(string.ascii_lowercase)
print (f'Lowercase Letters: {abc}')

abc = list(string.ascii_uppercase)
print (f'Uppercase Letters: {abc}')