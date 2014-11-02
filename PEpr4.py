def palindrome(n):
    g= 10**n -1
    
    list1 = []
    def checker(a):
        a= list(str(a))
        b =list(a)
        a.reverse()
        return a == b

    def hardpart(g):
        for i in range(g, -1, -1):
            for j in range(g, -1, -1):
                if checker(i*j):
                    list1.append(i*j)
                    break
    hardpart(g)
    return max(list1)
