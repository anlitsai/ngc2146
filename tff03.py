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
def gg1(M_dyn_msun,r_radius_kpc,type):
	M_dyn=M_dyn_msun*Msun
	r_radius=r_radius_kpc*kpc
	Sigma=M_dyn/(math.pi*r_radius**2)
	gg=2*math.pi*G*Sigma
	print '%.1e' %M_dyn_msun, "[Msun]", '%.1f' %r_radius_kpc,"[kpc]", '%.1e' %gg, "[CGS]", type

g11=gg1(2.0e10, 1.5, "ngc3628 | 2.0e10 Msun, 1.5 kpc")
#  --------------------------------------------	#
def gg2(v_rot_kms,r_radius_kpc,type):
	v_rot=v_rot_kms*1.0e5
	r_radius=r_radius_kpc*kpc
	gg=2*v_rot**2/r_radius
	print '%.0f' %v_rot_kms, "[km/s]", '%.1f' %r_radius_kpc,"[kpc]", '%.1e' %gg, "[CGS]", type
	return gg

g2_3628=gg2(213.0, 10.0, "| ngc3628, g ")
g2_3628_1=gg2(300.0, 15.0, "| ngc3628, g ")
g2_2146=gg2(250.0, 15.0, "| ngc2146, g ")

#  --------------------------------------------	#
def tff2(v_mof_kms,gg,type):
	v_mof=v_mof_kms*1.0e5
	t=v_mof/gg
	t_myr=t/Myr
	print '%.0f' %v_mof_kms,"[km/s]",'%.1e' %gg,"[CGS]", '%.1f' %t_myr, "[Myr]", type
	return t

t2_3628=tff2(90.0, g2_3628, "| ngc3628, t2, t3")
t2_2146_of=tff2(200.0, g2_2146, "| ngc2146, t2, t3, of")
t2_2146_sb=tff2(50.0, g2_2146, "| ngc2146, t2, t3, sb")
#  --------------------------------------------	#
def tff4(S_mof_kpc, v_rot_kms, gg, type):
	S_mof=S_mof_kpc*kpc
	v_rot=v_rot_kms*1.0e5
	t=0.5*(-2*v_rot/gg+math.sqrt(4*v_rot**2/gg**2+8*S_mof/gg))
	t_myr=t/Myr
	print '%.1e' %S_mof_kpc,"[kpc]", '%.1e' %v_rot_kms,"[km/s]",'%.1e' %gg,"[CGS]", '%.1f' %t_myr, "[Myr]", type
	return t
	
t4_3628=tff4(0.5, 90.0, g2_3628, "| ngc3628, t4")
t4_2146_of=tff4(2.0, 200.0, g2_2146, "| ngc2146, t4, of")
t4_2146_sb=tff4(0.5, 50.0, g2_2146, "| ngc2146, t4, sb")


# ---------------------------------------------	#
def tff234(t2, t4, type):
	t234=t2*2+t4
	t234_myr=t234/Myr
	print '%.1f' %t234_myr, "[Myr]", type
	return t234

t234_3628=tff234(t2_3628,t4_3628, "| ngc3628, t234, of")
t234_2146_of=tff234(t2_2146_of,t4_2146_of, "| ngc2146, t234, of")
t234_2146_sb=tff234(t2_2146_sb,t4_2146_sb, "| ngc2146, t234, sb")

# --- reference -------------------------------	#
# ngc3628: http://articles.adsabs.harvard.edu//full/1993MNRAS.263.1075W/0001084.000.html
# ngc2146: http://www.aanda.org/index.php?option=com_article&access=standard&Itemid=129&url=/articles/aa/full/2001/03/aah2217/aah2217.html


exit

