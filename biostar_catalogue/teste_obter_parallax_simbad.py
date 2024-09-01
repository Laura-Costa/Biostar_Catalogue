from astropy.coordinates import SkyCoord
from astroquery.simbad import Simbad

# Add to the default field returned by Simbad:
Simbad.add_votable_fields('plx', 'distance')

sim = Simbad.query_object('HD 146233')
# Prefer the parallax distance if available:
if not sim['PLX_VALUE'].mask[0]:
    print('------------------------------------------------------------------------------------')
    print("sim['PLX_VALUE'].mask: ", sim['PLX_VALUE'].mask)
    print('------------------------------------------------------------------------------------')
    print("sim['PLX_VALUE']: ", sim['PLX_VALUE'])
    print('------------------------------------------------------------------------------------')
    print("sim['PLX_VALUE'].mask[0]: ", sim['PLX_VALUE'].mask[0])
    print('------------------------------------------------------------------------------------')
    # Parallax distance:
    print("  Parallax distance is {:0.1f} pc.".format(1000. / sim['PLX_VALUE'][0]))
# but if no parallax we'll take any other distance:
elif not sim['Distance_distance'].mask[0]:
    print("  Distance from reference {} is {} {}.".format(sim['Distance_bibcode'][0],
                                                          sim['Distance_distance'][0],
                                                          sim['Distance_unit'][0]))
else:
    print("  No distance available in Simbad.")