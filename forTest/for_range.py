# for i in range(2,5):
#     print(i)



def fib(n):
    if n ==1:
        return [0]
    if n == 2:
        return [0,1]
    if n >= 3:
        fibs = [0,1]
        print(fibs[-1])
        print(fibs[-2])
        for i in range(3,n):
            fibs = fibs.append(fibs[-2]+fibs[-1])

        return fibs


print(fib(3))
