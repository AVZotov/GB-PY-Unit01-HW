def CheckInt(string):
    if len(string) != 6:
        return False
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True if len(string) == 6 else False

def IsLuckyTicket(userInput):
    firstValue = 0
    secondValue = 0
    
    if CheckInt(number):
        for i in range(3):
            firstValue += int(userInput[i])
    
        for i in range(-1, -4, -1):
            secondValue += int(userInput[i])
        
        return True if firstValue == secondValue else False
    
    return False
        

number = input('Enter Value: ')
print(f'Is your ticket is lucky? = {IsLuckyTicket(number)}')
