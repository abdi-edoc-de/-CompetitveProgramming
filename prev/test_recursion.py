def fact(n):
    # ans = n * fact(n-1)
    if n ==1:
        return 1
    return n * fact(n-1)
print(fact(3))