#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
Lsun=3.98e33	# [erg/s]
Msun=1.99e33	# solar mass
k_B=1.38e-16
N_A=6.02e23	# Avogadro constant
c=2.99e10	# [cm/s]
yr=365*86400	# [sec]
lyr=c*yr	# [cm]
pc=3.26*lyr	# [cm]
kpc=1000*pc	# [cm]
mpc=1.0e6*pc	# [cm]
Jy=1.0e-23	# [ergs cm-2 s-1 Hz-1]
ev=1.6e-12	# [erg]
m_p=1.67e-24	# [g]
m_e=9.11e-28	# [g]
E_ion_ev=13.6	# [eV]
E_bnd_ev=4.52	# [eV]
E_bndion_ev=0.5*E_bnd_ev+E_ion_ev	# [ev]
E_bndion_erg=E_bndion_ev*ev	# [erg]
# --- parameter -------------------------------	#
L_IR_m82=10**10.77	# IRAS (Sanders 2003)
L_IR_n253=10**10.44	# IRAS (Sanders 2003)
L_IR_n3628=10**10.25	# IRAS (Sanders 2003)
L_IR_n2146=10**11.07	# IRAS (Sanders 2003)
L_IR_n4631=10**10.20	# IRAS (Sanders 2003)
# F_IR_n3628=1.8e-14*(13.48*f12+5.16*f25+2.58*f60+f100)
d_m82_mpc=3.9	# () 
#d_n3628_mpc=10.04	# IRAS (Sanders 2003) 
d_n3628_mpc=7.7		# (Tully 1988) 
d_n2146_mpc=17.2	# (Tully 1988)
#d_n2146_mpc=16.47	# IRAS (Sanders 2003) 
L_Ha_m82=7.0e40		# (Strickland et al. 2004)
L_Ha_n253=3.6e40	# (Strickland et al. 2004)
L_Ha_n3628=2.3e40	# (Strickland et al. 2004)
L_Ha_n2146=15.0e40	# (Delle Ceca et al. 1999)
freq_n3628_88GHz=94.667	# Kotaro's data
#freq_n3628=freq_n3628_88GHz*1.0e9	# Kotaro's data
freq_n2146_88GHz=88.644	# Nakanishi's data
freq_m82_100GHz=100.884	# Kotaro's data
freq_m82_87GHz=87.2	# Jura et al. 1978
freq_m82_92GHz=92	# Carlstrom et al. 1991
freq_m82_1GHz=1.0	# (Condon 1992)
freq_n4631_1_5GHz=1.49	# (Hummel 1990)
freq_n4631_327MHz=0.327	# (Hummel 1990)
freq_Ostar_GHz=5.0	# (Beiging 1989)
#freq_m82=freq_m82_1GHz*1.0e9	# Kotaro's data
T_b=1.0e5	# electron temp in HII region (Condon 1992)
T_e=8.0e3	# (Condon 1992)
T_e=10.0e3	# (Condon 1992)
n_e=1000.0	# http://www.cv.nrao.edu/course/astr534/HIIRegions.html
#S_TnonT_n3628_88GHz=0.038	# [Jy] @88 GHz ; from Kotaro's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc3628/rms.3628.conti'
#S_TnonT_n3628_88GHz=0.025	# [Jy] @88 GHz ; from Kotaro's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc3628/rms.3628.conti'
#S_TnonT_n3628_88GHz=0.037	# [Jy] @88 GHz ; from Kotaro's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc3628/rms.3628.conti'
S_TnonT_n3628_88GHz=0.04	# [Jy] @88 GHz ; from Kotaro's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc3628/rms.3628.conti'
S_TnonT_n2146_88GHz=0.06	# [Jy] @88 GHz ; from Nakanishi's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc2146/tvstat'
#S_TnonT_n2146_88GHz=0.064	# [Jy] @88 GHz ; from Nakanishi's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc2146/tvstat'
#S_TnonT_n2146_88GHz=0.069	# [Jy] @88 GHz ; from Nakanishi's data 88 GHz ; see file '/iapetus/data/satoki_data/ngc2146/tvstat'
#S_TnonT_m82_100GHz_intef=0.43	# [Jy] @100GHz; (Matsushita 2005)
S_TnonT_m82_100GHz_intef=0.43	# [Jy] @100GHz; (Matsushita 2005)
S_TnonT_m82_87GHz_single=0.54	# [Jy] @87GHz; (Jura et al. 1978)
S_TnonT_m82_92GHz_single=0.59	# [Jy] @92GHz; (Carlstrom et al. 1991)
S_TnonT_n4631_1_5GHz=0.48	# [Jy] @1.49GHz; (Hummel et al 1990)
S_TnonT_n4631_327MHz=0.8	# [Jy] @327MHz; (Hummel et al 1990)
S_T_m82_1GHz=0.7	# [Jy] @1GHz; (Condon 1992)
a_recom_coeff=3.1e-13	# @8000K (orange-cover book p.467)
n_e=1.0e3
n_H=n_e
n_p=n_H
alpha=0.8
dN_uv_O7V=1.0e49	# [photon/s] ; (Maeder 1994) ; http://nedwww.ipac.caltech.edu/level5/March01/Maeder/Maeder5.html
dN_uv_O5V=6.0e49	# [photon/s] ; http://www.cv.nrao.edu/course/astr534/HIIRegions.html
#dN_uv_m82_satoki=2.9e53
# O7V : T_e=38000[K], L=2.6e5[Lsun] ; orange-cover book, p.A-13
eta=0.44	# (Maeder 1994)
gamma=2.35	# (Condon 1992)
M_SN=6.7	# [M_sun] ; (Condon 1992)
M_O7Vstar=30.0	#
alpha_H=3.0e-13	# [cm^3 s^-1] ; http://www.cv.nrao.edu/course/astr534/HIIRegions.html

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
def ttl2thrm(ttl,freq_GHz,type):
	thrm=ttl/(1.0+10*freq_GHz**(0.1-alpha))
	print type,'%.4f' %thrm, "[Jy/Hz]"
	return thrm
