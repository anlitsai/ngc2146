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
M1_molttl=4.2e9	# [Msun]
M2_dsk=5.0e10	# [Msun]
M2_molotf=3.0e7	# [Msun]
M2_molttl=3.6e9	# [Msun]
R1_molotf=2.0	# [kpc]
R1_molbbl=1.0	# [kpc]
R2_molotf=0.5	# [kpc]
#area_3mm_N2146_kpc2=2.38	# [kpc2]
#area_3mm_N2146_kpc2=0.58	# [kpc2]
area_3mm_N2146_kpc2=2.17	# [kpc2]
area_3mm_N3628_kpc2=0.22	# [kpc2]
sfr_3mm_N2146_MsunYr=20.01	# [Msun/yr]
sfr_3mm_N3628_MsunYr=3.8	# [Msun/yr]
rate1_massloss_N2146=26.0	# [Msun/yr]
rate2_massloss_N2146=54.0	# [Msun/yr]
rate1_massloss_N3628=4.0	# [Msun/yr]
rate2_massloss_N3628=10.0	# [Msun/yr]
#surden_CO_N2146_MsunPc2=362	# [Msun/pc2]
surden_CO_N2146_MsunPc2=382	# [Msun/pc2]
#surden_CO_N3628_MsunPc2=594	# [Msun/pc2]
surden_CO_N3628_MsunPc2=399	# [Msun/pc2]
surden_normal_MsunPc2=100	# [Msun/pc2]
effi1=0.1
E_Ostar_N2146=420*1.0e54	# [erg]
E_Ostar_N3628=79*1.0e54		# [erg]
E_ion_N2146=100*1.0e54	# [erg]
E_ion_N3628=0.2*1.0e54	# [erg]
v_exp_N2146_kms=200.0	# [km/s]
v_exp_N3628_kms=90.0	# [km/s]
drag_coeffi=0.4
# ----------------------------------------------------- #

def v_esc(m_Msun,r_kpc,type):
	m=m_Msun*Msun
	r=r_kpc*kpc
	v=math.sqrt(2*G*m/r)
	v_kms=v/1.0e5
	print type, "escape velocity = ", '%.2f' %v_kms, "[km/s]"
	return v_kms

def t_ff(M_dsk_Msun,m_Msun,r_kpc,type):
	m1=M_dsk_Msun*Msun
	m2=m_Msun*Msun
	r=r_kpc*kpc
#	t=math.pi*r**1.5/math.sqrt(G*(m1+m2))
#	t=math.pi/2*r**1.5/math.sqrt(2*G*(m1+m2))
#	t=math.pi/2*r**1.5/math.sqrt(G*(m1+m2))
	t=math.pi/2*(2*r)**1.5/math.sqrt(2*G*(m1+m2))
	t_myr=t/yr/1.0e6
	print type, "free-fall timescale = ", '%.2f' %t_myr, "[Myr]"
	return t_myr

def t_SF(area_kpc2,sfr_MsunYr,surden_MsunPc2,type):
	sfr_den=sfr_MsunYr/(area_kpc2*1.0e6)
	t_myr=(surden_MsunPc2-surden_normal_MsunPc2)/sfr_den/1.0e6
	print type, "(hold; surface density) molecular gas consumption time will be finished in = ", '%.2f' %t_myr, "[Myr]"
	return t_myr

def t_consump_mass_SFR(SFR_Msunyr,rate1_massloss,rate2_massloss,total_mass_Msun,type):
	rate1=SFR_Msunyr+rate1_massloss
	rate2=SFR_Msunyr+rate2_massloss
	t1_myr=total_mass_Msun/rate1/1.0e6
	t2_myr=total_mass_Msun/rate2/1.0e6
	print type, "molecular gas consumption time will be finished in = ", '%.2f' %t2_myr,"-",'%.2f' %t1_myr, "[Myr]"
	return t1_myr,t2_myr

def t_2disk(M_dsk_Msun,m_Msun,r_kpc,effi,E_Ostar,E_ion,type):
	m1=M_dsk_Msun*Msun
	m2=m_Msun*Msun
	r=r_kpc*kpc
	E_grav=G*m1*m2/(2*r)
#	E_kin=1*E_Ostar
	E_kin=effi*E_Ostar
	dE=E_grav-E_kin-E_ion
	print "E_grav=", E_grav,"[erg] ; E_kin=", E_kin,"[erg] (efficiency =",effi, ") ; E_ion=", E_ion, "[erg] ; dE=",dE,"[erg]"
	v=math.sqrt(dE*2/m2)
