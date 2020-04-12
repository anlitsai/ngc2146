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
#  --- parameter ------------------------------	#
# http://en.wikipedia.org/wiki/Angular_diameter_distance
# http://en.wikipedia.org/wiki/Degree_(angle)
# http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/manual/XSmodelMekal.html
def H0(v_kms,D_Mpc):
	h0=v_kms/D_Mpc
	print v,"km/s", D_Mpc, "Mpc", h0,"km/s/Mpc"
	return h0

def Z(v_kms):
	z=v_kms*1.0e5/c
	print v_kms,"km/s ; z =",z
	return z

def D(H0, v_kms):
	d=v_kms/H0
	z=v_kms*1.0e5/c
	print "H0 =", H0, "km/s/Mpc; z =",z, "v =",v_kms,"km/s ; D =", '%.3f' %d, "Mpc"
	return d
d=D(70.8,840.0)
d=D(71,840.0)
d=D(72,840.0)
d=D(73,840.0)
d=D(74,840.0)
d=D(75,840.0)

# --- reference -------------------------------	#

print "------------------------------------"
exit

