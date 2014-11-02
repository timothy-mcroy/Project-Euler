def pytrip(n):
    for a in range(1, n+1):
        for b in range(a+1, n-a+1):
            c= n-a-b
            if c > a and c > b:
                if a+b+c == n and (a**2 + b**2 ==c**2):
                    return (a,b,c), a*b*c
            
