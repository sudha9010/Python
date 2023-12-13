try:
    raise ValueError
    print(1)
except ValueError:
    print(2)
except TypeError:
    print(3)
