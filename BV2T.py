from __future__ import print_function, division
from PyAstronomy import pyasl

b = pyasl.BallesterosBV_T()

bv = 0.652

# Convert B-V into effective temperature
teff = b.bv2T(bv)
print("B-V = {0:4.2f} mag -> Teff = {1:4.0f} K".format(bv, teff))

# Convert effective temperature into B-V color
teff = 5678.4277
bv = b.t2bv(teff)
print("Teff = {0:4.0f} K -> B-V = {1:4.2f} mag".format(teff, bv))
