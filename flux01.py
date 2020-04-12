#!/usr/bin/env python
# NGC 2146

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
rad2as=180.0/math.pi*3600
#E_ion_ev=13.6	# [eV]
#E_bnd_ev=4.52	# [eV]
XH=3.0e20
#  --- parameter -------------------------------	#
as2pc=35.0
px2as=0.25
bm2as2=2.5*1.9
bm2px=bm2as2/(px2as**2)


def surf_den_skmt99(S_CO_JyBmMS,incli,D_Mpc,px,type):
	n_bm=px/bm2px
	n_as=px*px2as**2
	S_CO=S_CO_JyBmMS/1000*n_bm
	I_CO=S_CO/n_as
	cos_i=math.cos(incli/180.0*math.pi)
	sd_Msunpc2=(5.0e2*cos_i*I_CO)*XH
	M_gas_Msun=(1.18e4*D_Mpc**2*S_CO)*XH
	M_gas=M_gas_Msun*Msun
	print '%.2e' %I_CO,"[Jy km/s as-2]", '%.2e' %S_CO,"[Jy km/s]",'%.0f' %n_as,"[as2]",'%.0f' %n_bm,"[beam]",'%.2e' %sd_Msunpc2,"[Msun/pc2]",'%.2e' %M_gas_Msun,"[Msun]",type
	return sd_Msunpc2,M_gas


sd=surf_den_skmt99(9.0051E-06,89,7.7,75640,"n3628 conti rms")
sd=surf_den_skmt99(1.0408E-05,89,7.7,94184,"n3628 conti rms")
sd=surf_den_skmt99(1.9705E-05,89,7.7,71148,"n3628 conti rms")
sd=surf_den_skmt99(3.5077E-04,89,7.7,104648,"n3628 conti rms")
print "------------"

# --- reference -------------------------------	#
# Sakamoto et al. 1995, AJ, 110, 2075

exit

