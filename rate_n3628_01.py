#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
Lsun=3.98e33	# [erg/s]
pc=3.26*3.0e10*365*86400	# [cm]
k_B=1.38e-16
c=2.99e10	# [cm/s]
Jy=1.0e-23	# [ergs cm-2 s-1 Hz-1]
# --- parameter -------------------------------	#
L_IR=10**10.25	# IRAS (Sanders 2003)
# F_IR_n3628=1.8e-14*(13.48*f12+5.16*f25+2.58*f60+f100)
d_m82_mpc=3.2	# IRAS (Sanders 2003) 
d_n3628_mpc=10.04	# IRAS (Sanders 2003) 
L_Ha=2.3e40	# (Strickland 2004)
freq_n3628_GHz=88.0	# Kotaro's data
#freq_n3628=freq_n3628_GHz*1.0e9	# Kotaro's data
freq_m82_GHz=1.0	# (Condon 1992)
freq_Ostar_GHz=5.0	# (Beiging 1989)
freq_WRstar_GHz=5.0	# (Chapman 1999)
freq_m82=freq_m82_GHz*1.0e9	# Kotaro's data
T_b=1.0e5	# electron temp in HII region (Condon 1992)
T_e=8.0e3	# (Condon 1992)
n_e=1000.0	# http://www.cv.nrao.edu/course/astr534/HIIRegions.html
S_TnonT_n3628_88GHz=2.5e-2	# [Jy] @88 GHz ; from Kotaro's data 88 GHz ; see file 'rms.3628.conti'
S_T_m82_1GHz=0.7	# [Jy] @1GHz; (Condon 1992)
L_TnonT_Ostar_5GHz=1.0e19	# [erg/s] (Chapman 1999 ; Chapman 1999)
L_nonT_WRstar_5GHz=1.0e19	# [erg/s] (Chapman 1999)
a_recom_coeff=3.1e-13	# @8000K (orange-cover book p.467)
n_H=n_e
alpha=0.8
N_uv_O7V=1.0e49	# [photon/s] ; (Maeder 1994) ; http://nedwww.ipac.caltech.edu/level5/March01/Maeder/Maeder5.html
# O7V : T_e=38000[K], L=2.6e5[Lsun] ; orange-cover book, p.A-13
eta=0.44	# (Maeder 1994)
# --- production rate ---------------------------------	#
# (Condon 1992)
# kappa_pc1=3.3e-7*n_e**2*(T_e/1.0e4)**(-1.35)*freq_n3628_GHz**(-2.1)
# B_freq=2*k_B*T_e*freq**2/c**2
# coeff_emission=B_freq*kappa_pc1

def lam2freq(lamb_cm):
	freq=c/lamb_cm
	return freq
def freq2lamb(freq_Hz):
	lamb=c/freq_Hz
	return lamb

# flux S/S_T=1+10*(freq_GHz)**(0.1-alpha)	# (Condon 1992)
def ttl2thrm(ttl,freq_GHz):
	thrm=ttl/(1.0+10*freq_GHz**(0.1-alpha))
	return thrm
L_T_Ostar_5GHz=ttl2thrm(L_TnonT_Ostar_5GHz,freq_Ostar_GHz)
S_T_n3628_88GHz=ttl2thrm(S_TnonT_n3628_88GHz,freq_n3628_GHz)

# S=S_T+S_nonT
# flux S_nonT/S_T=10*(freq_GHz)**(0.1-alpha)	# (Condon 1992)
def nonthrm2thrm(nonthrm,freq_GHz):
	thrm=nonthrm/(10*freq_GHz**(0.1-alpha))
	return thrm
L_T_WRstar_5GHz=nonthrm2thrm(L_nonT_WRstar_5GHz,freq_WRstar_GHz)

# luminosity [erg/s/Hz]
def Lun(d_mpc,S):
	Lun=4*math.pi*(d_mpc*1.0e6*pc)**2*(S*Jy)
	return Lun
L_T_m82_1GHz=Lun(d_m82_mpc,S_T_m82_1GHz)
L_T_n3628_88GHz=Lun(d_n3628_mpc,S_T_n3628_88GHz)
L_TnonT_n3628_88GHz=Lun(d_n3628_mpc,S_TnonT_n3628_88GHz)

# S=S_T+S_nonT
# S_nonT/S_T=10*(freq_GHz)**(0.1-alpha)	# (Condon 1992)
# S_nonT=S*(1.0+0.1*(freq_GHz)**(alpha-0.1))**(-1)	# (Condon 1992)
def ttl2nonthrm(ttl,freq_GHz):
	nonthrm=ttl*(1.0+0.1*(freq_GHz)**(alpha-0.1))**(-1)
	return nonthrm
