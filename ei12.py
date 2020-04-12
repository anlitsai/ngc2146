#!/usr/bin/env python
# /iapetus/thesis/phd/calculation/ei03.py

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
yr=365*86400.0	# [sec]
pc=3.26*c*yr	# [cm]
#print pc
kpc=pc*1.0e3	# [cm]
au=1.5e13	# [cm]
mpc=pc*1.0e6	# [cm]
ev=1.60217653e-12	# [erg]
k_B=1.3806505e-16	# [erg/K]
ev_kB=ev/k_B	# [K]
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
Msun=1.99e33 # solar mass
Msun_pc2=Msun/pc**2
Lsun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24	# [g/particle]
m_u=1.66e-24	# [g/particle]
m_e=9.11-27	# [g/particle]
E_ion_ev=13.6	# [eV]
E_bnd_ev=4.52	# [eV]
as2rad=1.0/3600/180*math.pi	# [rad]
# --- parameter -------------------------------	#
z_n2146=0.003
z_n3628=0.0028
as2pc_n2146=80.0
as2pc_n3628=35.0
r_inui_n2146_arcmin=1.8
r_min_halo_n2146_arcmin=2.0
r_maj_halo_n2146_arcmin=2.0
r_core_n3628_arcmin=0.25
r_maj_core_n3628_arcmin=0.25
r_min_core_n3628_arcmin=0.25
r_maj_halo_n3628_arcmin=3.0
r_min_halo_n3628_arcmin=3.0
r_n2146_kpc=r_inui_n2146_arcmin*60*as2pc_n2146
r_n3628_kpc=0.5
r_n2146_kpc=2.0
r_n3628_kpc=0.5
d_n2146_mpc=17.2 # Tully 1988
#d_n2146_mpc=16.47
#d_n2146_mpc=11.6
#d_n3628_mpc=10.04
d_n3628_mpc=7.7 # Tully 1988
v_mol_n2146_kms=200.0
v_mol_n3628_kms=90.0
v_plm_kms=340.0
v_plm_kms=600.0

#  ------------------------------------	#
def as2pc(d_mpc,note):
	as_pc=d_mpc*1.0e6*au/pc
	print "1 arcsec = ", '%.2f' %as_pc, "[pc]", note
	return as_pc

print "------------------------------------"
a2p_n2146=as2pc(d_n2146_mpc,"@ n2146")
a2p_n3628=as2pc(d_n3628_mpc,"@ n3628")
print a2p_n2146, a2p_n3628
print "------------------------------------"

#  ------------------------------------	#
p1_mol=100*k_B*10
p2_mol=1000*k_B*100
#  ------------------------------------	#
#def EI(norm,radius_kpc, theta_arcmin, z ,note,f1,f2,kT_kev):
def EI(norm, d_mpc, r_maj_arcmin,r_min_arcmin, z ,note,f1,f2,eff_thrm,kT_kev,v_mol_kms, v_plm_kms):
#	R=radius_kpc*1000*pc
	arcsec2pc=math.sin(as2rad)*d_mpc*mpc/pc
	r_maj_rad=r_maj_arcmin*60.0*as2rad
	r_min_rad=r_min_arcmin*60.0*as2rad
#	Da=R/math.sin(theta_rad)
	Da=d_mpc*mpc
	R_maj=math.sin(r_maj_rad)*Da
	R_min=math.sin(r_min_rad)*Da
	r_maj_kpc=R_maj/kpc
	r_min_kpc=R_min/kpc
	a=1.0e-14/(4*math.pi*(Da*(1+z))**2)
	ei=norm/a
	V=4.0/3*math.pi*R_maj*R_min**2
	Vf1=V*f1
	Vf2=V*f2
	n_e=math.sqrt(ei/V)
