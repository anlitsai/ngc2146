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
E_1ostar=1.0e50	# (Vasquez et al. 2005, MNRAS, 362, 681, p1)
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
SFR_msunyr_n2146=23.0
M_mof_msun_n2146=3.4e8
M_sb1_msun_n2146=2.6e8
M_sb2_msun_n2146=3.7e7
M_dyn_msun_n2146=3.9e10
M_dyn_n2146=M_dyn_msun_n2146*Msun
t1_exp_yr_n2146=1.0e7
t2_exp_yr_n2146=2.0e7
z2_mof_kpc_n2146=2.0
E_th_plm_n2146=0.9e55
#E_1ostar=1.0e51	# (Knee & Wallace 2003, RevMexAA, 15, 44, p2)
E_ostar_n2146=3.3e5*E_1ostar
effi_ostar=0.3
g_n2146_2kpc=1.36e-7
N_ostar_n2146=3.3e5
E_kin_mof_n2146=3.0e55
E_kin_sb1_n2146=6.7e54
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
z1_mof_kpc_n3628=0.37
z2_mof_kpc_n3628=0.45
z_mof_kpc_n3628=(0.45+0.37)/2
r_radius_kpc_n3628=1.5
M_SBR_msun_n3628=2.0e8
SFR_msunyr_n3628=3.1
M_mof_msun_n3628=2.8e7
M_dyn_msun_n3628=2.0e10
M_dyn_n3628=M_dyn_msun_n3628*Msun
t1_exp_yr_n3628=3.9e6
t2_exp_yr_n3628=5.2e6
E_th_plm_n3628=1.5e53
E_ostar_n3628=4.5e4*E_1ostar
g_n3628_500pc=1.12e-6
N_ostar_n3628=4.5e4
E_kin_mof_n3628=2.3e54
print "============"
print "M82"
print "============"
print "parameters"
print "------------"
M_mdsk_msun_m82=1.3e9   # (Walter et al. 2002)
M_mof_msun_m82=3.3e8    # (Walter et al. 2002)
#M_dyn_msun_m82=1.1e11 	# (Sofue 1998 PASJ)
M_dyn_msun_m82=7.0e9	# (Young et al. 1984, ApJ)
M_SBR_msun_m82=2.3e8    # (Walter et al. 2002; Weiss et al. 2001)
SFR_msunyr_m82=6.0
M_dyn_m82=M_dyn_msun_m82*Msun
t_exp_yr_m82=1.0e7      # (Walter et al. 2002)
z_mof_kpc_m82=1.0       # (Walter et al. 2002)
E_kin_mof_m82=3.3e55	# (Walter et al. 2002)
E_th_plm_m82=8.0e54*0.03**0.5    # (Lehnert et al. 1999)
E1_th_plm_m82=0.8e54    # (Lehnert et al. 1999)
E2_th_plm_m82=2.5e54    # (Lehnert et al. 1999)
N_ostar_m82_interf=1.26e5      # re-measured from satoki 2005 data; (Matsushita et al. 2005)
#N_ostar_m82_single=1.59e5      # (Jura et al. 1978)
N_ostar_m82_single=1.52e5      # (Carlstrom et al 1991)
v1_mof_kms_m82=50	# (Walter et al.2002)
v2_mof_kms_m82=100	# (Walter et al.2002)
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
#	v2=0.5*v_rot**2
	print "grav. potential =", '%2e' %Phi, "[cm^2/s^2] |", type
