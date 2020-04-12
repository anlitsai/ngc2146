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



#print "---------------------------------"
def err(ea,eb):
	err=math.sqrt(ea**2+eb**2)
#	print ea, eb, err
	return err

#print "---------------------------------"
def errp(a,ea, b,eb):
	pa=ea/a
	pb=eb/b
	errp=math.sqrt(pa**2+pb**2)
#	print pa, pb, errp
	return errp

#print "---------------------------------"

print "---------------------------------"
def dd(a, ea, b, eb, type):
	ab=a/b
	e_ab=ab*errp(a,ea, b,eb)
	print '%.2f' %ab, "+/-", '%.2f' %e_ab, type
	return ab, e_ab
print "---------------------------------"
t_myr_n3628_of=dd(410.0*pc, 40.0*pc, 90.0e5*myr, 9.0e5*myr, "[Myr] | N3628 OF t_exp = R/v_exp")
dm_n2146_of=dd(3.4e8, 3.4e7, 15.0e6, 5.0e6, "[Msyn/yr] | N2146 OF dM = M/t_exp")
dm_n3628_of=dd(2.8e7, 2.8e6, t_myr_n3628_of[0]*1.0e6, t_myr_n3628_of[1]*1.0e6, "[Msyn/yr] | N2638 OF dM = M/t_exp")
dm_m82_of=dd(3.3e8, 3.3e7, 10.0e6, 1.0e6, "[Msyn/yr] | M82 OF dM = M/t_exp")
t_n3628_sb2=dd(700.0*pc, 300.0*pc, 35.0e5, 10.0e5, "[sec] | N2638 SB2 t_exp= R/v")
t_myr_n3628_sb2=t_n3628_sb2[0]/myr
t_err_myr_n3628_sb2=t_n3628_sb2[1]/myr
print "t_exp =", '%.2e' %(t_myr_n3628_sb2), "+/-", '%.2e' %(t_err_myr_n3628_sb2), "[Myr]"
print "t_min =", '%.2e' %(t_myr_n3628_sb2-t_err_myr_n3628_sb2), ", t_max=", '%.2e' %(t_myr_n3628_sb2+t_err_myr_n3628_sb2), "[Myr]"
print "---------------------------------"
print "--- t_back, t_cons, t_cons' -----------------"
t_back_t_cons=dd(37.5,7.5,65.0,15.0,"| NGC 2146 | t_back/t_cons")
t_cons1_t_cons=dd(98.5,22.5,65.0,15.0,"| NGC 2146 | t_cons'/t_cons")
t_back_t_cons=dd(2.8,0.3, 24.0,4.0,"| NGC 3628 | t_back/t_cons")
t_cons1_t_cons=dd(87.5,8.5,24.0,4.0,"| NGC 3628 | t_cons'/t_cons")
t_back_t_cons=dd(92.5,1.5,6.0,1.0,"| M82 | t_back/t_cons")
print "---------------------------------"
def mm(a, ea, b, eb, type):
	ab=a*b
	e_ab=ab*errp(a,ea, b,eb)
	print '%.2e' %ab, "+/-", '%.2e' %e_ab, type
	return ab, e_ab
print "---------------------------------"
v2_n2146_sb=mm(50.0e5, 10.0e5, 50.0e5, 10.0e5, "[cm2/s2] | N2146 SB = v^2")
#E2_n2146_sb=mm(v2_n2146_sb[0], v2_n2146_sb[1], 2.6e8*Msun, 0*Msun, "[erg] | N2146 SB, 2E = mv^2")
E_n2146_sb=mm(v2_n2146_sb[0], v2_n2146_sb[1], 2.6e8*Msun/2, 2.6e7*Msun/2, "[erg] | N2146 SB, E = 1/2mv^2")
#E_n2146_sb=0.5*E2_n2146_sb[0]
print "1/2mv^2 = ", '%.2e' %E_n2146_sb[0], " +/-", '%.2e' %E_n2146_sb[1], "[erg]"
print "E_min = ", '%.2e' %(E_n2146_sb[0]-E_n2146_sb[1]), ", E_max =", '%.2e' %(E_n2146_sb[0]+E_n2146_sb[1]), "[erg]"
print "---------------------------------"




def tcons(SFR_3mm,e_sfr, M_SBR,e_msbr,dM,e_dm,type):
	dmsfr=dM+SFR_3mm
	e_dmsfr=err(e_dm,e_sfr)
	t_cons=M_SBR/dmsfr
	e_tcons=t_cons*(errp(M_SBR,e_msbr, dmsfr,e_dmsfr))
	t_cons_myr=t_cons/1.0e6
	e_tcons_myr=e_tcons/1.0e6
#	ratio_tcons_tback=t_cons_myr/t_back_myr
#	e_r_tcons_tback=ratio_tcons_tback*errp(t_cons_myr, e_tcons, t_back_myr, e_tback)
	print "---------",type,"----------------"
