''' (c) 02 Aug. 2023, Fekete Balázs Valér, fbv81bp@[outlook.hu|gmail.com] '''

# My own modulo multiplier algorithm based on number system conversion.
# Disclaimer: idk, if this exists elsewhere, but it is a simple and
# clearly hardware friendly algorithm.

def FBV_mod_mult(x,y,m): # A multi-digit might even make use of Kartasuba, idk.
    accu = 0
    to_double = x
    while y > 0:
        if to_double > m:
            to_double -= m
        if y & 1 > 0:
            accu += to_double
            if accu > m:
                accu -= m
        to_double *= 2
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