print "======================================================"
print "M82 thermal Flux density @(1GHz, Condon 1992) = ", S_T_m82_1GHz, "[Jy/Hz]"

S_T_m82_87GHz_single=ttl2thrm(S_TnonT_m82_87GHz_single,freq_m82_87GHz,"M82 thermal Flux density @(87GHz, single dish) = ")
S_T_m82_92GHz_single=ttl2thrm(S_TnonT_m82_92GHz_single,freq_m82_92GHz,"M82 thermal Flux density @(92GHz, interferometer) = ")
S_T_m82_100GHz_intef=ttl2thrm(S_TnonT_m82_100GHz_intef,freq_m82_100GHz,"M82 thermal Flux density @(100GHz, interferometer) = ")
S_T_n2146_88GHz=ttl2thrm(S_TnonT_n2146_88GHz,freq_n2146_88GHz,"NGC 2146 thermal Flux density @(88GHz) = ")
S_T_n3628_88GHz=ttl2thrm(S_TnonT_n3628_88GHz,freq_n3628_88GHz,"NGC 3628 thermal Flux density @(88GHz) = ")
S_T_n4631_1_5GHz=ttl2thrm(S_TnonT_n4631_1_5GHz,freq_n4631_1_5GHz,"NGC 4631 thermal Flux density @(1.49GHz) = ")
S_T_n4631_327MHz=ttl2thrm(S_TnonT_n4631_327MHz,freq_n4631_327MHz,"NGC 4631 thermal Flux density @(327MHz) = ")

# S=S_T+S_nonT
# flux S_nonT/S_T=10*(freq_GHz)**(0.1-alpha)	# (Condon 1992)
def nonthrm2thrm(nonthrm,freq_GHz,type):
	thrm=nonthrm/(10*freq_GHz**(0.1-alpha))
	print type,'%.3f' %thrm, "[Jy/Hz]"
	return thrm

# luminosity [erg/s/Hz]
def Lun(d_mpc,S,type):
	Lun=4*math.pi*(d_mpc*1.0e6*pc)**2*(S*Jy)
	print type,'%.2e' %Lun,"[erg/s/Hz] (D=",d_mpc, "Mpc)"
	return Lun