#	print "    1/2*v_rot^2 =", '%2e' %v2, "[cm^2/s^2]"
print "---------------------------"
poten1_z_1pc=poten1(0.001,15.0,250,"z = 1pc")
print "   GM/(r=1pc) =", '%2e' %(-G*2.0e10*Msun/pc), "[cm^2/s^2]"
print
poten1_z_10pc=poten1(0.01,15.0,250,"z = 10pc")
print "   GM/(r=10pc) =", '%2e' %(-G*2.0e10*Msun/10/pc), "[cm^2/s^2]"
print
poten1_z_100pc=poten1(0.1,15.0,250,"z = 100pc")
print "   GM/(r=100pc) =", '%2e' %(-G*2.0e10*Msun/0.1/kpc), "[cm^2/s^2]"
print
poten1_z_500pc=poten1(0.5,15.0,250,"z = 500pc")
print "   GM/(r=500pc) =", '%2e' %(-G*2.0e10*Msun/0.5/kpc), "[cm^2/s^2]"
print
poten1_z_1kpc=poten1(1.0,15.0,250,"z = 1kpc")
print "   GM/(r=1kpc)  =", '%2e' %(-G*2.0e10*Msun/kpc), "[cm^2/s^2]"
print
poten1_z_2kpc=poten1(2.0,15.0,250,"z = 2kpc")
print "   GM/(r=2kpc)  =", '%2e' %(-G*2.0e10*Msun/2/kpc), "[cm^2/s^2]"
print
print "    1/2*(v=100 km/s)^2 = ", '%2e' %(0.5*100.0e5**2), "[cm^2/s^2]"
print "    1/2*(v=200 km/s)^2 = ", '%2e' %(0.5*200.0e5**2), "[cm^2/s^2]"
print "    1/2*(v=300 km/s)^2 = ", '%2e' %(0.5*300.0e5**2), "[cm^2/s^2]"
#  --------------------------------------------	#
def poten2(M_dyn_msun, z_kpc,type):
	M=M_dyn_msun*Msun
	z=z_kpc*kpc
	Phi=-G*M/(math.sqrt(2)*z)
	v_esc=math.sqrt(math.sqrt(2)*G*M/z)
	v_esc_kms=v_esc/1.0e5
	print "grav. potential =", '%2e' %Phi, "[cm^2/s^2] | v_esc =", '%.0f' %v_esc_kms,"[km/s]", type
	return v_esc
print "---------------------------"
poten2_n2146=poten2(M_dyn_msun_n2146,z2_mof_kpc_n2146,"N2146")
poten2_n3628=poten2(M_dyn_msun_n3628,z1_mof_kpc_n3628,"N3628")
poten2_n3628=poten2(M_dyn_msun_n3628,z2_mof_kpc_n3628,"N3628")
print "---------------------------"

#def v_esc(M_dyn_msun,z_kpc,type):
#	M=M_dyn_msun*Msun
#	z=z_kpc*kpc
#	v=math.sqrt(2*G*M/z)
#	v_kms=v/1.0e5
#	print "v_esc (z=",z_kpc,"kpc)=", '%.0f' %v_kms, "[km/s] |", type
#	return
#print "---------------------------"
#v_esc_n2146=v_esc(M_dyn_msun_n2146,z2_mof_kpc_n2146,"N2146")
#v_esc1_n3628=v_esc(M_dyn_msun_n3628,z1_mof_kpc_n3628,"N3628")
#v_esc2_n3628=v_esc(M_dyn_msun_n3628,z2_mof_kpc_n3628,"N3628")
#print "---------------------------"

#  --------------------------------------------	#
def tff1(n_cm3,type):
	rho=n_cm3*m_p
	t=math.sqrt(3*math.pi/(G*rho))
	t_myr=t/Myr
	print "free-fall timescale =", '%.1f' %t_myr, "[Myr]", type
	return t_myr
print "---------------------------"
tff_100=tff1(ne1,"| mol.cloud n_e=100 cm^-3")
tff_300=tff1(300,"| mol.cloud n_e=300 cm^-3")
tff_1000=tff1(ne2,"| mol.cloud n_e=1000 cm^-3")
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
tff_int(M_dyn_msun_n2146,z2_mof_kpc_n2146,v_mof_kms_n2146, "ngc2146 |")
tff_int(M_dyn_msun_n3628,z1_mof_kpc_n3628,v_mof_kms_n3628, "ngc3628 |")
tff_int(M_dyn_msun_n3628,z2_mof_kpc_n3628,v_mof_kms_n3628, "ngc3628 |")
print "---------------------------"
KE=0.5*200.0e5**2
PE=-G*M_dyn_n2146/(2.0*kpc)
E=KE+PE
print '%.3e' %KE,'%.3e' %PE,'%.3e' %E
print "---------------------------"


