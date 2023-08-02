# My own modulo multiplier algorithm based on number system conversion.
# Disclaimer: idk, if this exists elsewhere, but it is a simple and
# clearly hardware friendly algorithm. Both the comparator and the
# subtractor work with constant 'm' on one input, and their other input can
# be used alternately between 'x' and the 'accu'. y>0 can be a
# fixed length counter in case of known cryptographic applications, so no
# 3rd comparator is actually needed. While doubling and dividing by 2s is
# just plain shifting left and right.

def FBV_mod_mult(x,y,m): # A multi-digit might even make use of Kartasuba, idk.
    accu = 0
    while y > 0:
        if x > m:
            x -= m
        if y & 1 > 0:
            accu += x
            if accu > m:
                accu -= m
        x *= 2
        y //= 2
    return accu

m = 16381
x = 14532
y = 3769

print(x*y%m)
print(FBV_mod_mult(x,y,m))
print()

m = 16369
x = 6734
y = 5305

print(x*y%m)
print(FBV_mod_mult(x,y,m))
print()

m = 16411
x = 10356
y = 15320

print(x*y%m)
print(FBV_mod_mult(x,y,m))
print()

'''
Dump>>>
9425
9425

6712
6712

8783
8783
<<<
'''