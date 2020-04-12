#!/usr/bin/env python
# NGC 2146

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
pc2cm=3.26*3e10*365*86400
ev2erg=1.6e-12
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
c=3.0e10 # light speed
M_sun=1.99e33 # solar mass
L_sun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24
E_ion_ev=13.6	# [eV]
E_bnd_ev=4.52	# [eV]
N_A=6.02e23
Msun_pc2=M_sun/pc2cm**2
#  --- parameter -------------------------------	#
print "============"
print "NGC 2146"
print "============"
print "parameters"
print "------------"
v_motf_kms=200.0 # km/s (Tsai et al. 2009)
v_sound_kms=1.0e3
T_mol=30.0 # K (Tsai et al. 2009)
T_xotf=1.0e6 # K
n_mol=100.0 # cm^-3 (Tsai et al. 2009)
rho_mol=n_mol/N_A
EI=8.0e62 # cm^-3 (Inui et al. 2005)
R_xotf_pc=6.3*1000*4.8/3.5 # (Inui et al. 2005)
R_xotf_cm=R_xotf_pc*pc2cm
V_xotf_cm3=(4.0/3.0*math.pi)*R_xotf_cm**3 # (Inui et al. 2005)
V_xotf_cm3_Inui=(4.0/3.0*math.pi)*(6.3e3*pc2cm)**3 # (Inui et al. 2005)
fill=0.01 # (Inui et al. 2005)
print "filling factor =", fill
n_xotf=(EI/V_xotf_cm3/fill)**(0.5) # cm^-3 (Iuni et al. 2005)
kT_xotf_ev=0.5e3
kT_xotf_erg=kT_xotf_ev*ev2erg
print "kT [ev] of xray outflow =", kT_xotf_ev,"ev"
print "kT [erg] of xray outflow =", kT_xotf_erg,"erg"
print "V_xotf_cm3 =", V_xotf_cm3
print "V_xotf_cm3 (Inui) =", V_xotf_cm3_Inui
M_xotf_g=n_xotf*m_p*V_xotf_cm3*fill
M_xotf_Msun=M_xotf_g/M_sun
M_xotf_Msun_Inui=1.3e8*fill**0.5
M_xotf_g_Inui=M_xotf_Msun_Inui*M_sun
# print M_xotf_g,R_xotf_pc,R_xotf_cm,n_xotf,m_p,V_xotf_cm3
L_xotf_erg=1.3e40 # (Inui et al. 2005)
E_xotf_erg=1.0e56 # (Inui et al. 2005)
print "L_xotf =", L_xotf_erg, "[erg/s]"
print "E_xotf =", E_xotf_erg, "[erg]"
effi_x_thrm=0.3	# (Strickland & Stevens 2000)
effi_x_mech=0.01	# (Strickland & Stevens 2000)
R_motf_cm=2.0e3*pc2cm # (Tsai et al. 2009)
SFR=10.0 # M_sun/yr (Greve et al. 2000)
SNrate= 0.15 # yr^-1 (Tarchi et al. 2000)
print "SN rate =", SNrate, "[yr-1]"
effi_mass2rad=0.001 # (Thompson et al. 2005)
as_to_pc=80.0
#I_CO_gal_pc2=1.8e3 # within 1.0e7 pc^2 (Tsai et al. 2009)
#I_CO_motf_pc2=150.0 # (Tsai et al. 2009)
#I_CO_msbl_pc2=115.0 # (Tsai et al. 2009)
I_CO_mdsk_as2=13.2/(31100*0.04)	# (Tsai et al. 2009)	# file flux.imstat
I_CO_motf_as2=0.41/(11022*0.04)	# (Tsai, et al. 2009)
M_msbl_Msun=2.6e8 # M_sun (Tsai et al. 2009)
M_motf_Msun=3.4e8 # M_sun (Tsai et al. 2009)
M_motf_g=M_motf_Msun*M_sun # (Tsai et al. 2009)
M_mttl_Msun=4.1e9 # M_sun (Tsai et al. 2009)
M_mdsk_Msun=M_mttl_Msun-M_motf_Msun-M_msbl_Msun
R_starburst_pc=700.0 # (@tau=1# Thompson et al. 2005)
# R_starburst_pc=1000.0 # (our data)
R_starburst_pc_greve=1250.0 # (Greve 2000)
R_conti_pc=2560.0/2 # (our data) (/iapetus/data/satoki_data/ngc2146/20100130.conti89GHz )
V_starburst_pc3_greve=2.0e10 # (Greve 2000)
z_starburst_pc=600.0	# (our calculation) (iapetus:/iapetus/thesis/phd/calculation/veldisp13.sh)
z_starburst_pc_greve=500.0	# (Greve 2000)
tau=10.0
d_mpc=17.2	# Mpc
alpha=1.0	# (Chevalier 1985)
beta=1.0	# (Chevalier 1985)
timescale=1.0e7	# [yr] ; ourdata
surf_den_HI=1.0e21/N_A
surf_den_HI_Msunpc2=surf_den_HI*Msun_pc2
# --- gravitational pressure (Gunn & Gott 1972) -------	#
def flux_to_H2mass(S_CO_as2):
	return (1.2e4*S_CO_Jykms*d_mpc**2)*Msun*1.36