# ---------------------------------------------	#
#def tff_max(M_dyn_msun,M_of_msun,E_kin_mof,E_th_plm,N_ostar,effi_ostar,z1_kpc,v1_kms, v_rot_kms,r_rot_kpc, type):
def tff_max(M_dyn_msun,M_of_msun,E_kin_mof,E_th_plm,N_ostar,effi_ostar,z1_kpc, type):
	M_dyn=M_dyn_msun*Msun
	GM=G*M_dyn
	M_of=M_of_msun*Msun
#	v_now=v1_kms*1.0e5
	z_now=z1_kpc*kpc
	E_ostar=N_ostar*E_SN
	E_kin_o=E_ostar*effi_ostar
	GMMof_r=-GM*M_of/z_now
#	v_rot=v_rot_kms*1.0e5
#	r_rot=r_rot_kpc*kpc
	E_input=E_th_plm+E_kin_o
	v_go=math.sqrt(2*(E_kin_mof+E_input)/(M_of*0.8))
	v_go_kms=v_go/1.0e5
	v_go2=0.5*v_go**2
	Phi1=-GM/z_now
	Phi2=Phi1+0.5*v_go**2
	v_esc=math.sqrt(2*abs(Phi1))
	v_esc_kms=v_esc/1.0e5
	Phi1_Kuzmin=-GM/(math.sqrt(2)*z_now)	# Binney & Tremaine 2008 Galactic Dynamics, p73
	v_esc_Kuzmin=math.sqrt(2*abs(Phi1_Kuzmin))
	v_esc_kms_Kuzmin=v_esc_Kuzmin/1.0e5
	Phi2_Kuzmin=Phi1_Kuzmin+v_go2
	z_max_Kuzmin=-GM/(math.sqrt(2)*Phi2_Kuzmin)
	z_max_kpc_Kuzmin=z_max_Kuzmin/kpc

	z_max=z_max_Kuzmin
	gm21=1/math.sqrt(math.sqrt(2)*GM)
	z=z_now
	dz=z_max-z
	t_znow=gm21*((dz/math.sqrt(1/z-1/z_max))+(z_max*math.sqrt(dz)*math.atan(math.sqrt(z*dz)/(-dz))/math.sqrt(1-z/z_max)))
	z=z_max-0.01*pc
	dz=z_max-z
	t_zmax=gm21*((dz/math.sqrt(1/z-1/z_max))+(z_max*math.sqrt(dz)*math.atan(math.sqrt(z*dz)/(-dz))/math.sqrt(1-z/z_max)))
	z=pc
	dz=z_max-z
	t_z0=gm21*((dz/math.sqrt(1/z-1/z_max))+(z_max*math.sqrt(dz)*math.atan(math.sqrt(z*dz)/(-dz))/math.sqrt(1-z/z_max)))
	t1=t_znow-t_zmax
	t2=t_z0-t_zmax
	t1_myr=t1/Myr
	t2_myr=t2/Myr
	t3_myr=t_z0/Myr
	t12_myr=t1_myr+t2_myr
	print "     E_kin_mof =", '%.2e' %E_kin_mof, "[erg]"
	print "     E_th_plm =", '%.2e' %E_th_plm, "[erg]"
	print "     E_kin_o =", '%.2e' %E_kin_o, "[erg]"
	print "     E_input =", '%.2e' %E_input, "[erg]"
	print "     GMMof/r =", '%.2e' %GMMof_r, "[erg]"
	print "     v_go =",'%.2f' %v_go_kms, "[km/s] <======"
	print "     eff_ostar =",'%.2f' %effi_ostar
