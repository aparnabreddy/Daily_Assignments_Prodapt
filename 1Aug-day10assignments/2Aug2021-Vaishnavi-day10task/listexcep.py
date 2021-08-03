l=[234,456,678,654]
try:
    print(l[3])
    # print(a[2])
except (IndexError,NameError):
    print("Please enter correct index")
else:
    print("Execution completed successfully")

finally:
    print("ok")