print "======"
L_T_m82_1GHz=Lun(d_m82_mpc,S_T_m82_1GHz,"M82 L(thermal) @(1GHz) = ")
L_T_m82_87GHz_single=Lun(d_m82_mpc,S_T_m82_87GHz_single,"M82 L(thermal) @(87GHz single dish) = ")
L_T_m82_92GHz_single=Lun(d_m82_mpc,S_T_m82_92GHz_single,"M82 L(thermal) @(92GHz interferometer) = ")
L_T_m82_100GHz_intef=Lun(d_m82_mpc,S_T_m82_100GHz_intef,"M82 L(thermal) @(100GHz, interferometer) = ")
L_T_n2146_88GHz=Lun(d_n2146_mpc,S_T_n2146_88GHz,"NGC 2146 L(thermal) @(88GHz) = ")
L_T_n3628_88GHz=Lun(d_n3628_mpc,S_T_n3628_88GHz,"NGC 3628 L(thermal) @(88GHz) = ")
L_T_m82_87GHz_single=Lun(d_m82_mpc,S_T_m82_87GHz_single,"M82 L(thermal) @(87GHz single) = ")
L_TnonT_n2146_88GHz=Lun(d_n2146_mpc,S_TnonT_n2146_88GHz,"NGC 2146 L(thrm+non) @(88GHz) = ")
L_TnonT_n3628_88GHz=Lun(d_n3628_mpc,S_TnonT_n3628_88GHz,"NGC 3628 L(thrm+non) @(88GHz) = ")
L_TnonT_m82_87GHz_single=Lun(d_m82_mpc,S_TnonT_m82_87GHz_single,"M82 L(thrm+non) @(87GHz single) = ")
L_nonT_n2146_88GHz=L_TnonT_n2146_88GHz-L_T_n2146_88GHz
L_nonT_n3628_88GHz=L_TnonT_n3628_88GHz-L_T_n3628_88GHz
L_nonT_m82_87GHz_single=L_TnonT_m82_87GHz_single-L_T_m82_87GHz_single
print "NGC 2146 L(nonthrm) @(88GHz) = ",L_nonT_n2146_88GHz, "[erg/s/Hz] (D=", d_n2146_mpc, "Mpc)"
print "NGC 3628 L(nonthrm) @(88GHz) = ",L_nonT_n3628_88GHz, "[erg/s/Hz] (D=",d_n3628_mpc, "Mpc)"
print "M82 L(nonthrm) @(87GHz single) = ",L_nonT_m82_87GHz_single, "[erg/s/Hz] (D=",d_m82_mpc, "Mpc)"
#print "------"

# production rate [s-1]	# (Condon 1992)
def dN_uv(freq_GHz,L_thrm,type):
	dN_uv=6.3e52*(T_e/1.0e4)**(-0.45)*(freq_GHz)**(0.1)*(L_thrm/1.0e27)
#	dn_H2=L_thrm/(E_bndion_erg*N_A)
	dn_H2=dN_uv*E_bndion_erg/(N_A*2)
	L_H2=dN_uv*E_bndion_erg/2
#	dM_H2=dn_H2*2*yr/Msun
#	dM_H2=dN_H2*2*m_p*yr/Msun
#i	L_uv=dN_uv*E_bndion_erg
	dM_uv=dN_uv*m_e
#	dM_uv=dN_uv*m_p
#	dM_uv=dN_uv/N_A
	dM_uv_Msunyr=dM_uv/Msun*yr
	n_O7Vstar=dN_uv/dN_uv_O7V
	n_Ostar=n_O7Vstar/eta
	M_HI_II_Msun=dN_uv/7.9e44/1000.0**0.36
	M_ion_SBR=dN_uv*m_p/(alpha_H*n_p)	# need reference, see Tsai et al. 2010
	M_ion_SBR_Msun=M_ion_SBR/Msun
#	mass=n_O7Vstar*M_O7Vstar
	mass=n_Ostar*M_O7Vstar	# Anantharamaiah, et al. 2000
	print "---",type,"---"
	print "production rate = ", '%.2e' %dN_uv, "[photon/s]"
	print "thermal luminosity = ", '%.2e' %L_thrm, "[erg/s]"
