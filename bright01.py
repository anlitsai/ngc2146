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
X=3.0/3.0
H=1.36
XH=X*H

# ---------------------------------------------	@
def T_K(S_Jy,freq_GHz,bm_as2):
	S=S_Jy*1.0e-23
	freq=freq_GHz*1.0e9
	lamb=c/freq
	bm=bm_as2*math.pi/(4*math.log(2))
	T=lamb**2*S/(2*k_B*bm)
	print T,"[K]"
	return T
t=T_K(1.0e4,115,9)

def T_NMA(S_mJy,lamb_mm,bm_as2):
	T=13.6*lamb_mm**2/bm_as2*S_mJy
	print '%.2f' %T,"[mK]"
	return T
t=T_NMA(10,2.6,9)

c1=1.0e23*2*1.0e-9**2/c**2*k_B
def B_Jy(freq_GHz,T):
	B=c1*freq_GHz**2*T
	print B
	return B
b=B_Jy(115,100)

def B(freq,T):
	lamb=c/freq
	b=2*freq**2/c**2*k_B*T/1.0e-23/freq
	print '%.2e' %b
	return b
b=B(1.0e15,1.0e4)
#def surf_den_flux(S_CO_JyBmMSpx,px,i_deg,D_Mpc):
def surf_den_flux(I_CO_Kkms,v_kms,D_Mpc):
	sd_Msunpc2=(5.0e2*cos_i*I_CO_Kkms*v_kms)*XH
	M_gas_Msun=(1.18e4*D_Mpc**2*S_CO)*XH
	M_gas=M_gas_Msun*Msun
#	print '%.2f' %I_CO,"[Jy km/s as-2]", '%.2e' %S_CO,"[Jy km/s]",'%.0f' %n_as,"[as2]",'%.0f' %n_bm,"[beam]",'%.2f' %sd_Msunpc2,"[Msun/pc2]",'%.2e' %M_gas_Msun,"[Msun]",type
	return sd_Msunpc2,M_gas

# --- reference -------------------------------	#
# Sakamoto et al. 1995, AJ, 110, 2075
# Sakamoto et al. 1999, ApJSS, 124, 403

exit

