def HorizontalCalculation(Matrix):
    Accum = []
    for k in Matrix:
        for i in range(3,len(k)):
            
            g= k[i]* k[i-1]*k[i-2]* k[i-3]
            Accum +=[g]

    return max(Accum)


def BackSlash(Matrix):
    Accum =[]
    for k in range(len(Matrix)-3):
        for i in range(len(Matrix[k])-3):
            Accum +=[ Matrix[k][i]*Matrix[k+1][i+1]*Matrix[k+2][i+2]*Matrix[k+3][i+3]]

    return max(Accum)


def ForwardSlash(Matrix):
    Accum =[]
    for k in range(3,len(Matrix)):
        for i in range(len(Matrix[k])-3):
            Accum +=[ Matrix[k][i]*Matrix[k-1][i+1]*Matrix[k-2][i+2]*Matrix[k-3][i+3]]

    return max(Accum)
def VerticalCalculation(Matrix):
    Accum =[]
    for k in range(len(Matrix)-3):
        for i in range(len(Matrix[k])):
            Accum +=[ Matrix[k][i]*Matrix[k+1][i]*Matrix[k+2][i]*Matrix[k+3][i]]

    return max(Accum)
def readfile():
    Matrix = open('Grid.txt', 'r')
    Accum =[]
    for x in Matrix:
        Accum += [[int(i) for i in x.split()]]
    return Accum

a=readfile()
print (HorizontalCalculation(a))
print ("^Horizontal Calculation ^")
print ("v Backslash Calculation v ")
print (BackSlash(a))
print ("v Forwardslash Calculation v")
print (ForwardSlash(a))
print ("v Verticalslash Calculation v")
print (VerticalCalculation(a))

