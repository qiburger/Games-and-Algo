__author__ = 'qi'

import math

def bi2dec(n, sig):
     #To make sure the user inputs are of the right type
    if isinstance(int(n), (int, long)) and (sig in ["yes", "no"]):
        decimal_out = 0

        #Find the number of digits in n
        binary_length = len(n)


        if sig == "no":
            for i in range(binary_length):
                digit = int(n[(binary_length-i-1)])
                if digit in [0, 1]:
                    decimal_out += (digit * 2**i)
                else:
                    print "Please enter a binary number"
                    return False

        else:
            for i in range(binary_length-1):
                digit = int(n[(binary_length-i-1)])
                if digit in [0, 1]:
                    decimal_out += (digit * 2**i)
                else:
                    print "Please enter a binary number"
                    return False
            decimal_out += - int(n[0]) * 2 ** (binary_length - 1)

        print decimal_out
    else:
        print "Error!"
        return False


if __name__ == '__main__':
    n= raw_input("Enter a binary number:").strip()
    sig = raw_input("Is is signed (2c)? Answer 'yes' or 'no'")
    bi2dec(n, sig)