"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

For example, if the stair has 4 steps, there are 5 ways to climb to the top:
1) 1, 1, 1, 1
2) 1, 2, 1
3) 1, 1, 2
4) 2, 1, 1
5) 2, 2

The following class calculates the total ways to climb a stair with the specified number of steps.
It also counts the number of calculations performed which indicates the efficiency of the code.
Try if you can improve the performance of the code.
"""
from scipy.special import comb

def steps():
    x=input("How many steps in the stair?")
    try:
        x=int(x)
    except:
        print("Please enter a valid number")
        x=steps()
    if x<0:
        print("Please enter number 1 or greater")
        x=steps()
    return x

class ClimbStairs:
    """
    Class constructor
    total_steps: how many steps in total in the stair
    """
    def __init__(self, total_steps=10): 
        self.total_steps = total_steps
        self.calculation_count = 0

    """
    This function calculates how many solutions are there to reach the top when climbing i times 2 steps
    and n - 2i times 1 step
    """
    def calc_solutions(self, i):
        # If the we try to climb 2 steps more than n/2 times there is no solution
        if i > self.total_steps-i:
            return 0

        # If solution is possible, continue calculating
        self.calculation_count += 1

        # Call the current function recursively. 
        # The number of solutions for i or more times 2 steps equals to the number of solutions for (i+1) or more times 2 steps
        # plus number of ways of picking double steps from [total times=n- number of double steps]
        return(self.calc_solutions(i+1) + comb(self.total_steps-i,i,exact=True))

    def get_calculation_count(self):
        return self.calculation_count

    def solve(self):
        return self.calc_solutions(0)

if __name__=='__main__':
    total_steps = steps()
    new_challenge = ClimbStairs(total_steps)
    print(f'Ways to climb to top: {new_challenge.solve()}')
    print(f'Total calculations performed: {new_challenge.get_calculation_count()}')
