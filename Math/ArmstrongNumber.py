"""
you are given an integer 'n'. Return 'true' if 'n' is an Armstrong number, and 'false' otherwise.
An Armstrong number is a number (with 'k' digits) 
such that the sum of its digits raised to 'kth' power is equal to the number itself.
 For example, 371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.

"""
def count_digits(n):
    count = 0
    num = n
    while num > 0:
        count += 1
        num //= 10
    return count

def is_armstrong(n):

    num = n
    num_digits = count_digits(n)  
    sum_of_powers = 0
    
    
    while num > 0:
        digit = num % 10  # Extract last digit
        sum_of_powers += digit ** num_digits  
        num //= 10  # Remove last digit
    
    return sum_of_powers == n

print(is_armstrong(371))
print(is_armstrong(372))