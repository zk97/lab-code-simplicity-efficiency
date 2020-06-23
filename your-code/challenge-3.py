"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""
def size():
    x=input("What is the maximal length of the triangle side? Enter a number: ")
    try:
        x=int(x)
    except:
        print("Please enter a valid number")
        x=size()
    if x<5:
        print("Please enter number 5 or greater")
        x=size()
    return x

#Optimized function allows to search for bigger numbers (remember, if top=5n for some n then 3n^2+4n^2=top^2)
def calculate(top):
    #Check if top mod(5)!=0
    if top%5:
        #If not x,y are found then try with top -1 using break prevents extra iterations
        for y in range(3,int(top*.75)+1):
            for x in range(top-y,top):
                if top**2==x*x+y*y:
                    return top,x,y
        top,x,y=calculate(top-1)
    return top,x,y

#def my_function(X):
#    solutions = [[x,y,z] for x in range(5,X) for y in range (4,X) for z in range(3,X) if x*x==y*y+z*z]
#    return solutions[-1][0]
#
#X = input("What is the maximal length of the triangle side? Enter a number: ")
#
#print("The longest side possible is " + str(my_function(int(X))))

if __name__=='__main__':
    print("Up to 4 digits answer is given in acceptable time")
    sizes=calculate(size())
    print(f"The longest side possible is {sizes[0]} with solution being {sizes}")