def mass_to_intensity(mass_sun):
	return mass_sun/(1.4/2.0*d_mpc**2*1.18e4)
Msun_to_Ico=1.4/2.0*d_mpc**2*1.18e4
#======I_CO_motf_as2=mass_to_intensity(M_motf_Msun)	# Jy km/s arcsec^-2 (from my data)
def surf_den_CO_Msunpc2(I_CO_as2):
	return 6.5e2*I_CO_as2

def surf_den_CO(I_CO_as2):
	return 6.5e2*I_CO_as2*(M_sun/pc2cm**2)

surf_den_mdsk_Msunpc2=surf_den_CO_Msunpc2(I_CO_mdsk_as2)
surf_den_motf_Msunpc2=surf_den_CO_Msunpc2(I_CO_motf_as2)
surf_den_mdsk=surf_den_CO(I_CO_mdsk_as2)
surf_den_motf=surf_den_CO(I_CO_motf_as2)
surf_den_xotf=surf_den_motf*(n_xotf/n_mol)*(M_xotf_g/M_motf_g)
surf_den_xotf_Msunpc2=surf_den_xotf*Msun_pc2
print "n_xotf =", n_xotf, "[cm^-3]"
print "n_xotf (Inui) =", 5.1e-3*fill**(-0.5), "[cm^-3]"
print "n_mol =", n_mol, "[cm^-3]"
print "rho_mol", '%.2e' %(rho_mol), "[g cm^-3]"
print "M_xotf_g =", '%.2e' %(M_xotf_g), "[g]"
print "M_xotf_Msun =", '%.2e' %(M_xotf_Msun), "[Msun]"
print "M_xotf_g (Inui) =", '%.2e' %(M_xotf_g_Inui), "[g]"
print "M_xotf_Msun (Inui) =", '%.2e' %(M_xotf_Msun_Inui), "[Msun]"
print "M_motf_g =", '%.2e' %(M_motf_g), "[g]"
#print "M_msbl_Msun", M_msbl_Msun, "Msun"
print "M_motf_Msun", '%.2e' %(M_motf_Msun), "[Msun]"
#print "M_mttl_Msun", M_mttl_Msun, "Msun"
print "M_mdsk_Msun", '%.2e' %(M_mdsk_Msun), "[Msun]"
print "I_CO_mdsk_as2 =",'%.2e' %(I_CO_mdsk_as2), "[Jy km/s as^-2]"
print "I_CO_motf_as2 =", '%.2e' %(I_CO_motf_as2), "[Jy km/s as^-2]"
print "surf_den_mdsk =", '%.2f' %(surf_den_mdsk_Msunpc2), "[Msun/pc^2]"
print "surf_den_mdsk =", '%.2e' %(surf_den_mdsk), "[g/cm^2]"
print "surf_den_motf =", '%.2f' %(surf_den_motf_Msunpc2), "[Msun/pc^2]"
print "surf_den_motf =", '%.2e' %(surf_den_motf), "[g/cm^2]"
print "surf_den_xotf =", '%.2e' %(surf_den_xotf_Msunpc2), "[Msun/pc^2]"
print "surf_den_xotf =", '%.2e' %(surf_den_xotf), "[g/cm^2]"
print "surf_den_HI =", '%.2e' %(surf_den_HI_Msunpc2), "[Msun/pc^2]"
print "surf_den_HI =", '%.2e' %(surf_den_HI), "[g/cm^2]"