#	print "corresponding total luminosity = ", '%.2e' %L_uv, "[erg/s]"
	print "corresponding total mass loss rate = ", '%.2f' %dM_uv_Msunyr, "[Msun/yr]"
#	print "corresponding total H2 lose rate = ", '%.2e' %dn_H2, "[1/s]",'%.2e' %dM_H2, "[Msun/yr]"
	print "# of O7V-type stars = ", '%.2e' %n_O7Vstar
	print "# of O-type stars = ", '%.2e' %n_Ostar
	print "corresponding total mass = ", '%.2e' %mass
	print "total ionized gas mass = ", '%.2e' %M_HI_II_Msun, "[Msun]"
	print "ionized gas mass in SBR = ", '%.2e' %M_ion_SBR_Msun, "[Msun]"
	return dN_uv
print "-----------------------------------------------"
print " dN_uv=6.3e52*(T_e/1.0e4)**(-0.45)*freq**(0.1)*(L_thrm/1.0e27) (Condon 1992) "
print "-----------------------------------------------"
print "O7V-type star production rate = ", dN_uv_O7V, "[photon/s]"
print "# of O-type star in our Galaxy ~ 6500 (Roberts 1957, PASP)"
#print "------"
#dN_uv_m82_satoki_pr=2.9e53
#print "M82 production rate (A,B,C,D,E,F,G) @100GHz (Matsushita et al. 2005) = ",dN_uv_m82_satoki_pr ,"[photon/s]"
dN_uv_m82_condon=dN_uv(freq_m82_1GHz,L_T_m82_1GHz,"M82 (condon 1992; 1GHz)")
print
dN_uv_m82_jura_single=dN_uv(freq_m82_87GHz,L_T_m82_87GHz_single,"M82 single dish (Jura 1978)")
dN_uv_m82_carlstrom_interf=dN_uv(freq_m82_92GHz,L_T_m82_92GHz_single,"M82 interferometer (Carlstrom 1991)")
dN_uv_m82_satoki_intef=dN_uv(freq_m82_100GHz,L_T_m82_100GHz_intef,"M82 interferometer (satoki 2005; 100GHz)")
dN_uv_n2146=dN_uv(freq_n2146_88GHz,L_T_n2146_88GHz,"NGC 2146")
dN_uv_n3628=dN_uv(freq_n3628_88GHz,L_T_n3628_88GHz,"NGC 3628")


# --- SFR -----------------------------------------	#
def SFR_Ha_K(L_Ha,type):
	sfr=7.9e-42*L_Ha
	print type,'%.2f' %sfr, "[M_sun/yr]"
print "-----------------------------------------------"
print " SFR_Ha=7.9e-42*L_Ha (IMF=-2.35; 0.1-100M; Kennicut 1998)"
print "-----------------------------------------------"
SFR_Ha_K_n253=SFR_Ha_K(L_Ha_n253, "NGC 253 SFR (Ha) (data) = ")
SFR_Ha_K_m82=SFR_Ha_K(L_Ha_m82, "M82 SFR (Ha) (data) = ")
print "    M82: 5 Msun/yr (Tarchi et al. 2000)"
SFR_Ha_K_n2146=SFR_Ha_K(L_Ha_n2146, "NGC 2146 SFR (Ha) (data) = ")
print "    NGC 2146: 15 Msun/yr (Tarchi et al. 2000)"
SFR_Ha_K_n3628=SFR_Ha_K(L_Ha_n3628, "NGC 3628 SFR (Ha) (data) = ")


def SFR_Ha(L_Ha,type):
	sfr=1.0e-41*L_Ha	# (Thronson 1991)
	print type, '%.2f' %sfr, "[M_sun/yr]"
	return sfr
print "-----------------------------------------------"
print " SFR_Ha=1.0e-41*L_Ha (IMF:-2.35; 0.1-100Msun; Thronson 1991) "
print "-----------------------------------------------"
SFR_Ha_n253=SFR_Ha(L_Ha_n253, "NGC 253 SFR (Ha) (data) = ")
SFR_Ha_m82=SFR_Ha(L_Ha_m82, "M82 SFR (Ha) (data) = ")
print "    M82: 5 Msun/yr (Tarchi et al. 2000)"
SFR_Ha_n2146=SFR_Ha(L_Ha_n2146, "NGC 2146 SFR (Ha) (data) = ")
print "    NGC 2146: 15 Msun/yr (Tarchi et al. 2000)"
SFR_Ha_n3628=SFR_Ha(L_Ha_n3628, "NGC 3628 SFR (Ha) (data) = ")

