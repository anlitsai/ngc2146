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

def mdyn(vrot_kms,r_kpc,type):
	r=r_kpc*kpc
	v=vrot_kms*1.0e5
	m=r*v**2/G
	m_Msun=m/Msun
 	print type, "Mdyn = ",'%.2e'  %m_Msun,"[Msun], v_rot =",'%.2f' %vrot_kms,"[km/s]"
	return m_Msun
print "-------------------------------"
m=mdyn(220.0,1.5,"N3628")
m=mdyn(210.0,1.5,"N3628")
print "-------------------------------"


def ve0(Mof_Msun,vof_kms,Eion,type):
	m=Mof_Msun*Msun
	v=vof_kms*1.0e5
	Eof=0.5*m*v**2
	ve=math.sqrt((2/m)*(Eof+Eion))
	ve_kms=ve/1.0e5
	print type, "v_equiv = ",ve_kms,"[km/s] ,M_of = ", '%.2e' %Mof_Msun,"[Msun], v_of = ",'%.2f' %vof_kms,"[km/s], E_ion = ", '%.2f' %Eion," [erg]"
	return ve_kms
print "-------------------------------"
v=ve0(2.8e7,90.0,0.71e54*0.1,"N3628")
print "-------------------------------"


def ve(Mof_Msun,vof_kms,Eion,Esn,eta_thrm,eff_mech,type):
	m=Mof_Msun*Msun
	v=vof_kms*1.0e5
	Eof=0.5*m*v**2
	ve=math.sqrt((2/m)*(Eof+Eion+(eta_thrm+eff_mech)*Esn))
	ve_kms=ve/1.0e5
	print type, "v_equiv = ",ve_kms,"[km/s] ,M_of = ", '%.2e' %Mof_Msun,"[Msun], v_of = ",'%.2f' %vof_kms,"[km/s], E_ion = ", '%.2f' %Eion," [erg]"
	return ve_kms
print "-------------------------------"
v=ve(2.8e7,90.0,0.71e54*0.1,4.5e4*1.0e51,0.3,0.1,"N3628")
print "-------------------------------"





def z_max(Mdisk_Msun,v_kms,z_kpc,type):
	m=Mdisk_Msun*Msun
	z=z_kpc*kpc
	v=v_kms*1.0e5
	z_max_cm=(1/z-v**2/(math.sqrt(2)*G*m))**(-1)
	z_max=z_max_cm/kpc
	print type, "M_dyn = ", '%.2e' %Mdisk_Msun,"[Msun], v_of = ",'%.2f' %v_kms,"[km/s], z_of = ", '%.2f' %z_kpc," [kpc], z_max = ", '%.2f' %z_max, "[kpc]"
	return z_max

print "-------------------------------"
z=z_max(2.0e10,90.0,0.4,"N3628")
z=z_max(1.7e10,90.0,0.4,"N3628")
z=z_max(2.0e10,270.0,0.4,"N3628")
z=z_max(1.7e10,270.0,0.4,"N3628")
print "-------------------------------"
print 0.56/37, 0.4/37


# ---- reference -------------------------------------- #
# http://en.wikipedia.org/wiki/Escape_velocity
# http://en.wikipedia.org/wiki/Free-fall_time
# http://www.grc.nasa.gov/WWW/K-12/airplane/termv.html
# http://www.grc.nasa.gov/WWW/K-12/airplane/shaped.html
# http://en.wikipedia.org/wiki/Terminal_velocity
# http://en.wikipedia.org/wiki/Drag_coefficient
# ----------------------------------------------------- #
exit