#	print "dM =", '%.2f' %dM, "+/-", '%.2f' %e_dm,"Msun/yr"
#	print "SFR =", '%.2f' %SFR_3mm, "+/-", '%.2f' %e_sfr,"Msun/yr"
#	print "dmsfr =", '%.2f' %dmsfr, "+/-", '%.2f' %e_dmsfr,"Msun/yr"
#	print "M_SBR =", '%.2e' %M_SBR, "+/-", '%.2e' %e_msbr,"Msun"
	print "t_cons =", '%.2f' %t_cons_myr, "+/-", '%.2f' %e_tcons_myr,"Myr"
	print '%.2f' %(t_cons_myr-e_tcons_myr), "--", '%.2f' %(t_cons_myr+e_tcons_myr),"Myr"
	return t_cons_myr, e_tcons_myr

tcons_n2146_myr=tcons(15.7, 1.57, 2.5e9, 2.5e8, dm_n2146_of[0], dm_n2146_of[1], "n2146")
tcons_n3628_myr=tcons(2.1, 0.21, 2.0e8, 2.0e7, dm_n3628_of[0],dm_n3628_of[1], "n3628")
tcons_m82_myr=tcons(7.2, 0.72, 2.5e8, 2.5e7, dm_m82_of[0],dm_m82_of[1],  "m82")
#print "---------------------------------"
#tau_n2146=tau(22.8, 21.0, 2.5e9, 25.5, 15e6, 42e6, "n2146")
#tau_n3628=tau(3.1, 3.2, 2.0e8, 5.8, 4.55e6, 4.4e6, "n3628")
#tau_m82=tau(10.5, 10.5, 2.5e8, 33, 10e6, 280e6, "m82")
print "---------------------------------"
print "after correction from t_back"

def tcons_back(SFR_3mm, e_sfr, M_SBR, e_msbr, dM, e_dm, t_back_myr, e_tback, type):
	t_back=t_back_myr*1.0e6
	dmtback=dM*t_back
	e_dmtback=dmtback*errp(dM, e_dm, t_back, e_tback)
	mdmt=M_SBR-dmtback
	e_mdmt=err(e_dm,e_dmtback)
	t_cons=mdmt/SFR_3mm
	e_tcons=t_cons*errp(mdmt, e_mdmt, SFR_3mm, e_sfr)
	t_cons_myr=t_cons/1.0e6
	e_tcons_myr=e_tcons/1.0e6
#	ratio_tcons_tback=t_cons_myr/t_back_myr
#	e_r_tcons_tback=ratio_tcons_tback*errp(t_cons_myr, e_tcons, t_back_myr, e_tback)
	print "---------",type,"----------------"
	print "t_cons =", '%.2f' %t_cons_myr, "+/-", '%.2f' %e_tcons_myr,"Myr"
	print '%.2f' %(t_cons_myr-e_tcons_myr), "--", '%.2f' %(t_cons_myr+e_tcons_myr),"Myr"
	return t_cons_myr,e_tcons_myr
	
tcons_back_n2146_myr=tcons_back(15.7, 1.57, 2.5e9, 2.5e8, 25.5, 8.5, 37.5, 7.5,"n2146")
tcons_back_n3628_myr=tcons_back(2.1, 0.21, 2.0e8, 2.0e7, 5.8, 1.4, 2.8, 0.3, "n3628")
#print "----- test array ----------------------------"
#print tcons_back_n2146_myr[0]
#print tcons_back_n2146_myr[1]
print "---------------------------------"
print "---------------------------------"



def tau_err(SFR_3mm,e_sfr,M_SBR,e_msbr,dM,e_dm,t_exp_myr,e_texp_myr,t_back_myr,e_tback, t_cons_myr,e_tcons_myr,type):
#	eta=dM/SFR_3mm
#	e_eta=eta*errp(dM, e_dm, SFR_3mm,e_sfr)*eta
#	dmsfr=dM+SFR_3mm
#	e_dmsfr=err(dM,SFR_3mm)
	t_tot_myr=t_exp_myr+t_cons_myr
	e_ttot_myr=err(e_texp_myr,e_tcons_myr)
	tau=t_exp_myr/t_tot_myr
	e_tau=tau*errp(t_exp_myr,e_texp_myr, t_tot_myr, e_ttot_myr)
	print "---------",type,"----------------"
#	print "dM/SFR_3mm =", '%.2f' %eta, "+/-", '%.2f' %e_eta
#	print "dM+SFR_3mm =", '%.2f' %dmsfr, "+/-", '%.2f' %e_dmsfr
	print "tau =", '%.2f' %tau, "+/-", '%.2f' %e_tau

tau_n2146=tau_err(15.7, 1.57, 21.0, 2.1, 2.5e9, 2.5e8, 25.5, 8.5, 15.0, 5.0,tcons_back_n2146_myr[0], tcons_back_n2146_myr[1], "n2146")
tau_n3628=tau_err(2.1, 0.21, 3.2, 0.32, 2.0e8, 2.0e7, 5.8, 1.4, 4.55, 0.65, tcons_back_n3628_myr[0], tcons_back_n3628_myr[1], "n3628")
tau_m82=tau_err(7.2, 0.72, 10.5, 1.05, 2.5e8, 2.5e7, 33, 3.3,  10.0, 1.0, tcons_m82_myr[0], tcons_m82_myr[1], "m82")
print "---------------------------------"






exit
