# Code to print the greatest number among the given N inputs
N = int(input("Enter the number of inputs: "))
max_number = float('-inf')  # Initialize max_number to negative infinity

for i in range(N):
    num = int(input("Enter a number: "))
    if num > max_number:
        max_number = num

print("The greatest number is:", max_number)
