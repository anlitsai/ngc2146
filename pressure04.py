#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
pc_to_cm=3.26*3e10*365*86400
ev_to_erg=1.6e-12
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
c=3.0e10 # light speed
M_sun=1.99e33 # solar mass
L_sun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24
#  --- parameter -------------------------------	#
v_motf_kms=200.0 # km/s (Tsai et al. 2009)
v_motf_cms=v_motf_kms*1.0e5 # cm/s
T_mol=30.0 # K (Tsai et al. 2009)
T_xotf=1.0e6 # K
n_mol=100.0 # cm^-3 (Tsai et al. 2009)
EI=8.0e62 # cm^-3 (Inui et al. 2005)
R_xotf_pc=6.3*1000*4.8/3.5 # (Inui et al. 2005)
R_xotf_cm=R_xotf_pc*pc_to_cm
V_xotf_cm3=(4.0/3.0*math.pi)*R_xotf_cm**3 # (Inui et al. 2005)
V_xotf_cm3_Inui=(4.0/3.0*math.pi)*(6.3e3*pc_to_cm)**3 # (Inui et al. 2005)
print "------------"
print "parameters"
print "------------"
fill=0.01 # (Inui et al. 2005)
print "filling factor =", fill
n_xotf=(EI/V_xotf_cm3/fill)**(0.5) # cm^-3 (Iuni et al. 2005)
kT_xotf_erg=0.5e3*ev_to_erg
print "kT_xotf_erg =", kT_xotf_erg,"erg"
print "V_xotf_cm3 =", V_xotf_cm3
print "V_xotf_cm3 (Inui) =", V_xotf_cm3_Inui
M_xotf_g=n_xotf*m_p*V_xotf_cm3*fill
#print M_xotf_g,R_xotf_pc,R_xotf_cm,n_xotf,m_p,V_xotf_cm3
E_xotf_erg=1.0e56 # (Inui et al. 2005)
R_motf_cm=2.0e3*pc_to_cm # (Tsai et al. 2009)
SFR=10.0 # M_sun/yr (Greve et al. 2000)
SNRate= 0.15 # yr^-1 (Tarchi et al. 2000)
effi=0.001 # (Thompson et al. 2005)
as_to_pc=80.0
#I_CO_gal_pc2=1.8e3 # within 1.0e7 pc^2 (Tsai et al. 2009)
#I_CO_motf_pc2=150.0 # (Tsai et al. 2009)
#I_CO_msbl_pc2=115.0 # (Tsai et al. 2009)
M_msbl_Msun=2.6e8 # M_sun (Tsai et al. 2009)
M_motf_Msun=3.4e8 # M_sun (Tsai et al. 2009)
M_motf_g=M_motf_Msun*M_sun # (Tsai et al. 2009)
M_mttl_Msun=4.1e9 # M_sun (Tsai et al. 2009)
M_mdsk_Msun=M_mttl_Msun-M_motf_Msun-M_msbl_Msun
thick_pc=500.0	# (Greve 2000)
R_starburst_pc=700.0 # (@tau=1# Thompson et al. 2005)
R_starburst_pc=1000.0 # (our data)
R_starburst_pc=1250.0 # (Greve 2000)
V_starburst_pc3=1.0e10 # (Greve 2000)
tau=10.0
d_mpc=17.2	# Mpc
# --- gravitational pressure (Gunn & Gott 1972) -------	#
Msun_to_Ico=1.4/2.0*d_mpc**2*1.18e4
I_CO_mdsk_as2=M_mdsk_Msun/Msun_to_Ico	# Jy km/s arcsec^-2 (from my data)
I_CO_motf_as2=M_motf_Msun/Msun_to_Ico	# Jy km/s arcsec^-2 (from my data)
# I_CO_mdsk_as2=I_CO_mdsk_pc2/(1.0e7/as_to_pc**2)
# surf_den_mol[M_sun/pc^2]=6.5e2*I(CO)[Jy km/s as^(-2)] # (Sakamoto et al. 1995)
# surf_den_mol[M_g/cm^2]=surf_den_mol[M_sun/pc^2]*Msun_pc2_to_cgs
Msun_pc2_to_cgs=M_sun/pc_to_cm**2
surf_den_mdsk=6.5e2*I_CO_mdsk_as2*Msun_pc2_to_cgs
surf_den_motf=6.5e2*I_CO_motf_as2*Msun_pc2_to_cgs
surf_den_xotf=surf_den_motf*n_xotf/n_mol*M_xotf_g/M_motf_g
print "Msun_pc2_to_cgs =", Msun_pc2_to_cgs
print "n_xotf =", n_xotf, "cm^-3"
print "n_xotf(Inui) =", 5.1e-3*fill**(-0.5), "cm^-3"
print "n_mol =", n_mol, "cm^-3"
print "M_xotf_g =", M_xotf_g, "g"
print "M_motf_g =", M_motf_g, "g"
print "I_CO_mdsk_as2 =", I_CO_mdsk_as2, "Jy km/s as^-2"
print "I_CO_motf_as2 =", I_CO_motf_as2, "Jy km/s as^-2"
print "surf_den_mdsk =", surf_den_mdsk, "g/cm^2"
print "surf_den_motf =", surf_den_motf, "g/cm^2"
print "surf_den_xotf =", surf_den_xotf, "g/cm^2"
a=2*math.pi*G
print "2*pi*G =",a
p_grav_motf=a*surf_den_mdsk*surf_den_motf
p_grav_xotf=a*surf_den_mdsk*surf_den_xotf
# ind_p_grav=alog10(2*math.pi*G)+ind_surf_den_gal+ind_surf_den_motf
#a surf_den_gal:surface mass density of galaxy
# surf_den_motf:surface mas density of outflow
print "------------"
print "calculation results"
print "------------"
print "motf-disk grav P: ", p_grav_motf
print "xotf-disk grav P: ", p_grav_xotf
# unit checked

