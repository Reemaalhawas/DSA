"""
Problem statement
Check whether a given number ’n’ is a palindrome number.

Note :
Palindrome numbers are the numbers that don't change when reversed.
You don’t need to print anything. Just implement the given function.
Example:
Input: 'n' = 51415
Output: true
Explanation: On reversing, 51415 gives 51415.
"""
def check_palindrome(n):
    num = n 
    rev = 0 
    while num > 0 :
        dig = num  % 10 
        rev =  ( rev * 10 )  + dig 
        num = num // 10 
    return  rev == n 

print(check_palindrome(51415))
print(check_palindrome(51416))