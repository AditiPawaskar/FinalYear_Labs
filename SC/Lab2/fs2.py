import skfuzzy as fuzz
import numpy as np

aa = np.r_[0,0,0,0.3,0.7,1,0.9]
bb = np.r_[0,0,1,0.2,0.1,0,0]

cc = np.r_[1,2,3,4,5,6,7]



z,mfz  = fuzz.fuzzymath.fuzzy_and(cc,aa,cc,bb)
print("A intersection B")
print(z)
print(mfz)

y,mfy  = fuzz.fuzzymath.fuzzy_or(cc,aa,cc,bb)
print("A union B")
print(y)
print(mfy)

# for complement of fuzzy set aa
mfx = fuzz.fuzzymath.fuzzy_not(aa)
print("A complement")
print(cc)
print(mfx)

# for complement of fuzzy set bb
mfw = fuzz.fuzzymath.fuzzy_not(bb)
print("B complement")
print(cc)
print(mfw)

v,mfv = fuzz.fuzzymath.fuzzy_sub(cc,aa,cc,bb)
print(" A-B:")
print(v)
print(mfv)

print("De Morgans Law : (A U B)' = A' intersection B' ")
mf_lhs = fuzz.fuzzymath.fuzzy_not(mfy)
rhs,mf_rhs = fuzz.fuzzymath.fuzzy_and(cc,mfx,cc,mfw)
print("LHS :")
print(mf_lhs)
print("RHS :")
print(mf_rhs)
print("Hence proved")



   