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
E_SN=1.0e51	# [erg]
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
v_mof_kms_n2146=200.0 # km/s (Tsai et al. 2009)
v_rot_kms_n2146=220.0 # km/s (Tsai et al. 2009)
v_rot_HI_kms_n2146=250.0 # km/s (Taramopoulos et al. 2001)
r_rot_HI_kpc_n2146=15.0 # kpc (Taramopoulos et al. 2001)
r_radius_kpc_n2146=3.3
M_SBR_msun_n2146=2.5e9
SFR_msunyr_n2146=20.1
M_mof_msun_n2146=3.4e8
M_dyn_msun_n2146=3.9e10
M_dyn_n2146=M_dyn_msun_n2146*Msun
t1_exp_yr_n2146=1.0e7
t2_exp_yr_n2146=2.0e7
R2_mof_kpc_n2146=2.0
E_th_plm_n2146=0.9e55
E_1ostar=1.0e50	# (Vasquez et al. 2005, MNRAS, 362, 681, p1)
#E_1ostar=1.0e51	# (Knee & Wallace 2003, RevMexAA, 15, 44, p2)
E_ostar_n2146=3.3e5*E_1ostar
effi_ostar=0.15
g_n2146_2kpc=1.36e-7
N_ostar_n2146=3.3e5
E_kin_mof_n2146=3.0e55
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
v_mof_kms_n3628=90.0 # km/s (Tsai et al. 2009)
v_rot_kms_n3628=220.0 # km/s (Tsai et al. 2009)
v_rot_HI_kms_n3628=213.0 # km/s (Wilding et al. 1993)
#v_rot_HI_kms_n3628=300.0 # km/s (Wilding et al. 1993)
r_rot_HI_kpc_n3628=270*37.33/1000 # kpc (Wilding et al. 1993)
#r_rot_HI_kpc_n3628=15 # kpc (Wilding et al. 1993)
R1_mof_kpc_n3628=0.37
R2_mof_kpc_n3628=0.56
r_radius_kpc_n3628=1.5
M_SBR_msun_n3628=2.0e8
SFR_msunyr_n3628=3.8
M_mof_msun_n3628=2.8e7
M_dyn_msun_n3628=2.0e10
M_dyn_n3628=M_dyn_msun_n3628*Msun
t1_exp_yr_n3628=3.3e6
t2_exp_yr_n3628=6.8e6
E_th_plm_n3628=1.5e53
E_ostar_n3628=4.5e4*E_1ostar
g_n3628_500pc=1.12e-6
N_ostar_n3628=4.5e4
E_kin_mof_n3628=2.3e54
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
def poten1(z_kpc, radius_kpc,v_rot_kms,type):
	v_rot=v_rot_kms*1.0e5
	r=radius_kpc*kpc
	z=z_kpc*kpc
	Phi=2*math.pi*v_rot**2/r*(z-math.sqrt(z**2+r**2))
	v2=0.5*v_rot**2
	print "grav. potential =", '%2e' %Phi, "[cm^2/s^2] |", type
	print "    1/2*v_rot^2 =", '%2e' %v2, "[cm^2/s^2]"
print "---------------------------"
poten1_z_1pc=poten1(0.001,15.0,250,"z = 1pc")
poten1_z_10pc=poten1(0.01,15.0,250,"z = 10pc")
poten1_z_100pc=poten1(0.1,15.0,250,"z = 100pc")
poten1_z_500pc=poten1(0.5,15.0,250,"z = 500pc")
poten1_z_1kpc=poten1(1.0,15.0,250,"z = 1kpc")
poten1_z_2kpc=poten1(2.0,15.0,250,"z = 2kpc")
print "---------------------------"

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

# ---------------------------------------------	#
def tff_int(M_msun,r1_kpc,v1_kms, type):
	r1=r1_kpc*kpc
