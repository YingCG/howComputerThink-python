"""
Converting Hexadecimal to Decimal

Hexadecimal or "base 16" uses all of of the number 0-9, plus a few others to signify higher numbers:
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15

Therefore, the number 'D' in hexadecimal would be 13 in decimal
The nnumber '1A' in hexadecimal would be 26 in decimal. 
Just like we have the "ten" place in base 10, hexadecimal has the "sixteens" place. So 1A would be 16 + 10 or 26

And just like decimal has the "hundreds place (because 10 * 10 is 100)"
Hexadecimal has the "256" place (because 16 * 16 is 256)
'ABC' in hexadecimal is (256 * 10) + (16 * 11) + (1 * 12) or 2,748
 """

hexNumbers = {
    "0": 0,
    "1": 1,
    "2": 3,
    "3": 4,
    "4": 5,
    "5": 6,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
}

# converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None


def hexToDec(hexNum):
    for char in hexNum:
        if char in hexNumbers:
            return None


# Test case 1 --> 10
hexToDec("A")

# Test case 2 --> 0
hexToDec("O")

# Test case 3 --> 27
hexToDec("1B")

# Test case 4 --> 960
hexToDec("3C0")

# Test case 5 --> None
hexToDec("A6G")

# Test case 3 --> None
hexToDec("ZZTOP")
