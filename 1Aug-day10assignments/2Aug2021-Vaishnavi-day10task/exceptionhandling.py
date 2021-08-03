# ZeroDivisionError - 20/0
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# div=a/b
# print(div)

# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     div=a/b            #can create eception
#     print(div)
# except :
#     print("Something went wrong")

try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    div=a/b            #can create exception
    print(div)
except ZeroDivisionError:
    print("division by zero not allowed")
except ValueError:
    print("Only number should be entered")