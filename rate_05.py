#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
Lsun=3.98e33	# [erg/s]
pc=3.26*3.0e10*365*86400	# [cm]
k_B=1.38e-16
c=2.99e10	# [cm/s]
Jy=1.0e-23	# [ergs cm-2 s-1 Hz-1]
ev=1.6e-12	# [erg]
E_ion_ev=13.6	# [eV]
E_bnd_ev=4.52	# [eV]
E_bndion_ev=E_ion_ev+E_bnd_ev	# [ev]
E_bndion_erg=E_bndion_ev*ev	# [erg]
# --- parameter -------------------------------	#
L_IR_m82=10**10.77	# IRAS (Sanders 2003)
L_IR_n3628=10**10.25	# IRAS (Sanders 2003)
L_IR_n2146=10**11.07	# IRAS (Sanders 2003)
# F_IR_n3628=1.8e-14*(13.48*f12+5.16*f25+2.58*f60+f100)
d_m82_mpc=3.2	# IRAS (Sanders 2003) 
d_n3628_mpc=10.04	# IRAS (Sanders 2003) 
d_n2146_mpc=17.2	# IRAS (Sanders 2003) 
L_Ha_m82=7.0e40	# (Sander et al. 2003)
L_Ha_n3628=2.3e40	# (Sander et al. 2003)
L_Ha_n2146=15.0e40	# (Sander et al. 2003)
freq_n3628_88GHz=88.155	# Kotaro's data
#freq_n3628=freq_n3628_88GHz*1.0e9	# Kotaro's data
freq_n2146_88GHz=88.644	# Nakanishi's data
freq_m82_100GHz=100.884	# Kotaro's data
freq_m82_1GHz=1.0	# (Condon 1992)
freq_Ostar_GHz=5.0	# (Beiging 1989)
freq_m82=freq_m82_1GHz*1.0e9	# Kotaro's data
T_b=1.0e5	# electron temp in HII region (Condon 1992)
T_e=8.0e3	# (Condon 1992)
n_e=1000.0	# http://www.cv.nrao.edu/course/astr534/HIIRegions.html
S_TnonT_n3628_88GHz=0.037	# [Jy] @88 GHz ; from Kotaro's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc3628/rms.3628.conti'
S_TnonT_n2146_88GHz=0.064	# [Jy] @88 GHz ; from Nakanishi's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc2146/tvstat'
#S_TnonT_m82_100GHz_intef=0.43	# [Jy] @100GHz; (Matsushita 2005)
S_TnonT_m82_100GHz_intef=0.43	# [Jy] @100GHz; (Matsushita 2005)
S_TnonT_m82_100GHz_single=0.54	# [Jy] @100GHz; (Matsushita 2005)
S_T_m82_1GHz=0.7	# [Jy] @1GHz; (Condon 1992)
a_recom_coeff=3.1e-13	# @8000K (orange-cover book p.467)
n_H=n_e
alpha=0.8
N_uv_O7V=1.0e49	# [photon/s] ; (Maeder 1994) ; http://nedwww.ipac.caltech.edu/level5/March01/Maeder/Maeder5.html
#N_uv_m82_satoki=2.9e53
# O7V : T_e=38000[K], L=2.6e5[Lsun] ; orange-cover book, p.A-13
eta=0.44	# (Maeder 1994)
gamma=2.35	# (Condon 1992)
M_SN=6.7	# [M_sun] ; (Condon 1992)
M_O7Vstar=30.0	#
# --- production rate ---------------------------------	#
# (Condon 1992)
# kappa_pc1=3.3e-7*n_e**2*(T_e/1.0e4)**(-1.35)*freq_n3628_88GHz**(-2.1)
# B_freq=2*k_B*T_e*freq**2/c**2
# coeff_emission=B_freq*kappa_pc1

def lam2freq(lamb_cm):
	freq=c/lamb_cm
	return freq
def freq2lamb(freq_Hz):
	lamb=c/freq_Hz
	return lamb

# flux S/S_T=1+10*(freq_GHz)**(0.1-alpha)	# (Condon 1992)
def thrm2ttl(thrm,freq_GHz,type):
	ttl=thrm*(1.0+10*freq_GHz**(0.1-alpha))
	print type,'%.3f' %ttl, "[Jy/Hz]"
	return ttl
print "======================================================"
#print "M82 total Flux density @(1GHz, 3.2Mpc, Condon 1992) = ", S_TnonT_m82_100GHz, "[Jy/Hz]"
S_total_m82_8GHz_intef=thrm2ttl(S_T_m82_1GHz_intef,8.0,"M82 total Flux density @(100GHz, interferometer, 10Mpc) = ")

