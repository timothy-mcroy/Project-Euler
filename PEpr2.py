def foo(n):
        """ n is to be the limit on the size of the fibonacci numbers"""
        assert type(n)==type(5)
        assert n>2
        p=[1,2]
        while p[-1]<n:
                a= p[-1] + p[-2]
                p.append(a)
        g= [p[i] for i in range(1,len(p),3)]  # Every third fibo number is even
        return sum(g)                         # We use this property to skip extraneous modulus operations.