print "------------"
print "calculation results"
print "------------"
print "+[ grav P = 2*pi*G*(surf_den_xry)*(surf_den_HI_disk) ]+"
def p_grav(surf_den_1,surf_den_2,type):
	gravP=2*math.pi*G*surf_den_1*surf_den_2
	print " o", type, "grav P:", '%.2e' %(gravP)
	return gravP

p_grav_motf=p_grav(surf_den_motf,surf_den_HI,"mol. outflow")
p_grav_xotf=p_grav(surf_den_xotf,surf_den_HI, "xray outflow")
# unit checked

# --- ram pressure (Gunn & Gott 1972) -----------------	#
print "------------"
print "+[ ram P = rho*(relative velocity)^2 ]+"
#E_bnd_ion_particle_erg=(E_bnd_ev+E_ion_ev)*ev2erg
#E_bnd_ion_mass_erg=E_bnd_ion_particle_erg*N_A*M_xotf_g
def ramP(effi_x1,effi_x2,type1,type2):
	print "   ", type1, effi_x1
	print "   ", type2, effi_x2
	effi_x=effi_x1*effi_x2
	E_ttl_erg=E_xotf_erg/effi_x
	print "    total Energy =",'%.2f' %(E_ttl_erg), "[erg]"
	E_mech_erg=E_ttl_erg*(1-effi_x)
	v_xry_kms=math.sqrt(E_mech_erg*2/M_xotf_g)/1.0e5
	print "    v_xry = ",  '%.2f' %(v_xry_kms), "[km/s]"
	v_rel_kms=v_xry_kms-v_motf_kms
	v_rel_cms=v_rel_kms*1.0e5
	p=rho_mol*v_rel_cms**2
	print "    v_rel = ",  '%.2f' %(v_rel_kms), "[km/s]"
	print " o ram P: ", '%.2e' %(p)
	return p
# unit checked
type2="Lx increasing factor"
print "the total energy released by SNe and stellar winds (doesn't include the K.E)"
p_ram1=ramP(0.1,1,"thermalization efficiency (lower)",type2)
p_ram1=ramP(0.3,1,"thermalization efficiency",type2)
p_ram1=ramP(0.5,1,"thermalization efficiency",type2)
p_ram1=ramP(1,1,"thermalization efficiency (upper)",type2)
print "radiating the mechanical energy supplied by the starburst"
p_ram1=ramP(0.01,10,"starburst energy injection rate (thin-disk)",type2)
p_ram1=ramP(0.05,3,"starburst energy injection rate (thick-disk, lower)",type2)
p_ram1=ramP(0.2,3,"starburst energy injection rate (thick-disk, upper)",type2)

# --- SN explosions pressure effect on hot ISM (Thompson et al 2005) --	#
print "------------"
print "+[ shock P = 10^-12*E_xry^(17/14)*n_mol^(-4/7)*SNrate/Vol ]+"
def A_pc2(R):
	A=math.pi*R**2
#	print "Starburst Area = ", '%.2e' %(A) , "[pc^2]"
	return A

def V_pc3(R,z):
	V=math.pi*R**2*z
	return V