# flux S/S_T=1+10*(freq_GHz)**(0.1-alpha)	# (Condon 1992)
def ttl2thrm(ttl,freq_GHz,type):
	thrm=ttl/(1.0+10*freq_GHz**(0.1-alpha))
	print type,'%.3f' %thrm, "[Jy/Hz]"
	return thrm
print "======================================================"
print "M82 thermal Flux density @(1GHz, 3.2Mpc, Condon 1992) = ", S_T_m82_1GHz, "[Jy/Hz]"

S_T_m82_100GHz_intef=ttl2thrm(S_TnonT_m82_100GHz_intef,freq_m82_100GHz,"M82 thermal Flux density @(100GHz, interferometer, 10Mpc) = ")
S_T_m82_100GHz_single=ttl2thrm(S_TnonT_m82_100GHz_single,freq_m82_100GHz,"M82 thermal Flux density @(100GHz, single dish, 10Mpc) = ")
S_T_n3628_88GHz=ttl2thrm(S_TnonT_n3628_88GHz,freq_n3628_88GHz,"NGC 3628 thermal Flux density @(88GHz, 10Mpc) = ")
S_T_n2146_88GHz=ttl2thrm(S_TnonT_n2146_88GHz,freq_n2146_88GHz,"NGC 2146 thermal Flux density @(88GHz, 17.2Mpc) = ")

# S=S_T+S_nonT
# flux S_nonT/S_T=10*(freq_GHz)**(0.1-alpha)	# (Condon 1992)
def nonthrm2thrm(nonthrm,freq_GHz,type):
	thrm=nonthrm/(10*freq_GHz**(0.1-alpha))
	print type,'%.3f' %thrm, "[Jy/Hz]"
	return thrm

# luminosity [erg/s/Hz]
def Lun(d_mpc,S,type):
	Lun=4*math.pi*(d_mpc*1.0e6*pc)**2*(S*Jy)
	print type,'%.2e' %Lun,"[erg/s/Hz]"
	return Lun
print "======"
L_T_m82_1GHz=Lun(d_m82_mpc,S_T_m82_1GHz,"M82 L(thermal) @(1GHz, 3.2Mpc) = ")
L_T_m82_100GHz_intef=Lun(d_m82_mpc,S_T_m82_100GHz_intef,"M82 L(thermal) @(100GHz, interferometer, 3.2Mpc) = ")
L_T_m82_100GHz_single=Lun(d_m82_mpc,S_T_m82_100GHz_single,"M82 L(thermal) @(100GHzsingle dish, 3.2Mpc) = ")
L_T_n3628_88GHz=Lun(d_n3628_mpc,S_T_n3628_88GHz,"NGC 3628 L(thermal) @(88GHz, 10Mpc) = ")
L_T_n2146_88GHz=Lun(d_n2146_mpc,S_T_n2146_88GHz,"NGC 2146 L(thermal) @(88GHz, 17Mpc) = ")
L_TnonT_n3628_88GHz=Lun(d_n3628_mpc,S_TnonT_n3628_88GHz,"NGC 3628 L(thrm+non) @(88GHz, 10Mpc) = ")
L_TnonT_n2146_88GHz=Lun(d_n2146_mpc,S_TnonT_n2146_88GHz,"NGC 2146 L(thrm+non) @(88GHz, 17Mpc) = ")
L_nonT_n3628_88GHz=L_TnonT_n3628_88GHz-L_T_n3628_88GHz
L_nonT_n2146_88GHz=L_TnonT_n2146_88GHz-L_T_n2146_88GHz
print "NGC 3628 L(nonthrm) @(88GHz, 10Mpc) = ",L_nonT_n3628_88GHz, "[erg/s/Hz]"
print "NGC 2146 L(nonthrm) @(88GHz, 17Mpc) = ",L_nonT_n2146_88GHz, "[erg/s/Hz]"
#print "------"

# production rate [s-1]	# (Condon 1992)
def N_uv(freq_GHz,L_thrm,type):
	N_uv=6.3e52*(T_e/1.0e4)**(-0.45)*(freq_GHz)**(0.1)*(L_thrm/1.0e27)
	L_uv=N_uv*E_bndion_erg
	n_O7Vstar=N_uv/N_uv_O7V
	n_Ostar=n_O7Vstar/eta
#	mass=n_O7Vstar*M_O7Vstar
	mass=n_Ostar*M_O7Vstar
	print "---",type,"---"
	print "production rate = ", '%.2e' %N_uv, "[photon/s]"
	print "# of O7V-type stars = ", '%.2e' %n_O7Vstar
	print "# of O-type stars = ", '%.2e' %n_Ostar
	print "corresponding total luminosity = ", '%.2e' %L_uv, "[erg/s]"
	print "corresponding total mass = ", '%.2e' %mass
	return N_uv