def SFR_IR_K(L_IR,type):
	sfr=4.5e-44*L_IR*Lsun	# (Kennicutt 1998)
	print type,'%.2f' %sfr, "[M_sun/yr]"
	return sfr
print "-----------------------------------------------"
print " SFR_IR=4.5e-44*L_IR (0.1-100M; IMF=-2.35; starburst age 10-100Myr >5Msun) (Kennicut 1998) "
print "-----------------------------------------------"
SFR_IR_K_m82=SFR_IR_K(L_IR_m82,"M82 SFR (FIR) (data)")
SFR_IR_K_n253=SFR_IR_K(L_IR_n253,"NGC 253 SFR(FIR) (data)")
SFR_IR_K_n4631=SFR_IR_K(L_IR_n4631,"NGC 4631 SFR (FIR) (data)")
SFR_IR_K_n2146=SFR_IR_K(L_IR_n2146,"NGC 2146 SFR (FIR) (data)")
SFR_IR_K_n3628=SFR_IR_K(L_IR_n3628,"NGC 3628 SFR (FIR) (data)")

def SFR_IR_C(L_IR,type):
	sfr=1/1.1e10*L_IR	# (Condon 1992)
	sfr_235=sfr/1.6
	sfr_235_t=sfr_235*5.51
	sfr_235_1=sfr_235*2.16
	sfr_t=sfr*8.82
	sfr_1=sfr*2.59
	print type
	print "    IMF=-2.5 | SFR(>5M) =", '%.2f' %sfr, "| SFR(0.1-100) =",'%.2f' %sfr_t, "| SFR(1-100) =",'%.2f' %sfr_1
	print "    IMF=-2.35 | SFR(>5M) =", '%.2f' %sfr_235, "| SFR(0.1-100) =",'%.2f' %sfr_235_t, "| SFR(1-100) =",'%.2f' %sfr_235_1
	return sfr_235
print "-----------------------------------------------"
print " SFR_IR(>5Msun)=1/1.1e10*L_IR (IMF index=-2.5) (Condon 1992) "
print "-----------------------------------------------"
SFR_IR_C_m82=SFR_IR_C(L_IR_m82,"M82 SFR(>5Msun) (IR) (data)")
SFR_IR_C_n253=SFR_IR_C(L_IR_n253,"NGC 253 SFR(>5Msun) (IR) (data)")
SFR_IR_C_n4631=SFR_IR_C(L_IR_n4631,"NGC 4631 SFR(>5Msun) (IR) (data)")
SFR_IR_C_n2146=SFR_IR_C(L_IR_n2146,"NGC 2146 SFR(>5Msun) (IR) (data)")
SFR_IR_C_n3628=SFR_IR_C(L_IR_n3628,"NGC 3628 SFR(>5Msun) (IR) (data)")

def SFR_dN_ion(dN_uv,sfr_IR_K,sfr_IR_C,type):
	sfr=1.08e-53*dN_uv	# (Kennicutt 1998) # (http://0rz.tw/DzdAK ; Johnson 2004)
	ratio_K=sfr/sfr_IR_K*100.0
	ratio_C=sfr/sfr_IR_C*100.0
	print type,'%.2f' %sfr, "[M_sun/yr] <==="
	print "  SFR_radio = ", '%.2f' %sfr_IR_K, "[M_sun/yr] | SFR_radio(total)/FIR(starburst) = ", '%.2f' %ratio_K, "%"
	print "  SFR_radio = ", '%.2f' %sfr_IR_C, "[M_sun/yr] | SFR_radio(total)/FIR(>5M) = ", '%.2f' %ratio_C, "%"
	print
	return sfr
