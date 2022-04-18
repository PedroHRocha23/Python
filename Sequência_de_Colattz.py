def collatz(number):
    if number % 2 == 0:
        x = (number // 2) 
    elif number % 2 == 1:
        x = (number + 1) * 3 
    
    return x

try:
    value = 0
    while value != 1: 
        number = int(input('Enter number:'))
        value = collatz(number)
        print(value)

    print('End!')

except:
    print('Deve ser fornecido um número inteiro')