print "-----------------------------------------------"
print " N_uv=6.3e52*(T_e/1.0e4)**(-0.45)*freq**(0.1)*(L_thrm/1.0e27) (Condon 1992) "
print "-----------------------------------------------"
print "O7V-type star production rate = ", N_uv_O7V, "[photon/s]"
print "# of O-type star in our Galaxy ~ 6500 (Roberts 1957, PASP)"
#print "------"
N_uv_m82_condon=N_uv(freq_m82_1GHz,L_T_m82_1GHz,"M82 (condon 1992)")
#N_uv_m82_satoki_pr=2.9e53
#print "M82 production rate (A,B,C,D,E,F,G) @100GHz (Matsushita et al. 2005) = ",N_uv_m82_satoki_pr ,"[photon/s]"
N_uv_m82_satoki_intef=N_uv(freq_m82_100GHz,L_T_m82_100GHz_intef,"M82 interferometer (satoki 2005)")
N_uv_m82_satoki_single=N_uv(freq_m82_100GHz,L_T_m82_100GHz_single,"M82 single dish (satoki 2005)")
N_uv_n2146=N_uv(freq_n2146_88GHz,L_T_n2146_88GHz,"NGC 2146")
N_uv_n3628=N_uv(freq_n3628_88GHz,L_T_n3628_88GHz,"NGC 3625")


# --- SF rate -----------------------------------------	#
def SFR_Ha(L_Ha,type):
	sfr=1.0e-41*L_Ha	# (Thronson 1991)
	print type, '%.2f' %sfr, "[M_sun/yr]"
	return sfr
print "-----------------------------------------------"
print " SFR_Ha=1.0e-41*L_Ha (Thronson 1991) "
print "-----------------------------------------------"
SFR_Ha_m82=SFR_Ha(L_Ha_m82, "M82 SFR (Ha) (data) = ")
SFR_Ha_n3628=SFR_Ha(L_Ha_n3628, "NGC 3628 SFR (Ha) (data) = ")
SFR_Ha_n2146=SFR_Ha(L_Ha_n2146, "NGC 2146 SFR (Ha) (data) = ")

def SFR_IR(L_IR,type):
	sfr=4.5e-44*L_IR*Lsun	# (Kennicutt 1998)
	print type,'%.2f' %sfr, "[M_sun/yr]"
	return sfr
print "-----------------------------------------------"
print " SFR_IR=4.5e-44*L_IR (Kennicut 1998) "
print "-----------------------------------------------"
SFR_IR_m82=SFR_IR(L_IR_m82,"M82 SFR (IR) (data)")
SFR_IR_n3628=SFR_IR(L_IR_n3628,"NGC 3628 SFR (IR) (data)")
SFR_IR_n2146=SFR_IR(L_IR_n2146,"NGC 2146 SFR (IR) (data)")

def SFR_radio_pr(N_uv,type):
	sfr=1.08e-53*N_uv	# (Kennicutt 1998) # (http://0rz.tw/DzdAK ; Johnson 2004)
	print type,'%.2f' %sfr, "[M_sun/yr] <==="
	return sfr
print "-----------------------------------------------"
print " SFR_radio=1.08e-53*N_uv (Kennicut 1998) "
print "-----------------------------------------------"
SFR_radio_m82_condon=SFR_radio_pr(N_uv_m82_condon,"M82 SFR (radio) (O, Condon 1992 data) = ")	
#SFR_radio_m82_pr_satoki_pr=SFR_radio_pr(N_uv_m82_satoki_pr,"M82 SFR (radio) (O, Matsushita 2005 data, from production rate) = ")	
SFR_radio_m82_pr_satoki_intef=SFR_radio_pr(N_uv_m82_satoki_intef,"M82 SFR (radio interferometer) (O, Matsushita 2005 data) = ")	
SFR_radio_m82_pr_satoki_single=SFR_radio_pr(N_uv_m82_satoki_single,"M82 SFR (radio single dish) (O, Matsushita 2005 data) = ")	
SFR_radio_n3628_pr=SFR_radio_pr(N_uv_n3628,"NGC 3628 SFR (radio) (O, our data) = ")	
SFR_radio_n2146_pr=SFR_radio_pr(N_uv_n2146,"NGC 2146 SFR (radio) (O, our data) = ")	
# L_nonT/1.0e7=5.3e21*freq_GHz**(-alpha)*(SFR_5Msun) (Condon 1992)
# L_T/1.0e7=5.5e20*freq_GHz**(-0.1)*(SFR_5Msun)	(Condon 1992)
def SFR_radio_5Msun(L_T,freq_GHz,type):
	sfr5=L_T*1.0e-7*freq_GHz**0.1/5.5e20
	print type, '%.2f' %sfr5, "[M_sun/yr]"
	return sfr5