print "-----------------------------------------------"
print " SFR_dN_ion=1.08e-53*dN_uv (Salpeter 0.1-100 Msun index=-2.35) (Kennicut 1998)"
print "-----------------------------------------------"
SFR_radio_m82_condon=SFR_dN_ion(dN_uv_m82_condon,SFR_IR_K_m82,SFR_IR_C_m82,"M82 SFR (radio) (O, Condon 1992 data; 1GHz) =")	
#SFR_radio_m82_pr_satoki_pr=SFR_dN_ion(dN_uv_m82_satoki_pr,"M82 SFR (radio) (O, Matsushita 2005 data, from production rate) = ")	
SFR_radio_m82_pr_jura_single=SFR_dN_ion(dN_uv_m82_jura_single,SFR_IR_K_m82,SFR_IR_C_m82,"M82 SFR (radio single dish) (O, Jura 1978 data) =")
SFR_radio_m82_pr_carlstrom_interf=SFR_dN_ion(dN_uv_m82_carlstrom_interf,SFR_IR_K_m82,SFR_IR_C_m82,"M82 SFR (radio interferometer) (O, Carlstrom 1991 data) =")
SFR_radio_m82_pr_satoki_intef=SFR_dN_ion(dN_uv_m82_satoki_intef,SFR_IR_K_m82,SFR_IR_C_m82,"M82 SFR (radio interferometer) (O, Matsushita 2005 data) =")
SFR_radio_n2146_pr=SFR_dN_ion(dN_uv_n2146,SFR_IR_K_n2146,SFR_IR_C_n2146,"NGC 2146 SFR (radio) (O, our data; 88GHz) =")
SFR_radio_n3628_pr=SFR_dN_ion(dN_uv_n3628,SFR_IR_K_n3628,SFR_IR_C_n3628,"NGC 3628 SFR (radio) (O, our data; 88GHz) =")
#SFR_radio_n253_pr=SFR_dN_ion(dN_uv_n253,SFR_IR_K_n253,SFR_IR_C_n253,"NGC 253 SFR (radio) (O, our data; 88GHz) =")

def SFR_dN_uv(dN_uv,sfr_g_IR_C_5m,type):
	sfr_sbr_radio_5m=1/3.5e53*dN_uv	# (Condon 1992)
	ratio=sfr_sbr_radio_5m/sfr_g_IR_C_5m*100
	sfr_sbr=sfr_sbr_radio_5m*5.5
	sfr_g=sfr_g_IR_C_5m*5.5
	print type,"SBR SFR_radio(>5Msun)", '%.2f' %sfr_sbr_radio_5m, "[M_sun/yr]"
	print "   SBR SFR_radio(>0.1Msun)", '%.2f' %sfr_sbr, "[M_sun/yr]"
	print "   global SFR_IR(>5Msun) =", '%.2f' %sfr_g_IR_C_5m, "[M_sun/yr]"
	print "   global SFR_IR(>0.1Msun) =", '%.2f' %sfr_g, "[M_sun/yr]"
	print "   SFR ratio of SBR/global =", '%.2f' %ratio, "%"
	return sfr_sbr
print "-----------------------------------------------"
print " SFR_dN_uv(>5Msun)=1/3.5e53*dN_uv (IMF:-2.5; Condon 1992) "
print "-----------------------------------------------"
SFR_dN_uv_m82_condon=SFR_dN_uv(dN_uv_m82_condon, SFR_IR_C_m82,"M82 SFR (condon 1992) =")
SFR_dN_uv_m82_jura_single=SFR_dN_uv(dN_uv_m82_jura_single, SFR_IR_C_m82, "M82 single dish (Jura 1978) =")
SFR_dN_uv_m82_carlstrom_interf=SFR_dN_uv(dN_uv_m82_carlstrom_interf, SFR_IR_C_m82, "M82 interferometer (Carlstrom 1991) =")
SFR_dN_uv_m82_satoki_intef=SFR_dN_uv(dN_uv_m82_satoki_intef, SFR_IR_C_m82,"M82 interferometer (satoki 2005) =")
SFR_dN_uv_n2146=SFR_dN_uv(dN_uv_n2146,SFR_IR_C_n2146, "NGC 2146 =")
SFR_dN_uv_n3628=SFR_dN_uv(dN_uv_n3628, SFR_IR_C_n3628,"NGC 3628 =")


def SFR_radio5m(L_T,freq_GHz,type):
	sfr_5m=1.82e-28*L_T*(freq_GHz)**0.1
