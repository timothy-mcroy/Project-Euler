def pe1(n):
    """Input should be a natural number"""
    assert type(n)== type(5) #Must be an integer
    assert n>0               #Must be a natural number
    total = 0
    for i in range(3, n, 3):
        total+=i
    for i in range(5,n,5):
        if i%3!=0:    #making sure that we don't double count
            total+=i
    return total
