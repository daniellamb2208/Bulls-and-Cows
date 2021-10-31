import random #choice
from itertools import permutations

digit = 6
t = 10  # loop times

def answer():
    x = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(x)

    return x[0:digit]

def diff(a, b):

    A, B = 0, 0

    for i in range(digit):
        for j in range(digit):
            if a[i] == b[j] and i == j:
                A = A + 1
            elif a[i] == b[j]:
                B = B + 1
    return A, B

def strize(z):
    s = ""
    for i in range(digit):
        s += str(z[i])
    return s

def narrow(z, g, A, B):
    # ref:https://neilchennc.blogspot.com/2010/05/ab.html
    # Fixed by De Morgan's laws
    zz = []
    z.remove(g)
    for i in z:
        if diff(i, g) == (A, B):
            zz.append(i)
    return zz

def guess(cc):
    
    x = answer()
    y = [0,1,2,3,4,5,6,7,8,9] # Elements
    z = list(permutations(y, digit))  # Universal 
    
    print("---------------------------")
    print("Total possibilities is {}".format(len(z)))
    print("{}: Answer is {}".format(cc, strize(x)))

    c = 1
    while True:
        _guess = random.choice(z)

        (A, B) = diff(x, _guess)
        print("{}: Guess {} is {}A{}B.".format(c, strize(_guess), A, B))
        
        if (A, B) == (digit, 0):
          print("{}th guesses to find answer".format(c))
          return c

        c = c + 1
        z = narrow(z, _guess, A, B)
        print("Remaining possible answers: {}".format(len(z)))

# plan to multi-threading

if __name__ == "__main__":

    while True:
        digit = int(input("Please enter which digit to guess:"))
        t = int(input("Please enter how many round to guess:"))
        if digit not in range(1,11) and t > 100:
            pass
        if digit == 0:
            print("Bye Bye")
            break
        p = 0
        for i in range(1,t+1):
            p = p + guess(i)
        
        print("Average guess count is {}".format(p/t))