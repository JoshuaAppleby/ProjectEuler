#Project Euler, Problem 5
#Smallest multiple

def smallmultiple(N):
    """2520 is the smallest number that can be divided by each of the 
        numbers from 1 to 10 without any remainder.
        What is the smallest positive number that is 
        evenly divisible by all of the numbers from 1 to 20?
    """
    answer = 1
    list = []
    for i in range(2,N):
        list.append(i)
    
    for i in range(0, len(list)):
        for j in range(1, i+1):
            if list[i] % list[i-j] == 0:
                list[i] = int(list[i] / list[i-j])
   
    for i in range(0, len(list)):
        answer = answer * list[i]
    return answer

print(smallmultiple(20))