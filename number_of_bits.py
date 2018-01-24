##########################################################
# Several ways to count bits in Python 3.6
# JW 2018
##########################################################

# classic bit shift
def number_of_bits1(n):
    x = 0
    while n > 0:
        x += n & 1
        n >>= 1
    return x

# bin.count method
def number_of_bits2(n):
    x = bin(n).count("1")
    return x

# divide by 2 method
def number_of_bits3(n):
    x = 0
    while n > 0:
        if (n%2 > 0):
            x = x + 1
        n = n//2
    return x

#for 8 bit number n
def number_of_bits4(n):
    x = 0
    for p in range(8):
        x += (n>>p) & 1
    return x


# test for 100 (bin: ‭0110 0100‬)
print (number_of_bits1(100))
print (number_of_bits2(100))
print (number_of_bits3(100))
print (number_of_bits4(100))
