
def GetInt():
    while(True):
        userInput = input('Enter value: ')
        try:
            int(userInput)
            return int(userInput)
        except:
            print('Value not a number! Please try again')

width = GetInt()
height = GetInt()
pieces = GetInt()

result = True if pieces < width * height and \
(pieces % width == 0 or pieces % height == 0) else False

if result:
    print(f'You can split chocolate on {pieces} pieces')
else:
    print('You can\'t split chocolate')