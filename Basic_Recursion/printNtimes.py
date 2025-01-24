"""
Print numbers from 1 to n without the help of loops.
 You only need to complete the function printNos() that takes n as a parameter and prints the number from 1 to n recursively.

Note: Don't print any newline, it will be added by the driver code.

"""
def printNos(n: int) -> None:
    if n < 1 : # Base case 
        return 
    printNos(n-1)
    print(n , end=" ")

printNos(4)

# Time complexity : 
# O(n) 


# print name n times : 

def printName(s : str , n : int ) -> None : 
    if s == ""  or n < 1 : 
        return 
    printName(s , n-1)
    print(s , end=" ")

# Time complexity is O(n)

printName(" Reema " , 5)
