#!/usr/bin/python3
"""
This script demonstrates how to use Python and mathematical concepts
to solve a problem. In this scenario, we use prime factorization.
"""

def minOperations(n):
    """Calculates the minimum number of operations needed to result
    in exactly n 'H' characters in the file.
    
    Args:
        n (int): The target number of 'H' characters.
    
    Returns:
        int: The fewest number of operations needed to achieve exactly n 'H' 
             characters, or 0 if it is impossible to achieve.
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