#	r_max=G*M/(-0.5*v1**2+G*M/r1)
	M=M_msun*Msun
	v1=v1_kms*1.0e5
	r_max=1/(v1**2/(-2*G*M)+1/r1)
	r_max_kpc=r_max/kpc
	v_max=math.sqrt(abs(v1**2-2*G*M/r1))
	v_max=math.sqrt(2*G*M/r_max)
	v_max_kms=v_max/1.0e5
	a=2*G*M/r1+v1**2
	b=-2*G*M
	t1=(math.sqrt(a+b/r1)*r1)/a-(b*math.log(b+2*a*r1+2*math.sqrt(a)*math.sqrt(a+b/r1)*r1))/(2*a**1.5)
	t_top=(math.sqrt(a+b/r_max)*r_max)/a-(b*math.log(b+2*a*r_max+2*math.sqrt(a*(a+b/r_max))*r_max))/(2*a**1.5)
	t1_myr=t1/Myr
	t_top_myr=t_top/Myr
	t_myr=t_top_myr-t1_myr
#	print '%.2f' %t1_myr, "[Myr]", '%.2f' %t_top_myr, "[Myr]",  '%.2f' %t_myr, "[Myr]", type
	print type, "r_now =",'%.2f' %r1_kpc, "[kpc] | r_max",'%.2f' %r_max_kpc, "[kpc] | v_max =",  '%.2f' %v_max_kms,"[km/s]"
	print "    t_now =", '%.2f' %t1_myr, "[Myr] | t_top =", '%.2f' %t_top_myr, "[Myr] | del_t =",  '%.2f' %t_myr, "[Myr]"
#'%.2f' %t_top_myr, "[Myr]",  type
	return t_top_myr

print "---------------------------"
tff_int(M_dyn_msun_n2146,R2_mof_kpc_n2146,v_mof_kms_n2146, "ngc2146 |")
tff_int(M_dyn_msun_n3628,R1_mof_kpc_n3628,v_mof_kms_n3628, "ngc3628 |")
tff_int(M_dyn_msun_n3628,R2_mof_kpc_n3628,v_mof_kms_n3628, "ngc3628 |")
print "---------------------------"
KE=0.5*200.0e5**2
PE=-G*M_dyn_n2146/(2.0*kpc)
E=KE+PE
print '%.3e' %KE,'%.3e' %PE,'%.3e' %E
print "---------------------------"

# ---------------------------------------------	#
def tff_max(M_dyn_msun,M_of_msun,E_kin_mof,E_th_plm,N_ostar,effi_ostar,d1_kpc,v1_kms, v_rot_kms,r_rot_kpc, type):
	d1=d1_kpc*kpc
#	d_max=G*M/(-0.5*v1**2+G*M/r1)
	M_dyn=M_dyn_msun*Msun
	M_of=M_of_msun*Msun
	v_now=v1_kms*1.0e5
	d_now=d1_kpc*kpc
	E_ostar=N_ostar*E_SN
	E_kin_o=E_ostar*effi_ostar
	GMMof_r=(G*M_dyn*M_of)/d_now
	d_max=1/((1/d_now)-(E_kin_mof+E_th_plm+E_kin_o)/(G*M_dyn*M_of))
#	d_max=1/((1/d_now)-(0.5*M_of*v_now**2+(E_th_plm+E_kin_o))/(G*M_dyn*M_of))
	d_max_kpc=d_max/kpc
#	g_d_now=G*M_dyn/d_now**2
#	g_d_max=G*M_dyn/d_max**2
#	g_r=0.5*(g_d_now+g_d_max)
	v_rot=v_rot_kms*1.0e5
	r_rot=r_rot_kpc*kpc
	g_r=2*v_rot**2/r_rot
	v_go=math.sqrt(v_now**2+2*(E_th_plm+E_kin_o)/M_of)
#	v_max=math.sqrt(abs(v_go**2+2*(E_th_plm+E_kin_o)/M_of-2*G*M_dyn/d_now))
#	v_max=math.sqrt(2*G*M_dyn/d_max)
#	v_max_kms=v_max/1.0e5
#	a=2*G*M_dyn/r1+v1**2
#	b=-2*G*M_dyn
	t_top=v_go/g_r
	t_top_myr=t_top/Myr
	t_return=v_go/g_r+math.sqrt((v_go/g_r)**2+2*d_max/g_r)
	t_return_=v_go/g_r+math.sqrt((v_go/g_r)**2-2*d_max/g_r)
	t_return_myr=t_return/Myr
	t_return_myr_=t_return_/Myr
#	t_down=
	r_max=-v_go*t_top+0.5*g_r*t_top**2
	r_max_kpc=r_max/kpc
