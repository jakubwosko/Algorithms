from __future__ import division # nedded for float division
import math   # import math module
import click
import texttable as tt

#####################################################################
# is_prime(A) returns 1 when A is prime or 0 when A is complex number
# brute force method is used with 6k+-1 to sqr N
#####################################################################

def is_prime(my_num):

    if my_num == 3 or my_num == 5:return 1
    if my_num % 2 == 0 or my_num % 3 == 0 or my_num % 5 == 0:return 0

    sqr=int(math.sqrt(my_num))
            
    for x in range(6, sqr+2, 6):
        if my_num % (x-1) == 0 or my_num % (x+1) == 0:
            return 0
    return 1

def number_of_bits(n):
    x = bin(n).count("1")
    return x

#####################################################################

tab = tt.Texttable()
headings = ['prime','binary','#no bits','bits cumulatively','distance']
tab.header(headings)

scope = 100
sumnb = 0
nb = 0
distance = 0
old_sumnb = 0

for i in range (3,scope):
    if is_prime(i)==1:
        nb = number_of_bits(i)
        i_bin = bin(i)
        sumnb = sumnb + nb
        distance = sumnb - old_sumnb
        old_sumnb = sumnb

        row = (i,i_bin,nb,sumnb,distance)
        tab.add_row(row)

s = tab.draw()
print (s)
