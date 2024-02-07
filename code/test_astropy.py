import astropy.units as u
from astropy.coordinates import SkyCoord
gc = SkyCoord(l=0*u.degree, b=45*u.degree, frame='galactic')
gc.fk5
