""""
Problem statement
You are given a number ’n’.
Find the number of digits of ‘n’ that evenly divide ‘n’.
Note:
A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.
Example:
Input: ‘n’ = 336
Output: 3
Explanation:
336 is divisible by both ‘3’ and ‘6’. Since ‘3’ occurs twice it is counted two times.


"""
def count_digits(n):
    count = 0
    num = n  
    
    while num > 0:
        digit = num % 10  # Extract last digit
        if digit != 0 and n % digit == 0:  # Check valid divisor
            count += 1
        num //= 10  # Remove last digit
    
    return count

# Test 
n = 235 
print(count_digits(n)) 

 

