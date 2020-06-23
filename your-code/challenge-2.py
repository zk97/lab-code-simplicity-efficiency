"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""
import random

chars=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
def RandomStringGenerator(size=12):
    return ''.join(random.choices(chars,k=size))

def BatchStringGenerator(n, a=8, b=12):
    print([RandomStringGenerator(random.choice(range(a,b+1))) for i in range(n)])

def Limits(place,lower=1):
    if lower==0:
        x=input('How many random strings to generate? ')
        try:
            x=int(x)
        except:
            print('Please enter a valid number')
            x=Limits(place,lower=lower)
        if x<1:
            print('Please enter number 1 or greater')
            x=Limits(place,lower=lower)
    else:
        x=input(f'Enter {place} string length: ')
        try:
            x=int(x)
        except:
            print('Please enter a valid number')
            x=Limits(place,lower=lower)
        if x<lower:
            print(f'Please enter number {lower} or greater')
            x=Limits(place,lower=lower)
    return x

if __name__=='__main__':
    a = Limits('minimum')
    b = Limits('maximum',a)
    n = Limits(None,0)

    BatchStringGenerator(n,a,b)
