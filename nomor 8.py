# python program to find L.C.M. of two input number

# this function computes GCD

def compute_gcd(x, y):

    while(y):
        x, y = y, x % y
    return x

# this function commputes LCM
def compute_lcm(x, y):
    lcm = (x*y//compute_gcd(x,y)
    return lcm

num 1 = 12
num2 = 20

print("The L.C.M. is", compute_lcm(num1, num2))