#	print "     v_now =", '%.2f' %v1_kms, "[km/s] | v_go =",'%.2f' %v_go_kms, "[km/s] <======"
	print "     Phi1 =", '%.2e' %Phi1, "[cm^2/s^2]"
	print "     1/2*v_go^2 =", '%.2e' %v_go2, "[cm^2/s^2]"
	print "     Phi2 =", '%.2e' %Phi2, "[cm^2/s^2]"
	print "     Phi_Kuzmin =", '%.2e' %Phi1_Kuzmin, "[cm^2/s^2]"
	print "     v_esc_Kuzmin =", '%.2f' %v_esc_kms_Kuzmin, "[km/s] <======"
	print "     z_now =", '%.1f' %z1_kpc, "[kpc] =",'%.2e' %z_now, "[cm] <======"
	print "     z_max_Kuzmin =", '%.2f' %z_max_kpc_Kuzmin, "[kpc] =",'%.2e' %z_max_Kuzmin, "[cm] <==="
	print "     t1(z1) =", '%.2f' %t1_myr, "[Myr] |  t2(1pc) =", '%.2f' %t2_myr, "[Myr]  |  t_total =", '%.2f' %t12_myr, "[Myr] <==="
#	print "     t3 =", '%.2f' %t3_myr, "[Myr]"
	print "---------------------------"
	return t12_myr

print "--- N2146 ------------------------"
tff_n2146_myr=tff_max(M_dyn_msun_n2146,M_mof_msun_n2146,E_kin_mof_n2146,E_th_plm_n2146,N_ostar_n2146,effi_ostar,z2_mof_kpc_n2146, "ngc2146 OF (M) |")
tff_max(M_dyn_msun_n2146,M_mof_msun_n2146,E_kin_mof_n2146,1.3e55,N_ostar_n2146,effi_ostar+0.05,z2_mof_kpc_n2146, "ngc2146 OF (U) |")
tff_max(M_dyn_msun_n2146,M_mof_msun_n2146,E_kin_mof_n2146,0.4e55,N_ostar_n2146,effi_ostar-0.050,z2_mof_kpc_n2146, "ngc2146 OF (L) |")
#print "---------------------------"
#tff_max(M_dyn_msun_n2146,M_sb1_msun_n2146,E_kin_sb1_n2146,0.4e55,N_ostar_n2146,effi_ostar-0.050,z2_mof_kpc_n2146, "ngc2146 OF (L) |")
print "---------------------------"
print "--- N3628 ------------------------"
tff_n3628_myr=tff_max(M_dyn_msun_n3628,M_mof_msun_n3628,E_kin_mof_n3628,E_th_plm_n3628,N_ostar_n3628,effi_ostar,z_mof_kpc_n3628,"ngc3628 OF (M) |")
tff_max(M_dyn_msun_n3628,M_mof_msun_n3628,2.8e54,2.3e53,N_ostar_n3628,effi_ostar+0.05,z_mof_kpc_n3628,"ngc3628 (U) |")
tff_max(M_dyn_msun_n3628,M_mof_msun_n3628,1.8e54,0.7e53,N_ostar_n3628,effi_ostar-0.05,z_mof_kpc_n3628, "ngc3628 (L) |")
print "--- M82 inteferometer ------------------------"
tff_m82_myr=tff_max(M_dyn_msun_m82,M_mof_msun_m82,E_kin_mof_m82,E_th_plm_m82,N_ostar_m82_interf,effi_ostar,z_mof_kpc_m82,"ngc3628 OF (M) |")
tff_m82_myr=tff_max(M_dyn_msun_m82,M_mof_msun_m82,E_kin_mof_m82,E2_th_plm_m82,N_ostar_m82_interf,effi_ostar,z_mof_kpc_m82,"ngc3628 OF (U) |")
tff_m82_myr=tff_max(M_dyn_msun_m82,M_mof_msun_m82,E_kin_mof_m82,E1_th_plm_m82,N_ostar_m82_interf,effi_ostar,z_mof_kpc_m82,"ngc3628 OF (L) |")
print "--- M82 single dish ------------------------"
tff_m82_myr=tff_max(M_dyn_msun_m82,M_mof_msun_m82,E_kin_mof_m82,E_th_plm_m82,N_ostar_m82_single,effi_ostar,z_mof_kpc_m82,"ngc3628 OF (M) |")
tff_m82_myr=tff_max(M_dyn_msun_m82,M_mof_msun_m82,E_kin_mof_m82,E2_th_plm_m82,N_ostar_m82_single,effi_ostar,z_mof_kpc_m82,"ngc3628 OF (U) |")
tff_m82_myr=tff_max(M_dyn_msun_m82,M_mof_msun_m82,E_kin_mof_m82,E1_th_plm_m82,N_ostar_m82_single,effi_ostar,z_mof_kpc_m82,"ngc3628 OF (L) |")
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

