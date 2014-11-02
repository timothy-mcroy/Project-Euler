import math

def factorialDigitSum(n):
    """This problem was particularly difficult to solve in a clever way.  So I used the math library.  """
    a= str(math.factorial(n))
    return sum([int(i) for i in a])