# SNrate_V=SNrate/V_starburst
V_conti=V_pc3(R_conti_pc,z_starburst_pc)
V_greve1=V_pc3(R_starburst_pc_greve,z_starburst_pc_greve)
V_greve2=2.0e10 # (Greve 2000)
E_init=E_xotf_erg
n_ambi=n_mol

def p_SNhot(V,type):
	rate_V=SNrate/V
	P=1.0e-12*(E_init/1.0e51)**(17.0/14)*(n_ambi/0.01)**(-4.0/7)*(rate_V/1.0e-13) # [erg cm^-3]
	print "    data from", type
	print "    starburst Volume = ", '%.2e' %(V), "[pc^3]"
	print " o SN shock-heated P: ",  '%.2e' %(P)
#	print "SN explosion P (shock-heated hot ISM): ", P
	return P
# E_init [erg]
# n_ambi [cm^-3]
# SNrate_V [yr^-1 pc^-3]
# SNrate_V=SNrateate per volume
p_SNhot_conti=p_SNhot(V_conti,"89GHz Continuum")
p_SNhot_greve1=p_SNhot(V_greve1,"Greve 2000 (1)")
p_SNhot_greve2=p_SNhot(V_greve2, "Greve 2000 (2)")

# unit checked

# --- thermal pressure --------------------------------	#
print "------------"
print "+[ thermal P = n*k*T ]+"
p_thm_mol=n_mol*k_B*T_mol
p_thm_xotf=2*n_xotf*kT_xotf_erg
p_thm_xotf_inui=4.9e-12*fill**(-0.5)
print " o molecular gas thermal P: ", p_thm_mol
print " o ionized gas thermal P: ",  '%.2e' %(p_thm_xotf)
print " o ionized gas thermal P (Inui): ", p_thm_xotf_inui
# unit checked

# --- radiation pressure (Thompson et al 2005) --------	#
print "------------"
print "+[ radiation P = effic*SFR/Area*c ]+"
# SFR_A=SFR/(A_starburst)
A_starburst_cm2=A_pc2(R_conti_pc)*pc2cm**2
SFR_A_cm2=SFR/(A_starburst_cm2)
# when tau << 1
p_rad_thin=c*effi_mass2rad*SFR_A_cm2
# when tau >= 1
p_rad_thick=c*effi_mass2rad*SFR_A_cm2*(1.0/2)*tau
#print " o optically thin radiation P: ",  '%.2e' %(p_rad_thin)
print " o optically thick radiation P: ",  '%.2e' %(p_rad_thick)
# unit checked

# --- SN explosion pressure affect on cold ISM (Thompson et al 2005) --	#
print "------------"
print "+[ SN explosion P = 5*n_mol^(-1/4)*E_xry^(13/14*P_rad) ]+"
# E_init=E_xotf_erg
# n_ambi=n_mol
p_SN_cold=5*(n_ambi/1.0)**(-1.0/4)*(E_init/1.0e51)**(13.0/14)*p_rad_thick
print " o SN explosion P (cold ISM): ",  '%.2e' %(p_SN_cold)
print "------------"
# unit checked

# ---------------------------------------------	#

# --- reference -------------------------------	#
# Chevalier et al. 2001, ApJ, 558, L27
# Chevalier et al. 1985, Nature, 317, 44
# Greve et al. 2000, AA, 364, 409
# Gunn & Gott 1972, ApJ, 176, 1
# Inui et al. 2005, P: ASJ, 57, 135
# Sakamoto et al. 1995, AJ, 110, 2075
# Strickland & Stevens 2000, MNRAS, 314, 511
# Tarchi et al. 2000, 358, 95
# Tsai et al. 2009, P: ASJ, 61, 237
# Thompson et al. 2005, ApJ, 630, 167
# Vollmer et al. 2001, ApJ, 561, 708
# Vollmer et al. 2005, AA, 441, 473

exit

