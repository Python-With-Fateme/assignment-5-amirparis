while True :
    number1=float(input('entrt your first number : '))
    number2=float(input('enter your second number :'))

    if number1==0 and number2==0 :
        break 
    
    if number1>number2 :
        print('fisrt number is bigger ')

    else :
        print('second number is bigger ')