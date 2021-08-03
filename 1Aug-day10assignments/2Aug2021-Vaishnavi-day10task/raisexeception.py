try:
    n=int(input("Enter a number: "))
    if n<0:
        raise ValueError(n)
    else:
        print(n)
except ValueError:
    print("n is out of range")