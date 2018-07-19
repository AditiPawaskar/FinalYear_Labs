import skfuzzy as fuzz
import numpy as np

a = np.r_[0,0,0,0.3,0.7,1,0.9]
b = np.r_[0,0,1,0.2,0.1,0,0]

c = np.r_[1,2,3,4,5,6,7]

z,mfz  = fuzz.fuzzymath.fuzzy_and(c,a,c,b)
print(z)
print(mfz)
