"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Owen Anderson
Lab Time: THUR 2:00-3:15
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())
    for x in range(-11,11):
        for y in range(-11,11):
            if (a*x + b*y == c and d*x + e*y ==f):
                print("x =",x, ",","y =",y)
                return
    else:
        print("There is no solution")
        
    
if __name__ == "__main__":
    brute_eq()