L_nonT_n3628_88GHz=ttl2nonthrm(L_TnonT_n3628_88GHz,freq_n3628_GHz)
print "L_nonT_n3628_88GHz = ",L_nonT_n3628_88GHz, "[erg]"
# production rate [s-1]	# (Condon 1992)
def N_uv(freq_GHz,L_thrm):
	N_uv=6.3e52*(T_e/1.0e4)**(-0.45)*(freq_GHz)**(0.1)*(L_thrm/1.0e27)
	return N_uv
N_uv_m82=N_uv(freq_m82_GHz,L_T_m82_1GHz)
N_uv_n3628=N_uv(freq_n3628_GHz,L_T_n3628_88GHz)
N_uv_Ostar=N_uv(freq_Ostar_GHz,L_T_Ostar_5GHz)
N_uv_WRstar=N_uv(freq_WRstar_GHz,L_T_WRstar_5GHz)
n_O7Vstar_m82=N_uv_m82/N_uv_O7V	
n_O7Vstar_n3628=N_uv_n3628/N_uv_O7V	
n_Ostar_m82=n_O7Vstar_m82/eta	
n_Ostar_n3628=n_O7Vstar_n3628/eta	

print "M82 thermal Flux density @ 1 GHz = ", S_T_m82_1GHz, "[Jy]"
print "M82 thermal Luminosity @ 3.2 Mpc = ", L_T_m82_1GHz, "[erg/s]"
print "M82 production rate = ", N_uv_m82, "[photon/s]"
print "# of O7V-type stars in M82 = ", '%e' %(n_O7Vstar_m82)
print "# of O-type stars in M82 = ", '%e' %(n_Ostar_m82)
print "------"
print "NGC 3628 thermal Flux density @ 88 GHz = ", S_T_n3628_88GHz, "[Jy]"
print "NGC 3628 thermal Luminosity @ 10 Mpc = ", L_T_n3628_88GHz, "[erg/s]"
print "NGC 3628 production rate = ", N_uv_n3628, "[photon/s]"
print "# of O7V-type stars in NGC 3628 = ", '%e' %(n_O7Vstar_n3628)
print "# of O-type stars in NGC 3628 = ", '%e' %(n_Ostar_n3628)

# --- SN rate -----------------------------------------	#
# r_SN=2.3e-12*L_FIR
# r_SN: SN rate [yr^-1]
# L_FIR: IRAS FIR luminosity [L_sun]
r_SN_IR=2.3e-12*L_IR	# (van Buren & Greenhouse 1994)
# L_nonT/1.0e27=13*(freq_GHz)**(-alpha)*r_SN	# (Condon 1992)
def SNrate_radio(L_nonT,freq_GHz):
	SNrate=L_nonT*1.0e-27*freq_GHz**(alpha)/13.0
	return SNrate
r_SN_radio=SNrate_radio(L_nonT_n3628_88GHz,freq_n3628_GHz)
print "NGC 3628 SN rate (IR) = ", r_SN_IR, "[SN/yr]"
print "NGC 3628 SN rate (radio) = ", r_SN_radio, "[SN/yr]"
# unit checked

# --- SF rate -----------------------------------------	#
SFR_Ha=1.0e-41*L_Ha	# (Thronson 1991)
SFR_IR=4.5e-44*L_IR*Lsun	# (Kennicutt 1998)
SFR_radio=1.08e-53*N_uv_n3628	# (Kennicutt 1998) # (http://0rz.tw/DzdAK ; Johnson 2004)
print "NGC 3628 SFR (Ha) = ",SFR_Ha, "[M_sun/yr]"
print "NGC 3628 SFR (IR) = ",SFR_IR, "[M_sun/yr]"
print "NGC 3628 SFR (radio) = ",SFR_radio, "[M_sun/yr]"

# -----------------------------------------------------	#
# Bieging et al. 1989, ApJ, 340, 518B
# Chapman et al. 1999, ApJ, 518, 890
# Condon 1992, ARAA, 30, 575
# Kennicutt 1998, ARAA, 36, 189a
# Johnson 2004, NewAstronomyReview, 48, 1337
# Maeder 1994, ARAA, 32, 227
# Sanders et al. 2003, ApJ, 126, 1607
# Strickland et al. 2004, ApJ, 606, 829 
# Thronson et al. 1991, MNRAS, 252,543
# van Buren & Greenhouse 1994, ApJ, 431, 640

exit
