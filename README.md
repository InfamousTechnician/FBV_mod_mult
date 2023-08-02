# FBV_mod_mult.py
My hardware friendly modular multiplication, that i just invented in the middle of the night, and now i go and finally sleep.

## Actually...
This one looks roughly the same: https://www.geeksforgeeks.org/multiply-large-integers-under-large-modulo/
My improvement on this one would be then, IFF we are doing cryptography, and thus are dealing with multiplicand as well as multiplier being smaller than the modulus, then the modulo divisions of this article can practically be replaced by conditional subtractions, as presented in my code.