# ---------------------------------------------	#
def tff_z(E_kin_mof,E_th_plm,N_ostar,effi_ostar,M_mof_msun,M_dyn_msun,z_kpc,z0_kpc):
	E_ostar=N_ostar*E_SN
	E_kin_o=E_ostar*effi_ostar
	M_mof=M_mof_msun*Msun
	v_E=math.sqrt(2*(E_kin_mof+E_th_plm+E_kin_o)/M_mof)
#	v_go_kms=v_go/1.0e5
#	v_E=v_E_kms*1.0e5
	M_dyn=M_dyn_msun*Msun
	z=z_kpc*kpc
	z0=z0_kpc*kpc
	g=G*M_dyn/(math.sqrt(2)*z**2)
	g0=G*M_dyn/(math.sqrt(2)*z0**2)
	g_1pc=G*M_dyn/(math.sqrt(2)*pc**2)
	print (v_E/g)**2, (z-z0)/g
	print g, g0,'%.2e' %g_1pc
	t1=v_E/g-math.sqrt((v_E/g)**2-2*(z-z0)/g)
	t2=v_E/g+math.sqrt((v_E/g)**2-2*(z-z0)/g)
	t1_myr=t1/Myr
	t2_myr=t2/Myr
	print "z =", '%.1f' %z0_kpc, "to", '%.1f' %z_kpc, "[kpc] | t =", '%.1f' %t1_myr, "or", '%.1f' %t2_myr, "[Myr]"
print "--- N2146 ------------------------"
tff_z(E_kin_mof_n2146,E_th_plm_n2146,N_ostar_n2146,effi_ostar,M_mof_msun_n2146,M_dyn_msun_n2146,4,2)
print "g is not constant, this result is not correct"
print "---------------------------"
# --------------------------------------------- #
def t_cons(M_SBR_msun,dM_flow_msun_yr,t_return_myr,tff_myr,SFR_msun_yr,type):
	M_sbr=M_SBR_msun*Msun
	dM=dM_flow_msun_yr*Msun/yr
	t_r2=(t_return_myr+tff_myr)*Myr
#	t_return=t_return_myr*Myr
	SFR=SFR_msun_yr*Msun/yr
	t_cons=(M_sbr-dM*t_r2)/SFR
	t_cons_myr=t_cons/Myr
	print "t_cons =", '%2f' %t_cons_myr, "[Myr]", type
	return t_cons_myr
print "--- consumption timescale ------------------------"
print "--- N2146 ------------------------"
t_cons(M_SBR_msun_n2146,17.0,tff_n2146_myr,tff_100,SFR_msunyr_n2146,"| N2146")
t_cons(M_SBR_msun_n2146,17.0,tff_n2146_myr,tff_1000,SFR_msunyr_n2146,"| N2146")
t_cons(M_SBR_msun_n2146,34.0,tff_n2146_myr,tff_100,SFR_msunyr_n2146,"| N2146")
t_cons(M_SBR_msun_n2146,34.0,tff_n2146_myr,tff_1000,SFR_msunyr_n2146,"| N2146")
print "--- N3628 ------------------------"
t_cons(M_SBR_msun_n2146,4.4,tff_n3628_myr,tff_100,SFR_msunyr_n3628,"| N3628")
t_cons(M_SBR_msun_n2146,7.2,tff_n3628_myr,tff_100,SFR_msunyr_n3628,"| N3628")
print "---------------------------"

