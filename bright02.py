#!/usr/bin/env python

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
rad2as=180.0/math.pi*3600
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
def S2Tl(S_Jy_bm,lamb,bm1_as,bm2_as):
	bm=bm1_as*bm2_as*(1.0/3600*math.pi/180)**2/(4*math.log(2))/math.pi
	I=S_Jy_bm*bm
#	freq=freq_GHz*1.0e9
#	lamb=c/freq
	T=lamb**2*I/(2*k_B)
	print '%.2e' %T,"[K]"
	return T
t=S2Tl(1.0e-3,0.1,1,1)

def S2Tf(S_Jy_bm,freq_GHz,bm1_as,bm2_as):
	bm=bm1_as*bm2_as*(1.0/3600*math.pi/180)**2/(4*math.log(2))*math.pi
	I=S_Jy_bm*bm
	freq=freq_GHz*1.0e9
	lamb=c/freq
	T=lamb**2*I/(2*k_B)
	print '%.2e' %T,"[K]"
	return T
t=S2Tf(1.0e-3,115,1,1)

def T_NMA(S_mJy,lamb_mm,bm_maj_as,bm_min_as,type):
	T=13.6*lamb_mm**2/(bm_maj_as*bm_min_as)*S_mJy
	print '%.2f' %T,"[mK] | ", type
	return T
t=T_NMA(1,1,1,1,"test")
t=T_NMA(4.93,1,2.9,2.4,"n3628,chan")
t=T_NMA(4.93,1,2.9,2.4,"n3628,chan")
t=T_NMA(1.0,1.0,1.0,1.0,"example from NMA page")

def T_NMA2(S_Jy,lamb,bm_as2):
	T=13.6*(lamb*10)**2/bm_as2*(S_Jy*1000)/1000
	print '%.2e' %T,"[K]"
	return T
t=T_NMA2(0.001,0.1,1)

def mass(S_Jy,lamb,bm1_as,bm2_as,D_Mpc,v_kms):
	bm=bm1_as*bm2_as
	T=13.6*(lamb*10)**2/bm*(S_Jy*1000)/1000
	colden=T*1.4e20*v_kms
	surfden=colden*m_p
	surfden_Msunpc2=surfden/Msun_pc2
	D=D_Mpc*1.0e6*pc
	A_cm2=bm*(D/rad2as)**2
	A_pc2=A_cm2/pc**2
	m=surfden*A_cm2/Msun
	print '%.2e' %surfden,"", '%.2e' %m,"mass"
	return surfden
mass(0.1,0.3,3.3,2.8,17.2,50)

def mass(S_Jy_kms,lamb_cm,bm_as,D_Mpc):
	T=13.6*(lamb_cm*10)**2/bm_as*(S_Jy_kms*1000)/1000
	colden=T*1.4e20
	surfden=colden*m_p
	surfden_Msunpc2=surfden/Msun_pc2
	D=D_Mpc*1.0e6*pc
	A_cm2=bm_as*(D/rad2as)**2
	A_pc2=A_cm2/pc**2
	m=surfden*A_cm2/Msun
	print '%.2e' %surfden,"", '%.2e' %m,"mass"
	return surfden
mass(1.8e3,0.26,1000,17.2)

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