#	print "v=",v/1.0e5 ,"km/s"
	t_half_myr=math.pi*r/v/yr/1.0e6
	print type, "molecular gas will return to disk = ", '%.2f' %t_half_myr, "[Myr]"
	return t_half_myr

def t_after_stbrst(t_later_myr,M_dsk_Msun,m_Msun,r_kpc,effi,E_Ostar,SFR_MsunYr,v_exp_kms,type):
	t_later_yr=t_later_myr*1.0e6
	mass_SF=SFR_MsunYr*t_later_yr*Msun
	m1=M_dsk_Msun*Msun-mass_SF
	m2=m_Msun*Msun-mass_SF*0.9
	v_exp=v_exp_kms*1.0e5
	r=(r_kpc*kpc+v_exp*t_later_yr*yr)
	E_grav=G*m1*m2/(2*r)
	E_kin=effi*E_Ostar
	dE=E_grav-E_kin
	v_kin=math.sqrt(dE*2/m2)
	v_kin_kms=v_kin/1.0e5
	print "E_grav=", E_grav,"[erg] ; E_kin=", E_kin,"[erg] ; dE=",dE,"[erg] ; v_kin=",'%.1f' %v_kin_kms ,"km/s"
	t_half_myr=math.pi*r/v/yr/1.0e6
	print type, t_later_myr,"Myr later, starburst time will be finished in = ", '%.2f' %t_half_myr, "[Myr]"
	return t_half_myr

	

print "-------------------------------"
v=v_esc(M1_dsk,R1_molotf,"N2146 OF")
v=v_esc(M1_dsk,R1_molbbl,"N2146 SB")
v=v_esc(M2_dsk,R2_molotf,"N3628 SB (not yet measure rotation curve)")
t=t_ff(M1_molotf,M1_dsk,R1_molotf,"N2146 OF")
t=t_ff(M1_molbbl,M1_dsk,R1_molbbl,"N2146 SB")
t=t_ff(M2_molotf,M2_dsk,R2_molotf,"N3628 OF")
t=t_SF(area_3mm_N2146_kpc2,sfr_3mm_N2146_MsunYr,surden_CO_N2146_MsunPc2,"N2146 OF")
t=t_SF(area_3mm_N3628_kpc2,sfr_3mm_N3628_MsunYr,surden_CO_N3628_MsunPc2,"N3628 OF")
t=t_2disk(M1_dsk,M1_molotf,R1_molotf,effi1,E_Ostar_N2146,E_ion_N2146,"N2146 OF")
t=t_2disk(M1_dsk,M1_molbbl,R1_molbbl,effi1,E_Ostar_N2146,E_ion_N2146,"N2146 SB")
t=t_2disk(M2_dsk,M2_molotf,R2_molotf,effi1,E_Ostar_N3628,E_ion_N3628,"N3628 OF")
t=t_consump_mass_SFR(sfr_3mm_N2146_MsunYr,rate1_massloss_N2146,rate2_massloss_N2146,M1_molttl,"N2146")
t=t_consump_mass_SFR(sfr_3mm_N3628_MsunYr,rate1_massloss_N3628,rate2_massloss_N3628,M2_molttl,"N3628")
print "-------------------------------"
#t=t_after_stbrst(1.0,M1_dsk,M1_molotf,R1_molotf,effi,E_Ostar_N2146,sfr_3mm_N2146_MsunYr,v_exp_N2146_kms,"N2146 OF")
#t=t_after_stbrst(10.0,M1_dsk,M1_molotf,R1_molotf,effi,E_Ostar_N2146,sfr_3mm_N2146_MsunYr,v_exp_N2146_kms,"N2146 OF")
#t=t_after_stbrst(1.0,M2_dsk,M2_molotf,R2_molotf,effi,E_Ostar_N3628,sfr_3mm_N3628_MsunYr,v_exp_N3628_kms,"N3628 OF")
#t=t_after_stbrst(10.0,M2_dsk,M2_molotf,R2_molotf,effi,E_Ostar_N3628,sfr_3mm_N3628_MsunYr,v_exp_N3628_kms,"N3628 OF")
print "-------------------------------"



# ---- reference -------------------------------------- #
# http://en.wikipedia.org/wiki/Escape_velocity
# http://en.wikipedia.org/wiki/Free-fall_time
# http://www.grc.nasa.gov/WWW/K-12/airplane/termv.html
# http://www.grc.nasa.gov/WWW/K-12/airplane/shaped.html
# http://en.wikipedia.org/wiki/Terminal_velocity
# http://en.wikipedia.org/wiki/Drag_coefficient
# ----------------------------------------------------- #
exit
