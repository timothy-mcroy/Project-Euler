def Lp(n):
    """This program scans a list of integers (that aren't separated by lines)
    and tries to find the largest product of 13 adjacent numbers."""
    a= 0
    n=[int(i) for i in list(str(n))]
    for i in range(len(n)):
        if  i+13==len(n):
            break
        p=1
        for j in range(13):
            if n[i+j] == 0:
                break
            p*=n[i+j]
        if p > a :
            a = p
    return a