#	n_e=math.sqrt(ei/Vf)
	n_e1=n_e/math.sqrt(f1)
	n_e2=n_e/math.sqrt(f2)
	kT=kT_kev*1000*ev
	p=2*n_e*kT#/1.66	p=(n_e+n_i)kT=2*n_e*kT
	p1=p/math.sqrt(f1)
	p2=p/math.sqrt(f2)
	rho_e=n_e*m_p
	rho_e1=n_e1*m_p
	rho_e2=n_e2*m_p
	M=rho_e*V/Msun
	M1=M*math.sqrt(f1)
	M2=M*math.sqrt(f2)
	E=3*n_e*kT*V#/1.66	1/2*mv^2=3/2*kT
	E1=E*math.sqrt(f1)
	E2=E*math.sqrt(f2)
	Et=E/eff_thrm
	Et1=E1/eff_thrm
	Et2=E2/eff_thrm
	v_rel=(v_mol_kms-v_plm_kms)*1.0e5
	v_rel1=(v_mol_kms-10-v_plm_kms)*1.0e5
	v_rel2=(v_mol_kms+10-v_plm_kms)*1.0e5
	p_ram=rho_e*v_rel**2
	p_ram10=rho_e1*v_rel**2
	p_ram11=rho_e1*v_rel1**2
	p_ram12=rho_e1*v_rel2**2
	p_ram20=rho_e2*v_rel**2
	p_ram21=rho_e2*v_rel1**2
	p_ram22=rho_e2*v_rel2**2
	print "------------------------------------"
	print note 
	print "------------------------------------"
	print "1 [as] = ", '%.2f' %arcsec2pc, "[pc]"
	print "norm = ", '%.2e' %norm
	print "radius = ", '%.2f' %r_maj_kpc, "[kpc] x", '%.2f' %r_min_kpc, "[kpc]"
	print "theta = ", '%.2f' %r_maj_arcmin, "[arcmin] x", '%.2f' %r_min_arcmin, "[arcmin]"
	print "Distance = ", '%.2e' %Da, "[cm]", '%.2f' %(d_mpc), "[mpc]"
#	print "Angular diameter distance (D_A) = ", '%.2e' %Da, "[cm]", '%.2e' %(Da/kpc), "[kpc]"
	print "redshift (z) = ", z
	print "EI = int(n_e n_H dV)= ", '%.2e' %ei, "[cm-3]"
	print "volume (V) = ", '%.2e' %V, "[cm3]"
	print "kT = ", kT_kev, "[keV]"
	print "filling factor (f) = ", f1,"--", f2
	print "plasma number density (n_e) = ", '%.3e' %n_e, "(",'%.3e' %n_e1,"--", '%.3e' %n_e2,") [cm-3]"
	print "plasma mass density (rho_e) = ", '%.3e' %rho_e, "(",'%.3e' %rho_e1,"--", '%.3e' %rho_e2,") [g cm-3]"
#	print "ram pressure (p_ram) = ", '%.3e' %p_ram,"(",'%.3e' %p_ram12, "--",'%.3e' %p_ram21,  ") [dyne cm-2]"
	print "ram pressure (p_ram) = ", '%.3e' %p_ram,"(",'%.3e' %p_ram10,"--", '%.3e' %p_ram11,"--",'%.3e' %p_ram12, "--",'%.3e' %p_ram20, "--",'%.3e' %p_ram21, "--",'%.3e' %p_ram22, ") [dyne cm-2]"
	print "plasma thermal pressure (p_ion) = ", '%.3e' %p,"(",'%.3e' %p1,"--",'%.3e' %p2, ") [dyne cm-2]"
	print "molecular pressure (p_mol) = (", '%.3e' %p1_mol,"--",'%.3e' %p2_mol, ") [dyne cm-2]"
	print "plasma mass (M) = ",  '%.3e' %M,"(",'%.3e' %M1,"--",'%.3e' %M2, ") [Msun]"
	print "plasma thermal energy (E) = ",  '%.4e' %E,"(",'%.4e' %E1,"--",'%.4e' %E2, ") [erg]"
	print "plasma total energy (E) = ",  '%.4e' %Et,"(",'%.4e' %Et1,"--",'%.4e' %Et2, ") [erg]"
	return ei

