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
v_otf_kms=200.0 # km/s (Tsai et al. 2009)
v_otf_cms=v_otf_kms*1.0e5 # cm/s
T_mol=30.0 # K (Tsai et al. 2009)
T_xry=1.0e6 # K
n_mol=100.0 # cm^-3 (Tsai et al. 2009)
EI=8.0e62 # (Inui et al. 2005)
R_xry_pc=6.3*1000*4.8/3.5 # (Inui et al. 2005)
R_xry_cm=R_xry_pc*pc_to_cm
V_xry=(4.0/3.0*math.pi)*R_xry_cm**3 # (Inui et al. 2005)
fill=0.03 # (Inui et al. 2005)
n_xry=(EI/V_xry*fill)**(0.5) # cm^-3 (Iuni et al. 2005)
kT_xry=0.5*100*ev_to_erg
M_xry=n_xry*m_p*V_xry*fill
print "------------"
#print M_xry,R_xry_pc,R_xry_cm,n_xry,m_p,V_xry
E_xry=1.0e56 # (Inui et al. 2005)
R_mol=2.0e3*pc_to_cm # (Tsai et al. 2009)
SFR=10.0 # M_sun/yr (Greve et al. 2000)
SNRate= 0.15 # yr^-1 (Tarchi et al. 2000)
effi=0.001 # (Thompson et al. 2005)
as_to_pc=80.0
#I_CO_gal_pc2=1.8e3 # within 1.0e7 pc^2 (Tsai et al. 2009)
#I_CO_otf_pc2=150.0 # (Tsai et al. 2009)
#I_CO_sbl_pc2=115.0 # (Tsai et al. 2009)
M_sbl=2.6e8 # M_sun (Tsai et al. 2009)
M_otf=3.4e8 # M_sun (Tsai et al. 2009)
M_otf_g=M_otf*M_sun # (Tsai et al. 2009)
M_ttl=4.1e9 # M_sun (Tsai et al. 2009)
M_dsk=M_ttl-M_otf-M_sbl
thick_pc=500.0	# (Greve 2000)
R_starburst_pc=700.0 # (@tau=1# Thompson et al. 2005)
R_starburst_pc=1000.0 # (our data)
R_starburst_pc=1250.0 # (Greve 2000)
V_starburst_pc3=1.0e10 # (Greve 2000)
tau=10.0
d=17.2	# Mpc
# --- gravitational pressure (Gunn & Gott 1972) -------	#
Msun_to_Ico=1.4/2.0*d**2*1.18e4
I_CO_dsk_as2=M_dsk/Msun_to_Ico	# Jy km/s arcsec^-2 (from my data)
I_CO_otf_as2=M_otf/Msun_to_Ico	# Jy km/s arcsec^-2 (from my data)
# I_CO_dsk_as2=I_CO_dsk_pc2/(1.0e7/as_to_pc**2)
# surf_den_mol[M_sun/pc^2]=6.5e2*I(CO)[Jy km/s as^(-2)] # (Sakamoto et al. 1995)
# surf_den_mol[M_g/cm^2]=surf_den_mol[M_sun/pc^2]*Msun_pc2_to_Mg_cm2
Msun_pc2_to_Mg_cm2=M_sun/pc_to_cm**2
surf_den_dsk=6.5e2*I_CO_dsk_as2
surf_den_otf=6.5e2*I_CO_otf_as2
surf_den_xry=surf_den_otf*n_xry/n_mol*M_xry/M_otf_g
print "Msun_pc2_to_Mg_cm2 =", Msun_pc2_to_Mg_cm2
print "n_xry =", n_xry
print "n_mol =", n_mol
print "M_xry =", M_xry
print "M_otf =", M_otf
print "I_CO_gal_pc2 =", I_CO_gal_pc2
print "I_CO_otf_pc2 =", I_CO_otf_pc2
print "I_CO_sbl_pc2 =", I_CO_sbl_pc2
print "surf_den_dsk =", surf_den_dsk
print "surf_den_otf =", surf_den_otf
print "surf_den_xry =", surf_den_xry
a=2*math.pi*G
print "2*pi*G =",a
print "surf_den_dsk,surf_den_otf =", surf_den_dsk,surf_den_otf
p_grav_mol=a*surf_den_dsk*surf_den_mol
p_grav_xry=a*surf_den_dsk*surf_den_xry
# ind_p_grav=alog10(2*math.pi*G)+ind_surf_den_gal+ind_surf_den_otf
#a surf_den_gal:surface mass density of galaxy
# surf_den_otf:surface mas density of outflow
print "------------"
print "molotf-disk grav P: ", p_grav_mol
print "xryotf-disk grav P: ", p_grav_xry
# unit checked

# --- ram pressure (Gunn & Gott 1972) -----------------	#
# p_ram=rho_mol*v_xry^2
# p_ram=rho_mol*v_xry^2=(m/V)(2*E_xry/m)=2*E_xry/(1/2*4/3*math.pi*R^3)=E_xry/R^3
#p_ram=E_xry/R_mol^3
# ind_p_ram=ind_E_xry-3*alog10(R_mol)
# p_ram=rho_mol*v_otf^2
rho_mol=n_mol/N_A
p_ram=rho_mol*v_otf_cms**2
print "ram P: ",p_ram
# unit checked

# --- shock heated pressure (Thompson et al 2005) -----	#
# SNRate_V=SNRate/V_starburst
# V_starburst=A_starburst*thick
# A_starburst=math.pi*R_starburst^2
A_starburst_pc2=math.pi*R_starburst_pc**2
SNRate_V=SNRate/V_starburst_pc3
E_init=E_xry
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
p_thm_xry=n_xry*kT_xry
p_thm_xry_inui=4.9e-12*fill**(-0.5)
print "molecular gas thermal P: ", p_thm_mol
print "ionized gas thermal P: ", p_thm_xry
print "ionized gas thermal P(Inui): ", p_thm_xry_inui
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
# E_init=E_xry
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

