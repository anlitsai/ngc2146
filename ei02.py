#!/usr/bin/env python
# /iapetus/thesis/phd/calculation/ei02.py

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
pc=3.26*c*365*86400	# [cm]
kpc=pc*1.0e3	# [cm]
ev=1.6e-12	# [erg]
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
Msun=1.99e33 # solar mass
Msun_pc2=Msun/pc**2
Lsun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24	# [g]
E_ion_ev=13.6	# [eV]
E_bnd_ev=4.52	# [eV]
#  ------------------------------------	#
def EI(norm,radius_kpc, theta_arcmin, z ,galaxy,fill,kT_kev):
	R=radius_kpc*1000*pc
	D=R*2
	theta_rad=theta_arcmin/60.0*math.pi/180.0
	Da=D/theta_rad
	a=1.0e-14/(4*math.pi*(Da*(1+z))**2)
	ei=norm/a
	V=4.0/3*math.pi*R**3
	Vf=V*fill
	n_e=math.sqrt(ei/Vf)
	kT=kT_kev*1000*ev
	p=2*n_e*kT
	M=n_e*m_p*Vf/Msun
	E=3*n_e*kT*Vf
	print "------------------------------------"
	print "galaxy = ", galaxy
	print "------------------------------------"
	print "norm = ", '%.2e' %norm
	print "radius = ", radius_kpc, "[kpc]"
	print "theta = ", '%.2e' %theta_arcmin, "[arcmin]"
	print "Angular diameter distance = ", '%.2e' %Da, "[cm]"
	print "redshift = ", z
	print "EI = int(n_e n_H dV)= ", '%.2e' %ei, "[cm-3]"
	print "filling factor = ", fill
	print "volume = ", '%.2e' %V, "[cm3]"
	print "kT = ", kT_kev, "[keV]"
	print "plasma density = ", '%.2e' %n_e, "[cm-3]"
	print "plasma pressure = ", '%.2e' %p, "[dyne cm-2]"
	print "plasma mass = ", '%.2e' %M, "[Msun]"
	print "plasma thermal energy = ", '%.2e' %E, "[erg]"
	return ei

print "------------------------------------"
ei_n2146=EI(1.0e-4,6.3,1.8,0.003,"NGC 2146",0.01,0.5)
ei_n2146=EI(3.0e-4,6.3,1.8,0.003,"NGC 2146 | possible",0.01,0.5)
ei_n2146=EI(5.0e-4,6.3,1.8,0.003,"NGC 2146",0.01,0.5)
ei_n2146=EI(5.0e-4,6.3,1.8,0.003,"NGC 2146",1.0,0.5)
ei_n2146=EI(5.0e-4,2.0,25.0/60,0.003,"NGC 2146",0.01,0.5)
ei_n2146=EI(3.0e-4,2.0,25.0/60,0.003,"NGC 2146",0.01,0.5)
print "------------------------------------"
ei_n3628=EI(1.0e-4,0.5,15.0/60,0.0028,"NGC 3628",0.01,0.3)
ei_n3628=EI(1.0e-4,0.5,15.0/60,0.0028,"NGC 3628",0.01,0.5)
ei_n3628=EI(1.0e-4,0.5,15.0/60,0.0028,"NGC 3628 | possible",1.0,0.3)
ei_n3628=EI(1.0e-4,0.5,15.0/60,0.0028,"NGC 3628",1.0,0.5)
ei_n3628=EI(1.0e-4,1.0,30.0/60,0.0028,"NGC 3628",0.01,0.3)
ei_n3628=EI(1.0e-4,1.0,30.0/60,0.0028,"NGC 3628",0.01,0.5)
ei_n3628=EI(1.0e-5,1.0,30.0/60,0.0028,"NGC 3628",0.01,0.5)
ei_n3628=EI(1.0e-6,1.0,30.0/60,0.0028,"NGC 3628",0.01,0.5)
print "------------------------------------"

# --- reference -------------------------------	#
# http://en.wikipedia.org/wiki/Angular_diameter_distance
# http://en.wikipedia.org/wiki/Degree_(angle)
# http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/manual/XSmodelMekal.html

exit

