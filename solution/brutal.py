import random #choice
from itertools import permutations

def answer():
    x = [0,1,2,3,4,5,6,7,8,9]
    random.shuffle(x)

    return x[0:4]

def diff(a, b):

    A, B = 0, 0

    for i in range(4):
        for j in range(4):
            if a[i] == b[j] and i == j:
                A = A + 1
            elif a[i] == b[j]:
                B = B + 1
    return A, B

def strize(z):
    return str(z[0])+str(z[1])+str(z[2])+str(z[3])

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
    print("---------------------------")
    print("{}: Answer is {}".format(cc, strize(x)))

    y = [0,1,2,3,4,5,6,7,8,9] # Elements
    z = list(permutations(y, 4))  # Universal 
    
    c = 1
    while True:
        _guess = random.choice(z)

        (A, B) = diff(x, _guess)
        print("{}: Guess {} is {}A{}B.".format(c, strize(_guess), A, B))
        
        if (A, B) == (4, 0):
          print("{}th guesses to find answer".format(c))
          return c

        c = c + 1
        z = narrow(z, _guess, A, B)
        print("Remaining possible answer: {}".format(len(z)))

# plan to multi-threading

if __name__ == "__main__":

    t = 100
    p = 0
    for i in range(1,t+1):
      p = p + guess(i)
      
    print("Average guess count is {}".format(p/t))