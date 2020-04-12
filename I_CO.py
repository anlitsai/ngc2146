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
X_CO2H2=1.4/3.0
H22mol=1.36
XH=X_CO2H2*H22mol
#  --- parameter ------------------------------	#
px2as=0.2
v_rms_kms=11.16
v_rms=v_rms_kms*1.0e5
#  --------------------------------------------	#
def I_CO(S_CO_JyBmMS,bm_maj,bm_min,px,incli,D_Mpc,type):
	bm_as2=bm_maj*bm_min
	n_as=px*px2as**2
	n_bm=n_as/bm_as2
	S_CO=S_CO_JyBmMS/1000*n_bm
	I_CO=S_CO/n_as
	cos_i=math.cos(incli/180.0*math.pi)
	sd_Msunpc2=(5.0e2*cos_i*I_CO)*XH
	sd=sd_Msunpc2*Msun_pc2
	z_gas_pc=(v_rms**2/(2*math.pi*G*sd))/pc
	z_gas_kpc=z_gas_pc/1000
	M_gas_Msun=(1.18e4*D_Mpc**2*S_CO)*XH
	M_gas=M_gas_Msun*Msun
	print '%.1e' %sd,"[g/cm2]",'%.0f' %sd_Msunpc2,"[Msun/pc2] (z =",'%.2f' %(z_gas_kpc),"kpc)",'%.1e' %M_gas_Msun,"[Msun]",type
	return sd_Msunpc2,M_gas
print "-----------------------------------------------------------"
sd=I_CO(4.0548E+03,3.01,2.36,92502,89,7.7,"momnt, NGC3628")
#sd=I_CO(780,3.6*20,3.6*3,1,80,3.25,"image, M82 | Walter et al. 2002")
sd=I_CO(780.0,72,10.8,1,80.0,3.25,"image, M82 | Walter et al. 2002")
print "-----------------------------------------------------------"
def I_CO_mass(S_CO_JyBmMS,bm_maj,bm_min,px,D_Mpc,type):
	S_CO_Jy_kms=
	M_gas_msun=1.2e4*S_CO_Jy_kms*D_Mpc**2
print "-----------------------------------------------------------"
print "-----------------------------------------------------------"

