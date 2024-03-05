# Find the greatest common denominator of two numbers
# using Euclid's algorithm

"""
Example

--------------------------
GCD(20,8)
a  |  b | remainder
--------------------------
20 |  8 |     4
--------------------------
 8 |  4 |     0
--------------------------

"""


def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a


# try out the function with a few examples
print(gcd(60, 96))
print(gcd(20, 8))
