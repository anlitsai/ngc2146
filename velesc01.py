#!/usr/bin/env python

# --- import constant ------------------------- #
import math
# --- constant -------------------------------- #
Lsun=3.98e33	# [erg/s]
Msun=1.98e33	# [g]
yr=365*86400	# [sec]
c=3.0e10	# [cm/s]
ly=c*yr		# [cm]
pc=3.26*ly	# [cm]
kpc=pc*1000	# [cm]
k_B=1.38e-16
c=2.99e10	# [cm/s]
Jy=1.0e-23	# [ergs cm-2 s-1 Hz-1]
G=6.67e-8	# [cm3 g-1 s-2]
# --- parameter ------------------------------- #
M1_dsk=9.9e10	# [Msun]
M1_molotf=3.4e8	# [Msun]
M1_molbbl=2.6e8	# [Msun]
M2_dsk=3.0e10	# [Msun]
M2_molotf=3.0e7	# [Msun]
R1_molotf=2.0	# [kpc]
R1_molbbl=1.0	# [kpc]
R2_molotf=0.5	# [kpc]
a_3mm_N2146_kpc=3.0	# [kpc]
b_3mm_N2146_kpc=0.7	# [kpc]
sfr_3mm_N2146_MsunYr=20.01	# [Msun/yr]
sfr_3mm_N2146_MsunYr=3.8	# [Msun/yr]
surden1_CO_N2146_MsunPc2=550	# [Msun/pc2]
surden2_CO_N2146_MsunPc2=150	# [Msun/pc2]
surden_CO_N2146_MsunPc2=362	# [Msun/pc2]
surden_CO_N3628_MsunPc2=594	# [Msun/pc2]
surden_normal_MsunPc2=100	# [Msun/pc2]

# ----------------------------------------------------- #

def v_esc(m_Msun,r_kpc,type):
	m=m_Msun*Msun
	r=r_kpc*kpc
	v=math.sqrt(2*G*m/r)
	v_kms=v/1.0e5
	print type, "escape velocity = ", '%.2e' %v_kms, "[km/s]"
	return v_kms

def t_ff(m1_Msun,m2_Msun,r_kpc,type):
	m1=m1_Msun*Msun
	m2=m2_Msun*Msun
	r=r_kpc*kpc
	t=math.pi/2*r**1.5/math.sqrt(2*G*(m1+m2))
	t_yr=t/yr
	print type, "free-fall timescale = ", '%.2e' %t_yr, "[yr]"
	return t_yr

def t_sbrst(a_kpc,b_kpc,sfr_MsunYr,surden_MsunPc2,type):
	ab_pc2=a_kpc*b_kpc*1000**2
	sfr_den=sfr_MsunYr/ab_pc2
	t_yr=(surden_MsunPc2-surden_normal_MsunPc2)/sfr_den
	print type, "starburst time will be finished in = ", '%.2e' %t_yr, "[yr]"
	return t_yr


print "-------------------------------"
v=v_esc(M1_dsk,R1_molotf,"N2146 OF")
v=v_esc(M1_dsk,R1_molbbl,"N2146 SB")
t=t_ff(M1_molotf,M1_dsk,R1_molotf,"N2146 OF")
t=t_ff(M1_molbbl,M1_dsk,R1_molbbl,"N2146 SB")
t=t_ff(M2_molotf,M2_dsk,R2_molotf,"N3628 OF")
t=t_sbrst(a_3mm_N2146_kpc,b_3mm_N2146_kpc,sfr_3mm_N2146_MsunYr,surden1_CO_N2146_MsunPc2,"N2146 OF")
t=t_sbrst(a_3mm_N2146_kpc,b_3mm_N2146_kpc,sfr_3mm_N2146_MsunYr,surden2_CO_N2146_MsunPc2,"N2146 OF")
t=t_sbrst(a_3mm_N2146_kpc,b_3mm_N2146_kpc,sfr_3mm_N2146_MsunYr,surden_CO_N2146_MsunPc2,"N2146 OF")
t=t_sbrst(a_3mm_N3628_kpc,b_3mm_N3628_kpc,sfr_3mm_N3628_MsunYr,surden_CO_N3628_MsunPc2,"N3628 OF")
print "-------------------------------"



# ---- reference -------------------------------------- #
# http://en.wikipedia.org/wiki/Escape_velocity
# http://en.wikipedia.org/wiki/Free-fall_time
# ----------------------------------------------------- #
exit
