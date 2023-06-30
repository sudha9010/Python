N = input("Enter a string: ")
N_str = str(N)
a = len(N_str)
for i in range(a-1, -1, -1):
    print(N_str[i])