# --- ram pressure (Gunn & Gott 1972) -----------------	#
# p_ram=rho_mol*v_xotf^2
# p_ram=rho_mol*v_xotf^2=(m/V)(2*E_xotf_erg/m)=2*E_xotf_erg/(1/2*4/3*math.pi*R^3)=E_xotf_erg/R^3
#p_ram=E_xotf_erg/R_mol^3
# ind_p_ram=ind_E_xotf_erg-3*alog10(R_mol)
# p_ram=rho_mol*v_motf^2
rho_mol=n_mol/N_A
p_ram=rho_mol*v_motf_cms**2
print "ram P: ",p_ram
# unit checked

# --- shock heated pressure (Thompson et al 2005) -----	#
# SNRate_V=SNRate/V_starburst
# V_starburst=A_starburst*thick
# A_starburst=math.pi*R_starburst^2
A_starburst_pc2=math.pi*R_starburst_pc**2
SNRate_V=SNRate/V_starburst_pc3
E_init=E_xotf_erg
n_ambi=n_mol
p_shk=1.0e-12*(E_init/1.0e51)**(17.0/14)*(n_ambi/0.01)**(-4.0/7)*(SNRate_V/1.0e-13) # [erg cm^-3]
# E_init [erg]
# n_ambi [cm^-3]
# SNRate_V [yr^-1 pc^-3]
# SNRate_V=SNRateate per volume
print "remnant expanded shock P: ", p_shk
# unit checked

# --- thermal pressure --------------------------------	#
p_thm_mol=n_mol*k_B*T_mol
p_thm_xotf=n_xotf*kT_xotf_erg
p_thm_xotf_inui=4.9e-12*fill**(-0.5)
print "molecular gas thermal P: ", p_thm_mol
print "ionized gas thermal P: ", p_thm_xotf
print "ionized gas thermal P(Inui): ", p_thm_xotf_inui
# unit checked

# --- radiation pressure (Thompson et al 2005) --------	#
# SFR_A=SFR/(A_starburst)
A_starburst_cm2=A_starburst_pc2*pc_to_cm**2
SFR_A_cm2=SFR/(A_starburst_cm2)
# when tau << 1
p_rad_thin=c*effi*SFR_A_cm2
# when tau >= 1
p_rad_thick=c*effi*SFR_A_cm2*(1.0/2)*tau
print "optically thin radiation P: ", p_rad_thin
print "optically thick radiation P: ", p_rad_thick
# unit checked

# --- SN explosion pressure (Thompson et al 2005) -----	#
# E_init=E_xotf_erg
# n_ambi=n_mol
p_SN=5*(n_ambi/1.0)**(-1.0/4)*(E_init/1.0e51)**(13.0/14)*p_ram
print "SN explosion P: ",  p_SN
print "------------"
# unit checked

# ---------------------------------------------	#

# --- reference -------------------------------	#
# Greve et al. 2000, AA, 364, 409
# Gunn & Gott 1972, ApJ, 176, 1
# Inui et al. 2005, P: ASJ, 57, 135
# Sakamoto et al. 1995, AJ, 110, 2075
# Tarchi et al. 2000, 358, 95
# Tsai et al. 2009, P: ASJ, 61, 237
# Thompson et al. 2005, ApJ, 630, 167
# Vollmer et al. 2001, ApJ, 561, 708
# Vollmer et al. 2005, AA, 441, 473

exit