#	print '%.2f' %t1_myr, "[Myr]", '%.2f' %t_top_myr, "[Myr]",  '%.2f' %t_myr, "[Myr]", type
	print type, "d_max",'%.2f' %d_max_kpc, "[kpc] | t_top =", '%.2f' %t_top_myr, "[Myr] | g =", '%.2e' %g_r, "[cm s-2]"
	print "     E_kin_mof =", '%.2e' %E_kin_mof, "[erg]"
	print "     E_th_plm =", '%.2e' %E_th_plm, "[erg]"
	print "     E_kin_o =", '%.2e' %E_kin_o, "[erg]"
	print "     GMMof/r =", '%.2e' %GMMof_r, "[erg]"
	print "     g =", '%.2e' %g_r, "[cm/s^2]"
#	print "     g =", '%.2e' %g_r, "(",'%.2e' %g_d_now, "--", '%.2e' %g_d_max,")"
	print "     v_now =", '%.2f' %(v_now/1.0e5), "[km/s] | v_go =",'%.2f' %(v_go/1.0e5), "[km/s]"
	print "     t_return =", '%.2f' %t_return_myr, "[Myr]"
	print "     t_return_ =", '%.2f' %t_return_myr_, "[Myr]"
	print "     r_max =", '%.2f' %r_max_kpc, "[kpc]"
	return t_top_myr

print "---------------------------"
tff_max(M_dyn_msun_n2146,M_mof_msun_n2146,E_kin_mof_n2146,E_th_plm_n2146,N_ostar_n2146,effi_ostar,R2_mof_kpc_n2146,v_mof_kms_n2146,v_rot_HI_kms_n2146,r_rot_HI_kpc_n2146, "ngc2146 (M) |")
tff_max(M_dyn_msun_n2146,M_mof_msun_n2146,E_kin_mof_n2146,1.3e55,N_ostar_n2146,0.2,R2_mof_kpc_n2146,v_mof_kms_n2146,v_rot_HI_kms_n2146,r_rot_HI_kpc_n2146, "ngc2146 (U) |")
tff_max(M_dyn_msun_n2146,M_mof_msun_n2146,E_kin_mof_n2146,0.4e55,N_ostar_n2146,0.1,R2_mof_kpc_n2146,v_mof_kms_n2146,v_rot_HI_kms_n2146,r_rot_HI_kpc_n2146, "ngc2146 (L) |")
print "---------------------------"
tff_max(M_dyn_msun_n3628,M_mof_msun_n3628,E_kin_mof_n3628,E_th_plm_n3628,N_ostar_n3628,effi_ostar,R2_mof_kpc_n3628,v_mof_kms_n3628, v_rot_HI_kms_n3628,r_rot_HI_kpc_n3628,"ngc3628 (M) |")
tff_max(M_dyn_msun_n3628,M_mof_msun_n3628,2.8e54,2.3e53,N_ostar_n3628,0.2,R2_mof_kpc_n3628,v_mof_kms_n3628, v_rot_HI_kms_n3628,r_rot_HI_kpc_n3628,"ngc3628 (U) |")
tff_max(M_dyn_msun_n3628,M_mof_msun_n3628,1.8e54,0.7e53,N_ostar_n3628,0.1,R2_mof_kpc_n3628,v_mof_kms_n3628, v_rot_HI_kms_n3628,r_rot_HI_kpc_n3628,"ngc3628 (L) |")
print "---------------------------"
#  --------------------------------------------	#
def t_max_poten(z_kpc, radius_kpc,v_rot_kms,type):
	v_rot=v_rot_kms*1.0e5
	r=radius_kpc*kpc
	z=z_kpc*kpc
	Phi=2*math.pi*v_rot**2/r*(z-math.sqrt(z**2+r**2))
	v2=0.5*v_rot**2
	print "grav. potential =", '%2e' %Phi, "[cm^2/s^2] |", type
	print "    1/2*v_rot^2 =", '%2e' %v2, "[cm^2/s^2]"
print "---------------------------"
t_max_poten(2.0,15.0,250,"z = 2kpc")
print "---------------------------"

#  --------------------------------------------	#

# --- reference -------------------------------	#
# ngc3628: http://articles.adsabs.harvard.edu//full/1993MNRAS.263.1075W/0001084.000.html
# ngc2146: http://www.aanda.org/index.php?option=com_article&access=standard&Itemid=129&url=/articles/aa/full/2001/03/aah2217/aah2217.html


exit

