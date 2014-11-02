
def bestPath(n):
    """Uses a dynamic approach to solving Project Euler 18 and 67."""
    b=[]
    for i in n:
        b.insert(0,[int(j) for j in i.split()])
    
    DP = [max(b[0][i],b[0][i+1]) for i in range(len(b[0])-1)]
    for row in b[1:-1]:
        DP = [max(row[i]+DP[i], row[i+1]+DP[i+1]) for i in range(len(row)-1)]
    return (DP[0] + b[-1][0])
    

