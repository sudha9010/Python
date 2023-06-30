# Code to find the numbers divisible by 6 from range M to N and if the count of number divisible by 6 is 0 then print No Number Found
M = int(input("Enter the starting number: "))
N = int(input("Enter the ending number: "))

count = 0

for i in range(M, N + 1):
    if i % 6 == 0:
        print(i)
        count += 1

if count == 0:
    print("No numbers found.")

