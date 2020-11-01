def sumatorio(n):
    if n != 0:
        return n + sumatorio(n-1)
    else:
        return 0
def fact(n):
    if n != 1:
        return n * fact(n-1)
    else:
        return 1

print(sumatorio(3))
print(fact(5))
