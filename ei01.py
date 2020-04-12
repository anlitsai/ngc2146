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
def EI(norm,radius_kpc, theta_arcmin, z ,galaxy):
	D_cm=radius_kpc*2*1000*pc
	theta_rad=theta_arcmin/60.0*math.pi/180.0
	Da=D_cm/theta_rad
	a=1.0e-14/(4*math.pi*(Da*(1+z))**2)
	ei=norm/a
	print "------------------------------------"
	print "norm = ", norm
	print "radius = ", radius_kpc, "[kpc]"
	print "theta = ", theta_arcmin, "[arcmin]"
	print "Angular diameter distance = ", Da, "[cm]"
	print "redshift = ", z
	print "galaxy = ", galaxy
	print "EI = int(n_e n_H dV)=", '%.2e' %ei, "[cm-3]"
	return ei
ei_n2146=EI(1.0e-4,6.3,1.8,0.003,"NGC 2146")
ei_n2146=EI(2.0e-4,6.3,1.8,0.003,"NGC 2146")
ei_n2146=EI(3.0e-4,6.3,1.8,0.003,"NGC 2146")
ei_n2146=EI(4.0e-4,6.3,1.8,0.003,"NGC 2146")
ei_n2146=EI(5.0e-4,6.3,1.8,0.003,"NGC 2146")
ei_n2146=EI(5.0e-4,2,25.0/60,0.003,"NGC 2146")
ei_n3628=EI(1.0e-4,0.5,15.0/60,0.0028,"NGC 3628")

# --- reference -------------------------------	#
# http://en.wikipedia.org/wiki/Angular_diameter_distance
# http://en.wikipedia.org/wiki/Degree_(angle)
# http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/manual/XSmodelMekal.html

print "------------------------------------"
exit

