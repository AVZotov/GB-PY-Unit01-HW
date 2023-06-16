def CheckInt(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True

number = input("Enter digit: ")
result = 0

if CheckInt(number):
    for value in number:
        result += int(value)
    print (result)
else:
    print (f'{number} not a digit')