print("Hello, World!")

 num1 = 10
 num2 = 7
 sum = num1 + num2
 print("The sum of", num1, "and", num2, "is", sum)

n = int(input("Enter the number of rows for the rhombus: "))

# Upper half of the rhombus
for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1))

# Lower half of the rhombus
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (i + 1))


