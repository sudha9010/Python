# Code to print a if a string has more than two vowels or not
S = input("Enter a string: ")
count = 0
length = len(S)
counter = 0
for i in S:
    if i.lower() in "aeiou":
        count += 1
    counter += 1
if count > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")






      