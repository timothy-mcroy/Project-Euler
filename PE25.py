"""PE 25
Currently not finished with this one.
"""

def pe25(n):
    """Here, n is the number of digits we're checking for"""
    a=b=c=1
    d=3
    while c<n:
        if (a+b)>10:
            c+=1
        a,b = b, (a+b)%10
        d+=1
    return d