#  --------------------------------------------	#
def t_cons2(M_SBR_msun,dM_flow_msun_yr,SFR_msun_yr,type):
	M_sbr=M_SBR_msun*Msun
	dM=dM_flow_msun_yr*Msun/yr
	SFR=SFR_msun_yr*Msun/yr
	t_cons=M_sbr/(dM+SFR)
	t_cons_myr=t_cons/Myr
	print "t_cons =", '%.2f' %t_cons_myr, "[Myr]", type
	return t_cons_myr
print "--- N2146 ------------------------"
t1_cons_n2146=t_cons2(M_SBR_msun_n2146,27.0,SFR_msunyr_n2146,"| N2146")
t2_cons_n2146=t_cons2(M_SBR_msun_n2146,58.0,SFR_msunyr_n2146,"| N2146")
print "--- N3628 ------------------------"
t1_cons_n3628=t_cons2(M_SBR_msun_n2146,4.4,SFR_msunyr_n3628,"| N3628")
t2_cons_n3628=t_cons2(M_SBR_msun_n2146,7.2,SFR_msunyr_n3628,"| N3628")

print "--- consumption timescale ------------------------"
print "--- consumption timescale ------------------------"
print "--- consumption timescale ------------------------"
def t_cons_back(M_SBR_msun,dM_msun_yr,SFR_msun_yr,t_back_myr,t_exp_myr, type):
	M_sbr=M_SBR_msun*Msun
	dM=dM_msun_yr*Msun/yr
	t_back=t_back_myr*Myr
	t_exp=t_exp_myr*Myr
	SFR=SFR_msun_yr*Msun/yr
	t_cons=(M_sbr-dM*t_back)/SFR
	t_cons_myr=t_cons/Myr
	t_prog=t_exp_myr/(t_exp_myr+t_cons_myr)
	print "t_cons =", '%.2f' %t_cons_myr, "[Myr] | t_pro =", '%.2f' %t_prog, "%", type
	return t_cons_myr
print "--- N2146 ------------------------"
t_cons_back_n2146=t_cons_back(M_SBR_msun_n2146,25.5,SFR_msunyr_n2146,tff_n2146_myr,20.0,"| N2146")
t_cons_back_n3628=t_cons_back(M_SBR_msun_n3628,5.8,SFR_msunyr_n3628,tff_n3628_myr,4.55,"| N3628")
t_cons_back_m82=t_cons_back(M_SBR_msun_m82,33.0,SFR_msunyr_m82,tff_m82_myr,50.0,"| M82")
	
print "--- N3628 ------------------------"

print "--- M82 ------------------------"


print "---------------------------"
def t_prog(t_exp_myr,t_cons_myr,type):
	t_prog=t_exp_myr/(t_exp_myr+t_cons_myr)*100
	print "progres =", '%.1f' %t_prog, "%", type
	return t_prog
print "--- N2146 ------------------------"
t_prog(20.0,t1_cons_n2146,"N2146")
t_prog(20.0,t2_cons_n2146,"N2146")
print "--- N3628 ------------------------"
t_prog(3.3,t1_cons_n3628,"N3628")
t_prog(6.8,t1_cons_n3628,"N3628")
t_prog(3.3,t2_cons_n3628,"N3628")
t_prog(6.8,t2_cons_n3628,"N3628")

#  --------------------------------------------	#

# --- reference -------------------------------	#
# ngc3628: http://articles.adsabs.harvard.edu//full/1993MNRAS.263.1075W/0001084.000.html
# ngc2146: http://www.aanda.org/index.php?option=com_article&access=standard&Itemid=129&url=/articles/aa/full/2001/03/aah2217/aah2217.html


exit

