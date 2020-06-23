"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

numbers={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5}
words={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
#Get number function receives if it is first or second number and asks input until number between 0 or 5 is received word or numbers accepted
def get_number(place):
    x=input(f'Please choose your {place} number (zero to five): ')
    try:
        x=int(x)
        if x not in range(6):
            print("Incorrect input please try again")
            x=get_number(place)
    except:
        try:
            x=numbers[x]
        except:
            print("Incorrect input please try again")
            x=get_number(place)
    return x
#Ask for operator until valid is received, word or symbols is accepted
def get_operation():
    x=input('What do you want to do? plus or minus: ')
    if x=='plus' or x=='+':
        return 'plus'
    elif x=='minus' or x=='-':
        return 'minus'
    else:
        print('Please enter a valid operator')
        return get_operation()
#Operate numbers and print result
def result(first,second,operator):
    if operator=='plus':
        result=first+second
        result=words[result]
    else:
        result=first-second
        try:
            result=words[result]
        except:
            result="negative "+words[-result]
    print(f'{words[first]} {operator} {words[second]} equals {result}')
if __name__=='__main__':
    print('Welcome to this calculator!')
    print('It can add and subtract whole numbers from zero to five')
    a = get_number('first')
    b = get_operation()
    c = get_number('second')
    result(a,c,b)
    
    print("Thanks for using this calculator, goodbye :)")
