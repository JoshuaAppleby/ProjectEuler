#Project Euler, Problem 2
#Even Fibonacci numbers

def evenfibonacci(N):
    """Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
        By starting with 1 and 2, the first 10 terms will be:
        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
        By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
        find the sum of the even-valued terms.
    """
    num1 = 1
    num2 = 2
    fibsum = 0
    while (num1 <= N) and (num2 <= N):
        if num1 % 2 == 0:
            fibsum += num1
        if num2 % 2 == 0:
            fibsum += num2
        num1 += num2
        num2 += num1
    return fibsum

print(evenfibonacci(4000000))