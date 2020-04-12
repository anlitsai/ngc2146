#!/usr/bin/env python
# /iapetus/thesis/phd/calculation/ei03.py

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
pc=3.26*c*365*86400	# [cm]
#print pc
kpc=pc*1.0e3	# [cm]
au=1.5e13	# [cm]
mpc=pc*1.0e6	# [cm]
ev=1.6e-12	# [erg]
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
Msun=1.99e33 # solar mass
Msun_pc2=Msun/pc**2
Lsun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24	# [g]
E_ion_ev=13.6	# [eV]
E_bnd_ev=4.52	# [eV]
as2rad=1.0/3600/180*math.pi	# [rad]
# --- parameter -------------------------------	#
z_n2146=0.003
z_n3628=0.0028
as2pc_n2146=80.0
as2pc_n3628=35.0
r_inui_n2146_arcmin=1.8
r_circle_n2146_arcmin=2.0
r_core_n3628_arcmin=0.25
r_circle_n3628_arcmin=2.0
r_n2146_kpc=r_inui_n2146_arcmin*60*as2pc_n2146
r_n3628_kpc=0.5
r_n2146_kpc=2.0
r_n3628_kpc=0.5
d_n2146_mpc=17.2
d_n2146_mpc=16.47
#d_n2146_mpc=11.6
d_n3628_mpc=10.04


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
def arcm2kpc(size_arcmin,d_mpc,note):
	am_kpc=size_arcmin*60*as2rad*d_mpc*1000
#	am_kpc=r_arcmin/60/360*2*math.pi*as_kpc
	print '%.2f' %size_arcmin,"[arcmin] =",'%.2f' %am_kpc, "[kpc] for",note,"@ d=", '%.2f' %d_mpc, "[Mpc]"
	return am_kpc

print "------------------------------------"
am2kp_inui_n2146=arcm2kpc(r_inui_n2146_arcmin,d_n2146_mpc,"n2146")
am2kp_circle_n2146=arcm2kpc(r_circle_n2146_arcmin,d_n2146_mpc,"n2146")
am2kp_core_n3628=arcm2kpc(r_core_n3628_arcmin,d_n3628_mpc,"n3628")
am2kp_circle_n3628=arcm2kpc(r_circle_n3628_arcmin,d_n3628_mpc,"n3628")
print "------------------------------------"
#  ------------------------------------	#
def EI(norm,radius_kpc, theta_arcmin, z ,note,fill,kT_kev):
	R=radius_kpc*1000*pc
	theta_rad=theta_arcmin*60.0*as2rad
	Da=R/math.sin(theta_rad)
	a=1.0e-14/(4*math.pi*(Da*(1+z))**2)
	ei=norm/a
	V=4.0/3*math.pi*R**3
	Vf=V*fill
	n_e=math.sqrt(ei/Vf)
	kT=kT_kev*1000*ev
	p=2*n_e*kT/1.6666
	M=n_e*m_p*Vf/Msun
	E=3*n_e*kT*Vf
	print "------------------------------------"
	print "note = ", note 
	print "------------------------------------"
	print "norm = ", '%.2e' %norm
	print "radius = ", '%.2f' %radius_kpc, "[kpc]"
	print "theta = ", '%.2e' %theta_arcmin, "[arcmin]"
	print "Angular diameter distance (D_A) = ", '%.2e' %Da, "[cm]"
	print "redshift (z) = ", z
	print "EI = int(n_e n_H dV)= ", '%.2e' %ei, "[cm-3]"
	print "filling factor (f) = ", fill
	print "volume (V) = ", '%.2e' %V, "[cm3]"
	print "kT = ", kT_kev, "[keV]"
	print "plasma density (n_e) = ", '%.2e' %n_e, "[cm-3]"
	print "plasma pressure (p) = ", '%.2e' %p, "[dyne cm-2]"
	print "plasma mass (M) = ", '%.2e' %M, "[Msun]"
	print "plasma thermal energy (E) = ", '%.2e' %E, "[erg]"
	return ei

print "------------------------------------"
ei_n3628=EI(4.70183E-06,am2kp_core_n3628,r_core_n3628_arcmin,z_n3628,"NGC 3628 core, vmekal+pow",1,0.479)
ei_n3628=EI(4.70183E-06,am2kp_core_n3628,r_core_n3628_arcmin,z_n3628,"NGC 3628 core, vmekal+pow",0.1,0.479)
ei_n3628=EI(4.70183E-06,am2kp_core_n3628,r_core_n3628_arcmin,z_n3628,"NGC 3628 core, vmekal+pow",0.01,0.479)
ei_n3628=EI(5.95039E-06,am2kp_core_n3628,r_core_n3628_arcmin,z_n3628,"NGC 3628 core, mekal+pow",1,0.43)
ei_n3628=EI(5.95039E-06,am2kp_core_n3628,r_core_n3628_arcmin,z_n3628,"NGC 3628 core, mekal+pow",0.1,0.43)
ei_n3628=EI(5.95039E-06,am2kp_core_n3628,r_core_n3628_arcmin,z_n3628,"NGC 3628 core, mekal+pow",0.01,0.43)
ei_n3628=EI(6.28310E-05,am2kp_circle_n3628,r_circle_n3628_arcmin,z_n3628,"NGC 3628 outside, vmekal+pow",1,0.372)
#ei_n3628=EI(6.28310E-05,am2kp_circle_n3628,r_circle_n3628_arcmin,z_n3628,"NGC 3628 outside, vmekal+pow",0.1,0.372)
#ei_n3628=EI(6.28310E-05,am2kp_circle_n3628,r_circle_n3628_arcmin,z_n3628,"NGC 3628 outside, vmekal+pow",0.01,0.372)
print "------------------------------------"
ei_n2146=EI(3.56274E-04,am2kp_circle_n2146,r_circle_n2146_arcmin,z_n2146,"NGC 2146",1,0.577)
print "------------------------------------"
print "EI(norm, radius_kpc, theta_arcmin, z, note, fill, kT_kev)"

# --- reference -------------------------------	#
# http://en.wikipedia.org/wiki/Angular_diameter_distance
# http://en.wikipedia.org/wiki/Degree_(angle)
# http://heasarc.gsfc.nasa.gov/docs/xanadu/xspec/manual/XSmodelMekal.html

exit

