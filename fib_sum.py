def sum_even_fibonacci(limit):
    fibs = [0,1]
    sum_even = 0
    for num in range(0,limit+1):
        fib_sum = fibs[num-1]+ fibs[num-2]
        if num>= 2:
            fibs.append(fib_sum)
    for fibo in fibs :
        if fibo <= limit and fibo % 2 ==0:
            sum_even += fibo
    return sum_even
            


    