import numpy as np
import skfuzzy as fuzz

# taking fuzzy sets A and B as user inputs

print("Enter elements of A")
a_x = input()
a_x = np.r_(a_x)
# print(a_x)

print("Enter memership values of corresponding elements of A")
a_mx = input()
a_mx = np.r_(a_mx)
# print(a_mx)

print("Enter elements of B")
b_x = input()
b_x = np.r_(b_x)
# print(b_x)

print("Enter memership values of corresponding elements of B")
b_mx = input()
b_mx = np.r_(b_mx)
# print(b_mx)


# LHS wrong
m,mfm = fuzz.fuzzymath.fuzzy_or(a_x, a_mx, b_x, b_mx)
print("Union:")
print(m)
print(mfm)

'''
n = fuzz.fuzzy_math.fuzzy_and(a_x, a_mx, b_x, b_mx)
print("Intersection:")
print(n)
print(mfn)
'''
