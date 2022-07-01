print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = float(input('Please choose your first number (0-5): '))
b = input('What do you want to do? + or -: ')
c = float(input('Please choose your second number (0-5): '))

def calculator(a, b, c):
    if a and c in range(0, 5) and (b=="+" or b=="-"):
        if b == "+":
            return (a + c)
        if b == "-": 
            return (a - c)
    else:
        return print("I am not able to answer this question. Check your input.")
print(calculator(a, b, c))
print("Thanks for using this calculator, goodbye :)")