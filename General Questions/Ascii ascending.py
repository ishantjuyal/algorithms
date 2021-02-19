"""
Take a string from the user. Rearrange that string in ascending order based 
on ASCII code of each character. Then print the rearranged string and 
sorted ASCII code sequence of characters.
"""

print("Enter the string:")
s = input()

ascii = [ord(i) for i in s]
ascii = sorted(ascii)

for i in ascii:
    print(chr(i), end = '')