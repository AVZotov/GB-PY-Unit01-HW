def CheckInt(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True

def IsConditionalNumber(string):
    if CheckInt(string):
        return True if int(string) % 2 == 0 else False
    return False

number = input("Enter your value: ")
coefficient = 6

if IsConditionalNumber(number):
    result = int(number) // coefficient
    print(f'Peter made = {result}\nSergey made = {result} \nKate made = {result * 4}')
else:
    print(f'Your input {number} not a number or number is odd!')