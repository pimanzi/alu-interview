#!/usr/bin/python3
"""This script is all about how to  use python with concepts of mathematics to solve a problem for instance in this scenarion we are gonna use factors"""
 

def minOperations(n):
    """function to solve the problem"""
    if n < 0 :
        return 0
    operations= 0
    factor=2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations


 