#!/usr/bin/env python

# --- import constant ------------------------- #
import math
#import pyfits
# --- constant -------------------------------- #
c=3.0e10 # light speed
yr=365*86400.0
Myr=1.0e6*yr
pc=3.26*c*yr
myr=1.0e6*yr
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
#E_ion_ev=13.6  # [eV]
#E_bnd_ev=4.52  # [eV]
c_cms=2.99792458e10
HCN_1_0_lamda=c_cms/88.63e9
ff_cont_n2146_lamda=c_cms/88.644e9
ff_cont_n3628_lamda=c_cms/94.667e9
#  --- parameter -------------------------------        #
t_o_lifetime_yr=1.0e7


def sfr(sfr_begin, t_tot_lifetime_yr,type):
	iteration=t_tot_lifetime_yr/t_o_lifetime_yr
	tau=int(100/iteration)
	tot_enh=sfr_begin
	print tau
	for i in range(1,102,tau):
		enh=1.63-0.015*i
#		enh=3.9+0.04*i
#		enh=2.8-0.03*i
		tot_enh=tot_enh*enh
		print i,"%",enh,'%.1f' %tot_enh
	tot_sfr=sfr_begin*tot_enh


sfr(1,1.0e7,"test")
sfr(1,1.0e8,"test")


def func_01(a,b,t,type):
	for i in range(1,t):
		rho =b*math.exp(a*i)/(b-a+a*math.exp(b*i))
		print rho

# fucn_01(1,2,20,"test")


def func_02(a,t,type):
	
	for i in range(1,t):
		rho =a*(1-math.exp(i-1))
		print rho

#func_02(1.0,10.0,"test")




def tcons(SFR_3mm,SFR_FIR,M_SBR,dM,t_exp_myr,t_back_myr,type):
	eta=dM/SFR_3mm
	t_cons=M_SBR/(dM+SFR_3mm)
	t_cons_myr=t_cons/Myr
	tau=t_exp_myr/(t_exp_myr+t_cons_myr)
	print "---------",type,"----------------"
	print "dM/SFR_3mm =", '%.2f' %eta
	print "t_cons =", '%.2f' %t_cons_myr, "Myr"
	print "t_back =", '%.2f' %t_back_myr, "Myr"
	print "tau =", '%.2f' %tau
	return t_cons_myr

tcons_n2146_myr=tcons(15.7, 21.0, 2.5e9, 25.5, 15.0, 42.0, "n2146")
tcons_n3628_myr=tcons(2.1, 3.2, 2.0e8, 5.8, 4.55, 4.4, "n3628")
tcons_m82_myr=tcons(7.2, 10.5, 2.5e8, 33, 10.0, 280.0, "m82")
#print "---------------------------------"
#tau_n2146=tau(22.8, 21.0, 2.5e9, 25.5, 15e6, 42e6, "n2146")
#tau_n3628=tau(3.1, 3.2, 2.0e8, 5.8, 4.55e6, 4.4e6, "n3628")
#tau_m82=tau(10.5, 10.5, 2.5e8, 33, 10e6, 280e6, "m82")
print "---------------------------------"
print "after correction from t_back"
print "---------------------------------"

def tcons_back(SFR_3mm,SFR_FIR,M_SBR,dM,t_exp_myr,t_back_myr,type):
	eta=dM/SFR_3mm
	t_cons=(M_SBR-dM*t_back_myr*Myr)/SFR_3mm
	t_cons_myr=t_cons/Myr
	tau=t_exp_myr/(t_exp_myr+t_cons_myr)
	print "---------",type,"----------------"
	print "dM/SFR_3mm =", '%.2f' %eta
	print "t_cons =", '%.2f' %t_cons_myr, "Myr"
	print "t_back =", '%.2f' %t_back_myr, "Myr"
	print "tau =", '%.2f' %tau
	return t_cons_myr
	
print "---------------------------------"
tcons_back_n2146_myr=tcons_back(15.7, 21.0, 2.5e9, 25.5, 15.0, 42.0, "n2146")
tcons_back_n3628_myr=tcons_back(2.1, 3.2, 2.0e8, 5.8, 4.55, 4.4, "n3628")
print "---------------------------------"


def tau_err(SFR_3mm,e1,SFR_FIR,e2,M_SBR,e3,dM,e4,t_exp_myr,e5,t_back_myr,t_cons_myr,type):
	eta=dM/SFR_3mm
	dmsfr=dM+SFR_3mm
#	t_cons_myr=M_SBR/dmsfr/Myr
	tau=t_exp_myr/(t_exp_myr+t_cons_myr)
	p1=e1/SFR_3mm
	p2=e2/SFR_FIR
	p3=e3/M_SBR
	p4=e4/dM
	p5=e5/t_exp_myr
	ee1=math.sqrt(p1**2+p2**2)*eta
	ee2=math.sqrt(e1**2+e4**2)
	ee3=math.sqrt(p3**2+p1**2+p4**2)*t_cons_myr
	ee4=math.sqrt(p3**2+(ee3/t_cons_myr)**2)*tau
	eta1=eta-ee1
	eta2=eta+ee1
	dmsfr1=dmsfr-ee2
	dmsfr2=dmsfr+ee2
	tcon1_myr=t_cons_myr-ee3
	tcon2_myr=t_cons_myr+ee3
	tau1=tau-ee4
	tau2=tau+ee4
	print "---------",type,"----------------"
	print "dM/SFR_3mm =", '%.2f' %eta, "+/-", '%.2f' %ee1, "(", '%.2f' %eta1, "-", '%.2f' %eta2, ")"
	print "dM+SFR_3mm =", '%.2f' %dmsfr, "+/-", '%.2f' %ee2, "(", '%.2f' %dmsfr1, "-", '%.2f' %dmsfr2, ")"
	print "t_cons =", '%.2f' %t_cons_myr, "Myr", "+/-", '%.2f' %ee3, "(", '%.2f' %tcon1_myr, "-", '%.2f' %tcon2_myr, ")"
	print "t_back =", '%.2f' %t_back_myr, "Myr"
	print "tau =", '%.2f' %tau, "+/-", '%.2f' %ee4, "(", '%.2f' %tau1, "-", '%.2f' %tau2, ")"

tau_n2146=tau_err(15.7, 1.57, 21.0, 2.1, 2.5e9, 2.5e8, 25.5, 8.5, 15.0, 5.0, 37.7, tcons_back_n2146_myr, "n2146")
tau_n3628=tau_err(2.1, 0.21, 3.2, 0.32, 2.0e8, 2.0e7, 5.8, 1.4, 4.55, 0.65, 2.8, tcons_back_n3628_myr, "n3628")
tau_m82=tau_err(7.2, 0.72, 10.5, 1.05, 2.5e8, 2.5e7, 33, 3.3,  10.0, 1.0, 92.5, tcons_m82_myr, "m82")
print "---------------------------------"






exit
