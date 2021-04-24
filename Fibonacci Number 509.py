def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    lisp = list()
    lisp.append(0)
    lisp.append(1)
    i = 2
    while (True):
        lisp.append(lisp[i-1] + lisp[i - 2])
        if i == n:
            break
        else:
            i += 1
    return (lisp[n-1]+lisp[n-2])

n = 13
print(fib(n))