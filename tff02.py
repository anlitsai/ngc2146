#!/usr/bin/env python

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
yr=365*86400.0
Myr=1.0e6*yr
lyr=c*yr
pc=3.26*lyr
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
m_H=1.67e-24
ne1=100.0
ne2=1000.0
#E_ion_ev=13.6	# [eV]
#E_bnd_ev=4.52	# [eV]
#  --- parameter -------------------------------	#
X_CO2H2=1.4/3.0
H22mol=1.36
XH=X_CO2H2*H22mol
v_sound_kms=1.0e3
T_mol=30.0 # K (Tsai et al. 2009)
T_xotf=1.0e6 # K
print "============"
print "NGC 2146"
print "============"
print "parameters"
print "------------"
i_deg_n2146=70.0
i_pi_n2146=i_deg_n2146/180.0*math.pi
sin_i=math.sin(i_pi_n2146)
cos_i_n2146=math.cos(i_pi_n2146)
D_Mpc_n2146=17.2
v_motf_kms_n2146=200.0 # km/s (Tsai et al. 2009)
v_rot_kms_n2146=200.0 # km/s (Tsai et al. 2009)
R_mof_kpc_n2146=2.0
r_radius_kpc_n2146=3.3
M_SBR_msun_n2146=2.5e9
SFR_msunyr_n2146=20.1
M_mof_msun_n2146=3.4e8
t1_exp_yr_n2146=1.0e7
t2_exp_yr_n2146=2.0e7
print "============"
print "NGC 3628"
print "============"
print "parameters"
print "------------"
i_deg_n3628=89.0
i_pi_n3628=i_deg_n3628/180.0*math.pi
sin_i_n3628=math.sin(i_pi_n3628)
cos_i_n3628=math.cos(i_pi_n3628)
D_Mpc_n3628=7.7
v_motf_kms_n3628=90.0 # km/s (Tsai et al. 2009)
v_rot_kms_n3628=220.0 # km/s (Tsai et al. 2009)
R1_mof_kpc_n3628=0.37
R2_mof_kpc_n3628=0.56
r_radius_kpc_n3628=1.5
M_SBR_msun_n3628=2.0e8
SFR_msunyr_n3628=3.8
M_mof_msun_n3628=2.8e7
t1_exp_yr_n3628=3.3e6
t2_exp_yr_n3628=6.8e6
#  --------------------------------------------	#
def tff01(R_mof_kpc, r_radius_kpc, M_dyn_msun,type):
	R_mof=R_mof_kpc*kpc
	r_radius=r_radius_kpc*kpc
	M_dyn=M_dyn_msun*Msun
	t=math.sqrt((R_mof*r_radius**2)/(G*M_dyn))
	t_myr=t/Myr
	print '%.1e' %R_mof_kpc,"[kpc]",'%.1e' %r_radius_kpc,"[kpc]", '%.1e' %M_dyn_msun, "[Msun]", '%.1e' %t_myr, "[Myr]" ,type
#  --------------------------------------------	#
def tff(R_mof_kpc, r_radius_kpc, v_rot_kms,type):
	R_mof=R_mof_kpc*kpc
	r_radius=r_radius_kpc*kpc
	v_rot=v_rot_kms*1.0e5
	M_dyn=r_radius*v_rot**2/G
	M_dyn_msun=M_dyn/Msun
	t=math.sqrt(R_mof*r_radius/v_rot**2)
	t_myr=t/Myr
	print '%.1f' %R_mof_kpc,"[kpc]",'%.1f' %r_radius_kpc,"[kpc]", '%.1f' %v_rot_kms, "[km/s]",'%.1e' %M_dyn_msun, "[Msun]", '%.1f' %t_myr, "[Myr]" ,type
#	print '%.2f' %I_CO,"[Jy km/s as-2]", '%.1e' %S_CO,"[Jy km/s]",'%.0f' %n_as,"[as2]",'%.0f' %n_bm,"[beam]",'%.1e' %sd,"[g/cm2]",'%.0f' %sd_Msunpc2,"[Msun/pc2] (z =",'%.2f' %(z_gas_pc),"pc)",'%.1e' %M_gas_Msun,"[Msun]",type
	return t_myr
print "------------"
print "Free-fall timescale to the galactic disk"
print "------------"
tff(R_mof_kpc_n2146, r_radius_kpc_n2146, v_rot_kms_n2146,"n2146")
tff(10.0, r_radius_kpc_n2146, v_rot_kms_n2146,"n2146")
tff(R1_mof_kpc_n3628, r_radius_kpc_n3628, v_rot_kms_n3628,"n3628")
tff(R2_mof_kpc_n3628, r_radius_kpc_n3628, v_rot_kms_n3628,"n3628")
tff(10.0, r_radius_kpc_n3628, v_rot_kms_n3628,"n3628")
# ---------------------------------------------	#
print "------------"
print "Molecular gas consumption timescale in SBR"
print "------------"
def tcons(M_SBR_msun, M_mof_msun, t_exp_yr, sfr_msunyr,type):
	M_SBR=M_SBR_msun*Msun
	M_mof=M_mof_msun*Msun
	t_exp=t_exp_yr*Myr
	sfr=sfr_msunyr
	M_loss_msunyr=M_mof_msun/t_exp_yr
	t_cons_yr=M_SBR_msun/(sfr_msunyr+M_loss_msunyr)
	t_cons_myr=t_cons_yr/1.0e6
	t_prog=t_exp_yr/(t_exp_yr+t_cons_yr)*100
	print '%.1e' %M_SBR_msun,"[Msun]", '%.1f' %M_loss_msunyr,"[Msun/yr]",'%.1f' %sfr_msunyr,"[Msun/yr]",'%.1f' %t_cons_myr,"[Myr]",'%.1f' %t_prog,"[%]",type
	return t_cons_myr
tcons(M_SBR_msun_n2146, M_mof_msun_n2146, t1_exp_yr_n2146, SFR_msunyr_n2146,"n2146")
tcons(M_SBR_msun_n2146, M_mof_msun_n2146, t2_exp_yr_n2146, SFR_msunyr_n2146,"n2146")
tcons(M_SBR_msun_n3628, M_mof_msun_n3628, t1_exp_yr_n3628, SFR_msunyr_n3628,"n3628")
tcons(M_SBR_msun_n3628, M_mof_msun_n3628, t2_exp_yr_n3628, SFR_msunyr_n3628,"n3628")


def gg(M_dyn_msun, area_kpc2):
	M_dyn=M_dyn_msun*msun
	area=area_kpc2*kpc**2
	sigma=M_dyn/area
	gg=2*math.pi*G*sigma
	print  '%.1e' %sigma, "[g/cm2]",'%.1e' %gg, "[cm/s2]"

gg()

# ---------------------------------------------	#

# --- reference -------------------------------	#

exit

