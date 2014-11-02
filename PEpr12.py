def Triangular(n):
    a= 1    #a is the total number of factors of b
    b= 1    #b is the triangular number
    while a<n:
       c=b*(b+1)/2  #The next triangular number
       y=int(c**.5)
       Factors= [x for x in range(1,y) if c%x == 0]
       a=len(Factors)*2
       b+=1
    return c
print (Triangular(500))
           
           
        
        
