#!/usr/bin/env python

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
pc=3.26*c*365*86400
kpc=pc*1.0e3
ev=1.6e-12
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
Msun=1.99e33 # solar mass
Msun_pc2=Msun/pc**2
Lsun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24
E_ion_ev=13.6	# [eV]
E_bnd_ev=4.52	# [eV]
#  --000000000000------------------------------	#
def HR(S,H,note):
	hr=(H-S)/(H+S)
	print "H =",H,"[photons], S =", S, "[photons], HR =",'%.3f' %hr,note
	return hr
n3628core=HR(1.1621e-05,7.901e-06,"| raym+pow, grp")
n3628core=HR(1.1554e-05,7.9445e-06,"| raym+pow, grp_2")
n3628core=HR(1.1625e-05,7.9433e-06,"| mekal+pow, grp")
# --- reference -------------------------------	#
# http://en.wikipedia.org/wiki/Angular_diameter_distance
# http://en.wikipedia.org/wiki/Degree_(angle)
# http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/manual/XSmodelMekal.html

print "------------------------------------"
print "test93"
print "------------------------------------"
n3628outcore=HR(0.00018491,8.6727e-06,"| vmekal+pow, test93 outcore grp")
n3628core=HR(1.3224e-05,8.0542e-06,"| vmekal+pow, test93 core grp")
print "------------------------------------"
print "test98"
print "------------------------------------"
n3628core=HR(1.1755e-05,7.2446e-06,"| vraym+pow, test98 core grp")


exit

