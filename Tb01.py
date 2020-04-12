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
rad2as=180.0/math.pi*3600
#E_ion_ev=13.6	# [eV]
#E_bnd_ev=4.52	# [eV]
c_cms=2.99792458e10
HCN_1_0_lamda=c_cms/88.63e9
ff_cont_n2146_lamda=c_cms/88.644e9
ff_cont_n3628_lamda=c_cms/94.667e9
Kb=1.38e-16	# [erg/K]
Jy=1.0e-23	# [erg/s/cm2/Hz]
mJy=Jy*1000	# [erg/s/cm2/Hz]
#  --- parameter -------------------------------	#
n3628_theta_maj_as=3.01
n3628_theta_min_as=2.36
n2146_theta_maj_as=3.3
n2146_theta_min_as=2.8


def Tb(lamb_mm, theta_maj_as, theta_min_as, S_mJy_bm,type):
	solidang_as2=1.133*theta_maj_as*theta_min_as
	Tb=13.6*lamb_mm**2/(theta_maj_as*theta_min_as)*S_mJy_bm
	print "solid angle =",'%.2f' %solidang_as2,"[as^2], S =",'%.2e' %S_mJy_bm,"[mJy/bm], Tb =", '%.4e' %Tb,"[mK] |", type
	return Tb


print "------------"
print "NMA"
print "------------"
T=Tb(2.7,n3628_theta_maj_as,n3628_theta_min_as,9.86,"n3628")
T=Tb(2.7,n3628_theta_maj_as,n3628_theta_min_as,10.5,"n3628")
T=Tb(2.7,3.93,3.79,2.05e6,"")
T=Tb(1.3,3.93,3.79,1.2,"")
T=Tb(2.7,n3628_theta_maj_as,n3628_theta_min_as,2.12e6,"n3628")
T=Tb(2.7,n3628_theta_maj_as,n3628_theta_min_as,8.01e6,"n3628 moment0 total")
T=Tb(2.7,n3628_theta_maj_as,n3628_theta_min_as,82.01e6,"n3628")
T=Tb(2.7,n3628_theta_maj_as,n3628_theta_min_as,82.01e3,"n3628 chan total")
T=Tb(2.7,n3628_theta_maj_as,n3628_theta_min_as,648.3,"n3628 moment0 noise")
T=Tb(2.7,n3628_theta_maj_as,n3628_theta_min_as,4.93,"n3628 chan noise")
T=Tb(2.7,n2146_theta_maj_as,n2146_theta_min_as,5.7,"n2146 chan noise")
T=Tb(2.7,n2146_theta_maj_as,n2146_theta_min_as,1.8e6,"n2146 total")
T=Tb(2.7,n2146_theta_maj_as,n2146_theta_min_as,585,"n2146 moment0 noise")
T=Tb(HCN_1_0_lamda,12.0,9.0,144,"example from BIMA/OVRO observations of Comet C/1999 S4")
T=Tb(ff_cont_n2146_lamda,n2146_theta_maj_as,n2146_theta_min_as,3.732E+04,"n2146 3mm, not sure")
#T=Tb(ff_cont_n3628_lamda,n3628_theta_maj_as,n3628_theta_min_as,,"n3628 3mm, not sure")
T=Tb(1,1,1,1,"example from NMA page")
#print "------------"
#print "something wrong..."
print "------------"
print "Tb(lamb_mm, theta_maj_as, theta_min_as, S_mJy)"
print "------------"




# --- reference -------------------------------	#
# Sakamoto et al. 1995, AJ, 110, 2075
# http://www.nro.nao.ac.jp/~nma/status/status-e.html#sensitivity


exit