#	sfr_1m=sfr_5m*9	# (Rosa-Gonzalez)
	sfr_01m=sfr_5m*5.5	# (Rosa-Gonzalez)
	print type, "SFR(>5Msun) =", '%.2f' %sfr_5m, "[M_sun/yr] | SFR(>0.1Msun) =", '%.2f' %sfr_01m
	return sfr_01m
print "-----------------------------------------------"
print "SFR_radio(>5M) = 1.82e-28*L_T*(freq_GHz)^0.1 (Condon 1992)"
print "-----------------------------------------------"
SFR_Radio_n2146=SFR_radio5m(L_T_n2146_88GHz,freq_n2146_88GHz,"NGC 2146")
SFR_Radio_n3628=SFR_radio5m(L_T_n3628_88GHz,freq_n3628_88GHz,"NGC 3628")
SFR_Radio_m82_inte_100GHz=SFR_radio5m(L_T_m82_100GHz_intef,freq_m82_100GHz,"M82 radio interferometer 100GHz")
SFR_Radio_m82_sing_87GHz=SFR_radio5m(L_T_m82_87GHz_single,freq_m82_87GHz,"M82 radio single dish 87GHz")
SFR_Radio_m82_interf_92GHz=SFR_radio5m(L_T_m82_92GHz_single,freq_m82_92GHz,"M82 radio interferometer 92 GHz")




# L_nonT/1.0e7=5.3e21*freq_GHz**(-alpha)*(SFR_5Msun) (Condon 1992)
# L_T/1.0e7=5.5e20*freq_GHz**(-0.1)*(SFR_5Msun)	(Condon 1992)
def SFR_radio_5Msun(L_T,freq_GHz,type):
	sfr5=L_T*1.0e-7*freq_GHz**0.1/5.5e20
	print type, '%.2f' %sfr5, "[M_sun/yr]"
	return sfr5
print "-----------------------------------------------"
print " SFR_radio (>5Msun)=L_T*1.0e-7*freq_GHz^0.1/5.5e20 (IMF:-2.5; Condon 1992) "
print "-----------------------------------------------"
SFR_radio_m82_5M_satoki_intef=SFR_radio_5Msun(L_T_m82_100GHz_intef,freq_m82_100GHz,"M82 SFR (radio interferometer 100GHz) (>5Msun OB, theory) = ")
SFR_radio_m82_5M_jura_single=SFR_radio_5Msun(L_T_m82_87GHz_single,freq_m82_87GHz,"M82 SFR (radio single dish 87GHz) (>5Msun OB, theory) = ")
SFR_radio_m82_5M_carlstrom_interf=SFR_radio_5Msun(L_T_m82_92GHz_single,freq_m82_92GHz,"M82 SFR (radio interferometer 92GHz) (>5Msun OB, theory) = ")
SFR_radio_n2146_5M=SFR_radio_5Msun(L_T_n2146_88GHz,freq_n2146_88GHz,"NGC 2146 SFR (radio) (>5Msun OB, theory) = ")
SFR_radio_n3628_5M=SFR_radio_5Msun(L_T_n3628_88GHz,freq_n3628_88GHz,"NGC 3628 SFR (radio) (>5Msun OB, theory) = ")

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
print "    SN rate M82: 0.06 SN/yr (Tarchi et al. 2000)"
r_SN_IR_n2146=r_SN_IR(L_IR_n2146,"NGC 2146 SN rate (IR) (data) =")
print "    SN rate NGC 2146: 0.15 SN/yr (Tarchi et al. 2000)"
r_SN_IR_n3628=r_SN_IR(L_IR_n3628,"NGC 3628 SN rate (IR) (data) =")
#r_SN_IR_n3628=2.3e-12*L_IR_n3628	# (van Buren & Greenhouse 1994)
# r_SN=integral(M^(-gamma))dM # (Condon 1992)
r_SN_radio_1=(M_SN)**(-gamma+1)

def r_SN_radio(SFR_radio, type):
	r_SN=0.041*SFR_radio	# M>5Msun (Condon 1992)
	SFR_r_SN=r_SN*24.4*5.5	# Salpeter IMF
