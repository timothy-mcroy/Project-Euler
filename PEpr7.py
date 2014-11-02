def primegen(n):
    p=[2,3,5]
    def checkprime(list1, b):
        a=list1[:int(len(list1)**.5)+1]  #going from the first prime to sqrt(n), because factoring
        if not any( b % item == 0 for item in a):   #Using a generator expression allows for the calculations to stop immediately after finding a prime.
            list1.append(b)
        else:
            checkprime(list1,b+2)
    while len(p) < n:
        checkprime( p, p[-1]+2)
        
    return p[-1]
        
