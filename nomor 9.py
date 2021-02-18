def compute_lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num 1 = 12
num 2 = 20

print('nilai KPK adalah ',compute_lcm(num1, num2))