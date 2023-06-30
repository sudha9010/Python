# Code to print odd number from N to M
M = int(input("Enter the value for M: "))
N = int(input("Enter the value for N: "))
b = ""
for i in range(M, N+1):
    if i % 2 != 0:
        b += str(i) + " "
print(b)
