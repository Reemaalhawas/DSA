def check_prime(n):
    if n <=1 : 
        return False 
    for i in range(2, n):
        if i % 2 == 0 :
            return False 
    return True 


# Time complexity O(n) the loop will run from 2 to n-1 times 


# Optimal approach using square root : 
import math 
def check_prime_sqr(n): 
    if n <= 1 : 
        return False 
    for i in range (2 , int(math.sqrt(n)+1)):
        if n % i ==0 : 
            return False 
    return True 

# Time Complexity is O(√n)