print "-----------------------------------------------"
print " SFR_radio (>5Msun)=L_T*1.0e-7*freq_GHz^0.1/5.5e20 (Condon 1992) "
print "-----------------------------------------------"
SFR_radio_m82_5M_satoki_intef=SFR_radio_5Msun(L_T_m82_100GHz_intef,freq_m82_100GHz,"M82 SFR (radio interferometer) (>5Msun OB, theory) = ")
SFR_radio_m82_5M_satoki_single=SFR_radio_5Msun(L_T_m82_100GHz_single,freq_m82_100GHz,"M82 SFR (radio interferometer) (>5Msun OB, theory) = ")
SFR_radio_n3628_5M=SFR_radio_5Msun(L_T_n3628_88GHz,freq_n3628_88GHz,"NGC 3628 SFR (radio) (>5Msun OB, theory) = ")
SFR_radio_n2146_5M=SFR_radio_5Msun(L_T_n2146_88GHz,freq_n2146_88GHz,"NGC 2146 SFR (radio) (>5Msun OB, theory) = ")

# --- SN rate -----------------------------------------	#
# r_SN=2.3e-12*L_FIR
# r_SN: SN rate [yr^-1]
# L_FIR: IRAS FIR luminosity [L_sun]
def r_SN_IR(L_IR,type):
	r_SN=2.3e-12*L_IR	# (van Buren & Greenhouse 1994)
	print type,'%.3f' %r_SN,"[SN/yr]"
	return r_SN
print "-----------------------------------------------"
print " r_SN_IR=2.3e-12*L_IR (van Buren & Greenhouse 1994) "
print "-----------------------------------------------"
r_SN_IR_m82=r_SN_IR(L_IR_m82,"M82 SN rate (IR) (data) =")
r_SN_IR_n3628=r_SN_IR(L_IR_n3628,"NGC 3628 SN rate (IR) (data) =")
r_SN_IR_n2146=r_SN_IR(L_IR_n2146,"NGC 2146 SN rate (IR) (data) =")
#r_SN_IR_n3628=2.3e-12*L_IR_n3628	# (van Buren & Greenhouse 1994)
# r_SN=integral(M^(-gamma))dM # (Condon 1992)
r_SN_radio_1=(M_SN)**(-gamma+1)

def r_SN_radio(SFR_radio, type):
	r_SN=0.041*SFR_radio	# M>5Msun (Condon 1992)
	print type,'%.2f' %r_SN,"[SN/yr]"
print "-----------------------------------------------"
print " r_SN_radio=0.041*SFR_radio (M>5Msun) (Condon 1992) "
print "-----------------------------------------------"
r_SN_radio_m82_condon=r_SN_radio(SFR_radio_m82_condon,"M82 SN rate (radio) (Condon 1992 data) =")
#r_SN_radio_m82_pr_satoki_pr=r_SN_radio(SFR_radio_m82_pr_satoki_pr,"M82 SN rate (radio) (Matsusthia 2005 data, form production rate) =")
r_SN_radio_m82_pr_satoki_intef=r_SN_radio(SFR_radio_m82_pr_satoki_intef,"M82 SN rate (radio) interferometer (Matsusthia 2005 data) =")
r_SN_radio_m82_pr_satoki_single=r_SN_radio(SFR_radio_m82_pr_satoki_single,"M82 SN rate (radio) single dish (Matsusthia 2005 data) =")
r_SN_radio_n3628_pr=r_SN_radio(SFR_radio_n3628_pr,"NGC 3628 SN rate (radio) (our data) =")
r_SN_radio_n3628_5M=r_SN_radio(SFR_radio_n3628_5M,"NGC 3628 SN rate (radio) (>5Msun OB, theory) =")
r_SN_radio_n2146_pr=r_SN_radio(SFR_radio_n2146_pr,"NGC 2146 SN rate (radio) (our data) =")
r_SN_radio_n2146_5M=r_SN_radio(SFR_radio_n2146_5M,"NGC 2146 SN rate (radio) (>5Msun OB, theory) =")

print "NGC 3628 SN rate (radio) (6.7Msun OB, theory) =", r_SN_radio_1, "[SN/yr]"

# -----------------------------------------------------	#
# Bieging et al. 1989, ApJ, 340, 518B
# Condon 1992, ARAA, 30, 575
# Kennicutt 1998, ARAA, 36, 189a
# Johnson 2004, NewAstronomyReview, 48, 1337
# Maeder 1994, ARAA, 32, 227
# Matsushita et al. 2005, ApJ, 618, 712
# Roberts 1957, PASP, 69, 59R
# Sanders et al. 2003, ApJ, 126, 1607
# Strickland et al. 2004, ApJ, 606, 829 
# Thronson et al. 1991, MNRAS, 252,543
# van Buren & Greenhouse 1994, ApJ, 431, 640

exit