#	SFR_r_SN=r_SN*24.4*9	# (Rosa-Gonzalez 2005)
	print type,'%.2f' %r_SN,"[SN/yr]"
	print "     total SFR (>0.1Msun) = ", '%.2f' %SFR_r_SN, "[Msun/yr]"
print "-----------------------------------------------"
print " r_SN_radio=0.041*SFR_radio (M>5Msun; IMF:-2.5; Condon 1992) "
print "-----------------------------------------------"
r_SN_radio_m82_condon=r_SN_radio(SFR_radio_m82_condon,"M82 SN rate (radio) (Condon 1992 data; 1GHz) =")
#r_SN_radio_m82_pr_satoki_pr=r_SN_radio(SFR_radio_m82_pr_satoki_pr,"M82 SN rate (radio) (Matsusthia 2005 data, form production rate) =")
#r_SN_radio_m82_pr_jura_single=r_SN_radio(SFR_radio_m82_pr_jura_single,"M82 SN rate (radio) single dish (Jura 1978 data) =")
print
r_SN_radio_m82_5M_jura_single=r_SN_radio(SFR_radio_m82_5M_jura_single,"M82 SN rate (radio) single dish (Jura 1978 data, >5Msun OB) =")
r_SN_radio_m82_5M_carlstrom_interf=r_SN_radio(SFR_radio_m82_5M_carlstrom_interf,"M82 SN rate (radio) interferometer (Carlstrom 1991 data, >5Msun OB) =")
#r_SN_radio_m82_pr_satoki_intef=r_SN_radio(SFR_radio_m82_pr_satoki_intef,"M82 SN rate (radio) interferometer (Matsusthia 2005 data; 100GHz) =")
r_SN_radio_m82_5M_satoki_intef=r_SN_radio(SFR_radio_m82_5M_satoki_intef,"M82 SN rate (radio) interferometer (Matsusthia 2005 data, >5Msun OB) =")
#r_SN_radio_n2146_pr=r_SN_radio(SFR_radio_n2146_pr,"NGC 2146 SN rate (radio) (our data; 88GHz) =")
r_SN_radio_n2146_5M=r_SN_radio(SFR_radio_n2146_5M,"====> NGC 2146 SN rate (radio) (our data, >5Msun OB) =")
#r_SN_radio_n3628_pr=r_SN_radio(SFR_radio_n3628_pr,"NGC 3628 SN rate (radio) (our data; 88GHz) =")
r_SN_radio_n3628_5M=r_SN_radio(SFR_radio_n3628_5M,"====> NGC 3628 SN rate (radio) (our data, >5Msun OB) =")

print "NGC 3628 SN rate (radio) (6.7Msun OB, theory) =", r_SN_radio_1, "[SN/yr]"

def r_SN_con(L_nonT,freq_GHz,type):
	r_SN=L_nonT/13.0e27*freq_GHz**0.75
	print type, '%.2f' %r_SN
print "-----------------------------------------------"
print " r_SN=L_nonT/13e27*nu_GHz^0.75 (Condon 1992) "
print "-----------------------------------------------"
r_SN_con(L_nonT_n2146_88GHz,freq_n2146_88GHz, "NGC 2146:")
r_SN_con(L_nonT_n3628_88GHz,freq_n3628_88GHz, "NGC 3628:")
r_SN_con(L_nonT_m82_87GHz_single,freq_m82_87GHz, "M82 single dish:")


# -----------------------------------------------------	#
# Anantharamaiah, et al. 2000, ApJ, 537, 613
# Bieging et al. 1989, ApJ, 340, 518B
# Condon 1992, ARAA, 30, 575
# Kennicutt 1998, ARAA, 36, 189a
# Johnson 2004, NewAstronomyReview, 48, 1337
# Maeder 1994, ARAA, 32, 227
# Matsushita et al. 2005, ApJ, 618, 712
# Roberts 1957, PASP, 69, 59R
# Rosa-Gonzalez 2005, MNRAS, 364, 1304
# Sanders et al. 2003, ApJ, 126, 1607
# Strickland et al. 2004, ApJ, 606, 829 
# Thronson et al. 1991, MNRAS, 252,543
# van Buren & Greenhouse 1994, ApJ, 431, 640

exit
