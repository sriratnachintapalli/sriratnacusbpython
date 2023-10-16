
# nth term of Fibonacci series using recursion
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Reading number of terms
term = int(input("Which term of Fibonacci series? "))

result = fib(term)
print("\n%dth term of Fibonacci series is: %d" %(term, result))