print "------------------------------------"
ei_n3628=EI(5.06958E-06,d_n3628_mpc,r_maj_core_n3628_arcmin,r_min_core_n3628_arcmin,z_n3628,"NGC3628 core, vmekal+pow, grp, test76",0.1,0.01,0.3,0.46,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(4.69897E-06,d_n3628_mpc,r_maj_core_n3628_arcmin,r_min_core_n3628_arcmin,z_n3628,"NGC3628 core, vmekal+pow, grp_2, test76",0.1,0.01,0.3,0.48,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(5.25052E-06,d_n3628_mpc,r_maj_core_n3628_arcmin,r_min_core_n3628_arcmin,z_n3628,"NGC3628 core, mekal+pow, grp, test76",0.1,0.01,0.3,0.44,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(5.96931E-06,d_n3628_mpc,r_maj_core_n3628_arcmin,r_min_core_n3628_arcmin,z_n3628,"NGC3628 core, mekal+pow, grp_2, test76",0.1,0.01,0.3,0.43,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(3.53883E-06,d_n3628_mpc,r_maj_core_n3628_arcmin,r_min_core_n3628_arcmin,z_n3628,"NGC3628 core, raym+pow, grp, test76",0.1,0.01,0.3,0.45,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(6.28310E-05,d_n3628_mpc,r_maj_halo_n3628_arcmin,r_min_halo_n3628_arcmin,z_n3628,"NGC3628 halo, vmekal+pow, test76",0.1,0.01,0.3,0.372,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(7.16039E-05,d_n3628_mpc,r_maj_halo_n3628_arcmin,r_min_halo_n3628_arcmin,z_n3628,"NGC3628 halo, vmekal+pow, test93",0.1,0.01,0.3,0.33,v_mol_n3628_kms,v_plm_kms)

print "------------------------------------"
print "test 93"
print "------------------------------------"
ei_n3628=EI(7.16039E-05,d_n3628_mpc,r_maj_halo_n3628_arcmin,r_min_halo_n3628_arcmin,z_n3628,"NGC3628 halo, vmekal+pow, test93",0.1,0.01,0.3,0.331452,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(2.46909E-06,d_n3628_mpc,r_maj_core_n3628_arcmin,r_min_core_n3628_arcmin,z_n3628,"NGC3628 core, vraym+pow, test93",0.1,0.01,0.3,0.497376,v_mol_n3628_kms,v_plm_kms)
print "------------------------------------"
print "test 98"
print "------------------------------------"
ei_n3628=EI(7.16797E-05,d_n3628_mpc,3.0,3.0,z_n3628,"NGC3628 halo, vmekal+pow, grp, test98",0.1,0.01,0.3,0.33,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(3.49790E-06,d_n3628_mpc,0.25,0.25,z_n3628,"NGC3628 core, vraym+pow, grp, test98",0.1,0.01,0.3,0.50,v_mol_n3628_kms,v_plm_kms)
print "------------------------------------"
ei_n3628=EI(3.56274E-04,d_n3628_mpc,r_maj_halo_n3628_arcmin,r_min_halo_n3628_arcmin,z_n3628,"NGC3628, r=3arcmin",0.1,0.01,0.3,0.577,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(2.33972E-04,d_n3628_mpc,r_maj_halo_n3628_arcmin,r_min_halo_n3628_arcmin,z_n3628,"NGC3628, r=0.25arcmin",0.1,0.01,0.3,0.6,v_mol_n3628_kms,v_plm_kms)
print "------------------------------------"
print "test 86"
print "------------------------------------"
ei_n3628=EI(1.08433E-04,d_n3628_mpc,r_maj_halo_n3628_arcmin,r_min_halo_n3628_arcmin,z_n3628,"NGC3628, r=3arcmin, vmekal",0.1,0.01,0.3,0.30,v_mol_n3628_kms,v_plm_kms)
ei_n3628=EI(6.06550E-05,d_n3628_mpc,r_maj_core_n3628_arcmin,r_min_core_n3628_arcmin,z_n3628,"NGC3628, r=0.25arcmin, vmekal, not correct",0.1,0.01,0.3,0.45,v_mol_n3628_kms,v_plm_kms)

print "------------------------------------"
print "test 100"
print "------------------------------------"
#ei_n3628=EI(7.48473E-05,d_n3628_mpc,3,3,z_n3628,"NGC3628 halo, vapec+pow, grp, test100",0.1,0.01,0.3,0.33)
ei_n3628=EI(7.17317E-05,d_n3628_mpc,3,3,z_n3628,"NGC3628 halo, vmekal+pow, grp, test100",0.1,0.01,0.3,0.32,v_mol_n3628_kms,v_plm_kms)
#ei_n3628=EI(7.36888E-05,d_n3628_mpc,3,3,z_n3628,"NGC3628 halo, vraym+pow, grp, test100",0.1,0.01,0.3,0.35)
#ei_n3628=EI(4.34171E-06,d_n3628_mpc,0.3,0.3,z_n3628,"NGC3628 core, vapec+pow, grp, test100",0.1,0.01,0.3,0.54)
#ei_n3628=EI(3.72853E-06,d_n3628_mpc,0.3,0.3,z_n3628,"NGC3628 core, vmekal+pow, grp, test100",0.1,0.01,0.3,0.53)
ei_n3628=EI(2.46195E-06,d_n3628_mpc,0.3,0.3,z_n3628,"NGC3628 core, vraym+pow, grp, test100",0.1,0.01,0.3,0.58,v_mol_n3628_kms,v_plm_kms)
print "------------------------------------"
#print "test 100+"
#print "------------------------------------"
#ei_n3628=EI(7.78339E-06,d_n3628_mpc,0.3,0.3,z_n3628,"NGC3628 core, vmekal+pow, grp, test100+",0.1,0.01,0.3,0.49)
#ei_n3628=EI(4.78339E-06,d_n3628_mpc,0.3,0.3,z_n3628,"NGC3628 core, vmekal+pow, grp, test100+",0.1,0.01,0.3,0.49)
#ei_n3628=EI(5.78339E-06,d_n3628_mpc,0.3,0.3,z_n3628,"NGC3628 core, vmekal+pow, grp, test100+",0.1,0.01,0.3,0.49)
#print "------------------------------------"
#print "EI(norm, d_mpc, r_maj_arcmin, r_min_arcmin, z, note, f1, f2, kT_kev)"
#print "------------------------------------"
ei_n2146=EI(3.56274E-04,d_n2146_mpc,0.4/2,0.4/2,z_n2146,"NGC2146 core (0.4arcm diameter?), vraym+pow, grp, test20",0.1,0.01,0.3,0.577,v_mol_n2146_kms,v_plm_kms)
ei_n2146=EI(3.56274E-04,d_n2146_mpc,2.0/2,2.0/2,z_n2146,"NGC2146 halo (2arcm diameter?), vraym+pow, grp, test19",0.1,0.01,0.3,0.577345,v_mol_n2146_kms,v_plm_kms)
ei_n2146=EI(2.51542E-04,d_n2146_mpc,0.5/2,0.5/2,z_n2146,"NGC2146 core (0.5arcm diameter) re-fit 20110514, vmekal+pow, grp, test28",0.1,0.01,0.3,0.582138,v_mol_n2146_kms,v_plm_kms)
ei_n2146=EI(3.12928E-04,d_n2146_mpc,0.5/2,0.5/2,z_n2146,"NGC2146 core (0.5arcm diameter) re-fit 20110514, vraymond+pow, grp, test28",0.1,0.01,0.3,0.62635,v_mol_n2146_kms,v_plm_kms)
print "------------------------------------"

V_n2146_inui=4.0/3*math.pi*(6.3*1000*pc)**3
V2_n2146_inui=4.0/3*math.pi*(1.0*1000*pc)**3
V_n3628_dahlem=math.pi*14.0**2*40.0*(1000*pc)**3

def EI2(ei,V,f1,f2,kT_kev,note):
	Vf1=V*f1
	Vf2=V*f2
	n_e=math.sqrt(ei/V)
#	n_e=math.sqrt(ei/Vf)
	n_e1=n_e/math.sqrt(f1)
	n_e2=n_e/math.sqrt(f2)
	kT=kT_kev*1000*ev
	p=2*n_e*kT#/1.66
	p1=p/math.sqrt(f1)
	p2=p/math.sqrt(f2)
	rho_e=n_e*m_p
	rho_e1=n_e1*m_p
	rho_e2=n_e2*m_p
	M=rho_e*V/Msun
	M1=M*math.sqrt(f1)
	M2=M*math.sqrt(f2)
	E=3*n_e*kT*V#/1.66
	E1=E*math.sqrt(f1)
	E2=E*math.sqrt(f2)
	print "------------------------------------"
	print "note = ", note 
	print "------------------------------------"
#	print "radius = ", '%.2f' %radius_kpc, "[kpc]"
	print "EI = int(n_e n_H dV)= ", '%.2e' %ei, "[cm-3]"
	print "volume (V) = ", '%.2e' %V, "[cm3]"
	print "kT = ", kT_kev, "[keV]"
	print "filling factor (f) = ", f1,"--", f2
	print "plasma number density (n_e) = ", '%.3e' %n_e, "(",'%.3e' %n_e1,"--", '%.3e' %n_e2,") [cm-3]"
	print "plasma mass density (rho_e) = ", '%.3e' %rho_e, "(",'%.3e' %rho_e1,"--", '%.3e' %rho_e2,") [cm-3]"
	print "plasma pressure (p) = ", '%.3e' %p,"(",'%.3e' %p1,"--",'%.3e' %p2, ") [dyne cm-2]"
	print "plasma mass (M) = ",  '%.3e' %M,"(",'%.3e' %M1,"--",'%.3e' %M2, ") [Msun]"
	print "plasma thermal energy (E) = ",  '%.3e' %E,"(",'%.3e' %E1,"--",'%.3e' %E2, ") [erg]"
	return ei
print "------------------------------------"
ei2_n2146=EI2(8.0E+62,V_n2146_inui,0.1,0.01,0.5,"NGC2146, Inui 2005, r=1.8arcmin,V=4/3xpix6.3^3 kpc^3")
ei2_n2146=EI2(8.0E+62,V2_n2146_inui,0.1,0.01,0.5,"NGC2146, Inui 2005, r=0.3arcmin,V=4/3xpix1.0^3 kpc^3")
ei2_n3628=EI2(2.4E+62,V_n3628_dahlem,0.1,0.01,0.16,"NGC3628, Dahlem 1996, V=14^2x40xpi kpc^3")
print "------------------------------------"
print "EI2(ei,V_cm3,f1,f2,kT_kev,note)"

# --- reference -------------------------------	#
# http://en.wikipedia.org/wiki/Angular_diameter_distance
# http://en.wikipedia.org/wiki/Degree_(angle)
# http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/manual/XSmodelMekal.html

exit

