# Fibonacci numbers
# each new number is the sum of the two previous numbers
# write a program that lists Fibonacci numbers from 1-55

fibonacci = [1]
fib = ''
a = 0
b = 1

for i in range(9):
    fib = a + b
    a = b
    b = fib
    fibonacci.append(fib)
print(fibonacci)