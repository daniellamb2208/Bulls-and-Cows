import random

def answer():
    x = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(x)

    return x[0:4]

def diff(a, b):
    # A
    A, B = 0, 0

    for i in range(4):
        for j in range(4):
            if a[i] == b[j] and i == j:
                A = A + 1
            elif a[i] == b[j]:
                B = B + 1
    print("{}A{}B".format(A, B))
    return A, B

def strize(z):
    return str(z[0])+str(z[1])+str(z[2])+str(z[3])

def guess():
    
    x = answer()
    y = [0,1,2,3,4,5,6,7,8,9]
    z = y.copy()
    
    print("--------------------")
    print("Answer is {}".format(strize(x)))
    
    c = 1
    random.shuffle(z)
    print("{} is".format(strize(z)), end = " ")
    while not diff(x, z[0:4]) == (4, 0):
        random.shuffle(z)
        print("{} is".format(strize(z)), end = " ")
        c = c + 1
    print("Win at {}th times".format(c))
    return c

if __name__ == "__main__":
    p = 0
    for i in range(20):
        p = p + guess()

    print("avg of win time is "+str(p/20))