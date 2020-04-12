#!/usr/bin/env python
# NGC 2146

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
yr=365*86400
pc=3.26*c*yr
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
#E_ion_ev=13.6	# [eV]
#E_bnd_ev=4.52	# [eV]
#  --- parameter -------------------------------	#
print "============"
print "NGC 2146"
print "============"
print "parameters"
print "------------"
i_deg=70.0
i_pi=i_deg/180.0*math.pi
sin_i=math.sin(i_pi)
cos_i=math.cos(i_pi)
D_Mpc=17.2
X_CO2H2=1.4/3.0
H22mol=1.36
XH=X_CO2H2*H22mol
print "inclination",i_pi,sin_i,cos_i
v_motf_kms_n2146=200.0 # km/s (Tsai et al. 2009)
v_motf_kms_n3628=90.0 # km/s (Tsai et al. 2009)
v_sound_kms=1.0e3
T_mol=30.0 # K (Tsai et al. 2009)
T_xotf=1.0e6 # K
EI_n2146=8.0e62 # cm^-3 (Inui et al. 2005)
EI_n3628=1.0e61 # cm^-3 (chandra)
R_xotf_n2146_pc=6.3*1000*4.8/3.5 # (Inui et al. 2005)
#print "R_xotf_n2146 ",R_xotf_n2146_pc , "[pc]"
R_xotf_n3628_pc=0.5*1000 # (Inui et al. 2005)
R_xotf_n2146=R_xotf_n2146_pc*pc
R_xotf_n3628=R_xotf_n3628_pc*pc
V_xotf_n2146=(4.0/3.0*math.pi)*R_xotf_n2146**3 # (Inui et al. 2005)
V_xotf_n2146_Inui=(4.0/3.0*math.pi)*(6.3e3*pc)**3 # (Inui et al. 2005)
V_xotf_n3628=(4.0/3.0*math.pi)*R_xotf_n3628**3 # (Inui et al. 2005)
fill=0.01 # (Inui et al. 2005)
print "filling factor =", fill
n_mol=100.0 # cm^-3 (Tsai et al. 2009)
rho_mol=n_mol/N_A
n_xotf_n2146=(EI_n2146/V_xotf_n2146/fill)**(0.5) # cm^-3 (Iuni et al. 2005)
print "n_xotf_n2146 =", n_xotf_n2146, "[cm^-3]"
print "n_xotf_n2146 (Inui) =", 5.1e-3*fill**(-0.5), "[cm^-3]"
n_xotf_n3628=(EI_n3628/V_xotf_n3628/fill)**(0.5) # cm^-3 (Iuni et al. 2005)
print "n_mol =", n_mol, "[cm^-3]"
print "rho_mol", '%.1e' %(rho_mol), "[g cm^-3]"
kT_xotf_ev=0.5e3
kT_xotf=kT_xotf_ev*ev
print "kT [ev] of xray outflow =", kT_xotf_ev,"ev"
print "kT [erg] of xray outflow =", kT_xotf,"erg"
print "V_xotf_n2146 =", V_xotf_n2146
print "V_xotf_n2146 (Inui) =", V_xotf_n2146_Inui
rho_xotf_n2146=n_xotf_n2146*m_p
rho_xotf_n3628=n_xotf_n3628*m_p
print "rho_xotf_n2146", rho_xotf_n2146, "[g/cm3]"
M_xotf_n2146=rho_xotf_n2146*V_xotf_n2146*fill
M_xotf_n2146_Msun=M_xotf_n2146/Msun
M_xotf_n2146_Msun_Inui=1.3e8*fill**0.5
M_xotf_n2146_Inui=M_xotf_n2146_Msun_Inui*Msun
M_xotf_n3628=rho_xotf_n3628*V_xotf_n3628*fill
print "M_xotf_n2146=",M_xotf_n2146,"[g] ; M_xotf_n2146_Inui=",M_xotf_n2146_Inui,"[g]"
print "M_xotf_n2146=",'%2e' %M_xotf_n2146_Msun,"[Msun] ; M_xotf_n2146_Inui=",'%2e' %M_xotf_n2146_Msun_Inui,"[Msun]"
M_galdsk_Msun=8.67e10
M_galdsk_Msun=2.18e11
M_galdsk=M_galdsk_Msun*Msun
L_xotf=1.3e40 # (Inui et al. 2005)
E_xotf_n2146=1.0e56 # (Inui et al. 2005)
print "L_xotf =", L_xotf, "[erg/s]"
print "E_xotf_n2146 =", E_xotf_n2146, "[erg]"
E_xotf_total_n3628=7.7e55 # (chandra archive)
E_xotf_n3628=1.0e53 # (chandra archive)
effi_x_thrm=0.3	# (Strickland & Stevens 2000)
effi_x_mech=0.01	# (Strickland & Stevens 2000)
R_motf=2.0e3*pc # (Tsai et al. 2009)
SFR=10.0 # Msun/yr (Greve et al. 2000)
SFR=20.01 # (our 3mm conti. data)
SNrate=0.15 # yr^-1 (Tarchi et al. 2000)
SNrate=0.82 # (our 3mm conti. data)
print "SN rate =", SNrate, "[yr^-1]"
effi_mass2rad=0.001 # (Thompson et al. 2005)
as2pc_n2146=80.0
as2pc_n3628=35.0
px2as=0.2
bm2as2_n2146=3.3*2.8
bm2px=bm2as2_n2146/(px2as**2)
print bm2as2_n2146,bm2px
R_starburst_pc=700.0 # (@tau=1# Thompson et al. 2005)
# R_starburst_pc=1000.0 # (our data)
R_starburst_pc_greve=1250.0 # (Greve 2000)
R_conti_pc=2560.0/2 # (our data) (/iapetus/data/satoki_data/ngc2146/20100130.conti89GHz )
print "radius [pc],(1) R_xotf_n2146",R_xotf_n2146_pc,"R_conti",R_conti_pc
V_starburst_pc3_greve=2.0e10 # (Greve 2000)
z_starburst_pc=40.0	# (our calculation) (iapetus:/iapetus/thesis/phd/calculation/veldisp13.sh)
z_starburst_pc_greve=500.0	# (Greve 2000)
#z_starburst_pc_greve=500.0	# (Greve 2000)
z_gas_pc=12.0
tau=10.0
d_mpc=17.2	# Mpc
alpha=1.0	# (Chevalier 1985)
beta=1.0	# (Chevalier 1985)
a1=0.3          # Tsai 2009
b1=0.32         # Tsai 2009
c1=256.39               # Tsai 2009
timescale=1.0e7	# [yr] ; ourdata
v_rms_kms=11.16
v_rms=v_rms_kms*1.0e5

#def surf_den_skmt99(S_CO_JyBmMSpx,px,i_deg,D_Mpc):
def surf_den_skmt99(S_CO_JyBmMS,px,as2pc,type):
	n_bm=px/bm2px
	n_as2=px*px2as**2
	n_kpc2=n_as2*as2pc**2/1.0e6
	S_CO=S_CO_JyBmMS/1000*n_bm
	I_CO=S_CO/n_as2
	sd_Msunpc2=(5.0e2*cos_i*I_CO)*XH
	sd=sd_Msunpc2*Msun_pc2
	z_gas_pc=(v_rms**2/(2*math.pi*G*sd))/pc
	M_gas_Msun=(1.18e4*D_Mpc**2*S_CO)*XH
	M_gas=M_gas_Msun*Msun
	print '%.1e' %sd,"[g/cm2]",'%.0f' %sd_Msunpc2,"[Msun/pc2] (z =",'%.2f' %(z_gas_pc),"pc)",'%.2e' %M_gas_Msun,"[Msun]",'%.1e' %S_CO,"[Jy km/s]",'%.2f' %n_kpc2,"[kpc^2]" ,type
#	print '%.2f' %I_CO,"[Jy km/s as-2]", '%.1e' %S_CO,"[Jy km/s]",'%.0f' %n_as2,"[as2]",'%.0f' %n_bm,"[beam]",'%.1e' %sd,"[g/cm2]",'%.0f' %sd_Msunpc2,"[Msun/pc2] (z =",'%.2f' %(z_gas_pc),"pc)",'%.1e' %M_gas_Msun,"[Msun]",type
	return sd_Msunpc2,M_gas
print "------------"
print "surface density, gas mass (CO intensity)"
print "------------"
sd=surf_den_skmt99(3.730E+03,5303,as2pc_n2146,"mbbl")
sd=surf_den_skmt99(4.1472E+02,11022,as2pc_n2146,"motf")
sd=surf_den_skmt99(1.429E+03,8437,as2pc_n2146,"motf")
sd=surf_den_skmt99(7.481E+02,4683,as2pc_n2146,"motf")
sd=surf_den_skmt99(1.327E+03,6999,as2pc_n2146,"motf")
sd=surf_den_skmt99(6.669E+02,5730,as2pc_n2146,"motf")
sd=surf_den_skmt99(7.782E+02,5161,as2pc_n2146,"motf")
sd=surf_den_skmt99(6.981E+02,5343,as2pc_n2146,"motf")
sd=surf_den_skmt99(8.036E+02,4609,as2pc_n2146,"motf")
sd_motf_Msunpc2=sd[0]
sd_motf=sd_motf_Msunpc2*Msun_pc2
z=4*pc
rho_motf=sd_motf/z
M_motf=sd[1]
print sd_motf_Msunpc2, sd_motf, rho_motf
print "Chevalier 1985, rho=1.1e-25 [g cm-3]"
sd=surf_den_skmt99(1.1243E+04,38685,as2pc_n2146,"unkown")
sd=surf_den_skmt99(1.3559E+04,30802,as2pc_n2146,"45as")
sd=surf_den_skmt99(1.3182E+04,31100,as2pc_n2146,"mdsk")
sd=surf_den_skmt99(2.054E+04,18679,as2pc_n2146,"mdsk")
sd=surf_den_skmt99(2.111E+04,18040,as2pc_n2146,"mdsk")
sd=surf_den_skmt99(4.769E+04,1577,as2pc_n2146,"0.3kpc")
sd=surf_den_skmt99(3.523E+04,3877,as2pc_n2146,"0.5kpc")
sd=surf_den_skmt99(3.356E+04,6405,as2pc_n2146,"0.8kpc")
sd=surf_den_skmt99(3.652E+04,5454,as2pc_n2146,"0.8kpc")
sd=surf_den_skmt99(3.049E+04,9394,as2pc_n2146,"1.2kpc")
sd=surf_den_skmt99(3.779E+04,6813,as2pc_n2146,"SBR,diameter 30as")
sd=surf_den_skmt99(3.732E+04,6862,as2pc_n2146,"SBR,diameter 35as")
sd_gas_Msunpc2=sd[0]
sd_gas=sd_gas_Msunpc2*Msun_pc2
print "sd_gas",sd_gas
sd=surf_den_skmt99(2.431E+04,12852,as2pc_n2146,"1.2kpc")
sd=surf_den_skmt99(2.139E+04,16646,as2pc_n2146,"1.6kpc")
sd=surf_den_skmt99(1.723E+04,21464,as2pc_n2146,"1.6kpc")
sd=surf_den_skmt99(1.579E+04,25693,as2pc_n2146,"2.4kpc")
sd=surf_den_skmt99(1.381E+04,30152,as2pc_n2146,"2.4kpc")
sd=surf_den_skmt99(1.466E+04,28170,as2pc_n2146,"2.4kpc")
sd=surf_den_skmt99(1.364E+04,30695,as2pc_n2146,"2.8kpc")
sd=surf_den_skmt99(1.364E+04,30695,as2pc_n2146,"tvbox;diameter 30as")
sd=surf_den_skmt99(3.085E+04,9308,as2pc_n2146,"89GHz region; 2 sigma; r=1.4kpc")
sd=surf_den_skmt99(3.095E+04,9239,as2pc_n2146,"89GHz region; 2 sigma; r=1.4kpc")
sd=surf_den_skmt99(3.252E+04,8479,as2pc_n2146,"89GHz region better; 2 sigma; r=1.4kpc")
sd=surf_den_skmt99(4.03E+04,5527,as2pc_n2146,"89GHz region; 4 sigma; r=1.2kpc(?)")
sd=surf_den_skmt99(5.035E+04,2272,as2pc_n2146,"89GHz region; 8 sigma; r=0.8kpc(?)")
sd=surf_den_skmt99(6.984E+04,176,as2pc_n2146,"0.2kpc")
sd=surf_den_skmt99(1.027E+04,42672,as2pc_n2146,"total molecular gas; 0.1 sigma")
sd=surf_den_skmt99(1.370E+04,31200,as2pc_n2146,"total molecular gas; 4 sigma")
sd=surf_den_skmt99(5.055E+04,2338,as2pc_n3628,"n3628 ; 88GHz region")
sd=surf_den_skmt99(3.400E+04,4564,as2pc_n3628,"n3628 89GHz region convl n2146 88GHz; 2 sigma; r=0.26kpc(?)")
sd=surf_den_skmt99(1.282E+04,27917,35,"n3628 total molecular gas; 2 sigma")
sd=surf_den_skmt99(8.639E+03,43088,35,"n3628 total molecular gas; 0.5 sigma")
#sd=surf_den_skmt99(4.6646E-03*20,157212,"unknown")
#sd=surf_den_skmt99(1.746E+00,35560,"xotf")
#sd=surf_den_skmt99(1.621E+00,43849,"xotf")
#sd=surf_den_skmt99(2.288E+00,8958,"xotf")
#sd=surf_den_skmt99(2.226E+00,14394,"xotf")
#sd_xotf_Msunpc2=sd[0]
#sd_xotf=sd_xotf_Msunpc2*Msun_pc2
# ------------
# ?
#M_xotf_n2146=sd[1]
#print "M_xotf_n2146",M_xotf_n2146
#sd_xotf=sd_xotf_Msunpc2*Msun_pc2
#print "sd_xotf=",sd_xotf#,"sd_xotf_Msunpc2=",sd_xotf_Msunpc2
# ?
# ------------
sd_xotf=sd_motf*(n_xotf_n2146/n_mol)*(M_xotf_n2146/M_motf)
sd_xotf_Msunpc2=sd_xotf*Msun_pc2
print "sd_xotf=",sd_xotf#,"sd_xotf_Msunpc2=",sd_xotf_Msunpc2

def surf_den_dyn(r_kpc):
	v_kms=r_kpc*c1/(r_kpc**a1+r_kpc**(1-b1))/sin_i
	v=v_kms*1.0e5
	r=r_kpc*kpc
	r_pc=r_kpc*1000
	m_dyn=r*v**2/G      # Orange book p.958
	m_dyn_Msun=m_dyn/Msun
	sd_dyn=m_dyn/(math.pi*r**2)
	sd_dyn_Msunpc2=m_dyn_Msun/(math.pi*r_pc**2)
#	sd_dyn_Msunpc2=sd_dyn/Msun_pc2
#	sd_gas=0.075
#	z_gas_pc=(v_rms**2/(2*math.pi*G*sd_gas))/pc
	z_dyn_pc=(v_rms**2/(2*math.pi*G*sd_dyn))/pc
	print '%.2f' %(sd_dyn),"[g/cm2]",'%.0f' %(sd_dyn_Msunpc2),"[Msun/pc2] (z =",'%.2f' %(z_dyn_pc),"pc)",'%.2f' %v_kms,"[km/s]", '%.1e' %(m_dyn_Msun),"[Msun]", r_kpc,"kpc" 
#	print '%.2f' %(sd_dyn),"[g/cm2]",'%.0f' %(sd_dyn_Msunpc2),"[Msun/pc2] (r <",r_kpc,"kpc ; z = (gas)",'%.2f' %(z_gas_pc),"pc; (dyn)",'%.2f' %(z_dyn_pc),"pc)",'%.2f' %v_kms,"[km/s]", '%.1e' %(m_dyn_Msun),"[Msun]"
	return sd_dyn_Msunpc2
print "------------"
print "surface density, dynamical mass (rotation curve)"
print "------------"
sd05=surf_den_dyn(0.3)
sd05=surf_den_dyn(0.5)
sd08=surf_den_dyn(0.8)
sd10=surf_den_dyn(1.0)
sd12=surf_den_dyn(1.2)
sd_dyn=sd12
sd15=surf_den_dyn(1.5)
sd24=surf_den_dyn(2.4)
sd28=surf_den_dyn(2.8)
sd30=surf_den_dyn(3.0)
sd32=surf_den_dyn(3.2)
sd40=surf_den_dyn(4.0)
sd50=surf_den_dyn(5.0)
#sd35=surf_den_dyn(3.5)
#sd50=surf_den_dyn(5)
#sd100=surf_den_dyn(10)
def surf_den_rv(r_kpc,v_kms,i_deg,name):
	sin_i=math.sin(i_deg/180.0*math.pi)
	r=r_kpc*kpc/sin_i
	r_pc=r_kpc*1000
	v=v_kms*1.0e5
	m=r*v**2/G
	m_Msun=m/Msun
	sd=m_Msun/(math.pi*r_pc**2)
	print '%.0f' %(sd),"[Msun/pc2] (r <",r_kpc,"kpc)",'%.2f' %v_kms,"[km/s]", '%.1e' %(m_Msun),"[Msun]",name
	return sd
print "------------"
print "surface density, other galaxies (rotation curve)"
print "------------"
sd=surf_den_rv(1,100,90,"?")
sd=surf_den_rv(1,136,90,"?")
sd=surf_den_rv(2,100,90,"?")
sd=surf_den_rv(2,50,90,"?")
sd=surf_den_rv(3,200,90,"?")
sd=surf_den_rv(4,200,90,"?")
sd=surf_den_rv(5,100,77,"M31")
sd=surf_den_rv(1,50,77,"M31")
sd=surf_den_rv(1,50,56,"M33")
# http://w3.iihe.ac.be/icecube/3_Activities/1_WIMPs%20Analysis/
sd=surf_den_rv(2,50,90,"?")
sd=surf_den_rv(10,150,70,"N3198")
sd=surf_den_rv(5,150,70,"N3198")
sd=surf_den_rv(2,100,70,"N3198")
# http://bustard.phys.nd.edu/Phys171/lectures/dm.html
sd=surf_den_rv(15,300,35,"N4378")
sd=surf_den_rv(4,120,74,"N6503")
# http://www.nicolascretton.ch/Astronomy/index_The_subject.html
# --- gravitational pressure (Gunn & Gott 1972) -------	#


def mass(S_Jy_ms,lamb_cm,px,D_Mpc,region):
	bm_as2=px*px2as**2
	T=13.6*(lamb_cm*10)**2*bm_as2*S_Jy_ms/1000
	colden=T*1.4e20
	surfden=colden*m_p/Msun_pc2
	D=D_Mpc*1.0e6*pc
	A_cm2=bm_as2*(D/rad2as)**2
	A_pc2=A_cm2/pc**2
	m=surfden*A_pc2
	print '%.1e' %surfden,"[Msun/pc2]", '%.1e' %m,"[Msun]",region
	return surfden
#ass(2.431E+04,0.26,128520,17.2,"1.2kpc")
#mass(1.364E+04,0.26,306950,17.2,"1.2kpc")


print "------------"
print "calculation results"
print "------------"
print "+[ grav P = 2*pi*G*(surf_den_xry)*(surf_den_dynamical_mass) ]+"
def p_grav(sd,type):
	gravP=2*math.pi*G*sd*sd_dyn*Msun_pc2
	print " o", type, "grav P:", '%.1e' %(gravP)
	return gravP

p_grav_motf=p_grav(sd_motf,"mol. outflow | ngc2146")
p_grav_xotf=p_grav(sd_xotf, "xray outflow | ngc2146")
# unit checked

# --- ram pressure (Gunn & Gott 1972) -----------------	#
print "------------"
print "+[ ram P = rho*(relative velocity)^2 ]+"
def v_esc(M_Msun,R_kpc):
	M=M_Msun*Msun
	R=R_kpc*1.0e3*pc
	v=math.sqrt(2*G*M/R)/1.0e5
	print "escape velocity",v,"[km/s]"
	return v
#v_2kpc=v_esc(8.67e10,2)
#v_1kpc=v_esc(8.67e10,1)
#E_bnd_ion_particle=(E_bnd_ev+E_ion_ev)*ev
#E_bnd_ion_mass=E_bnd_ion_particle*N_A*M_xotf_n2146_g
def ramP(E_xotf,v_motf_kms,M_xotf,rho_xotf,type1,effi_x1,type2,effi_x2):
	print "   ", type1, effi_x1
	print "   ", type2, effi_x2
	effi_x=effi_x1*effi_x2
	E_ttl=E_xotf/effi_x
	print "    total Energy =",'%.2f' %(E_ttl), "[erg]"
	E_mech=E_ttl*0.1
#	E_mech=E_ttl*(1-effi_x)
	v_xry_kms=math.sqrt(E_mech*2/M_xotf)/1.0e5
	print "    v_xry = ",  '%.2f' %(v_xry_kms), "[km/s]"
	v_rel_kms=v_xry_kms-v_motf_kms
	v_rel=v_rel_kms*1.0e5
	p=rho_xotf*v_rel**2
#	p=rho_motf*v_rel**2
#	p=rho_mol*v_rel**2
	p_K=p/k_B
	print "    E_mech = ",  '%.2f' %(E_mech), "[erg]"
	print "    v_rel = ",  '%.2f' %(v_rel_kms), "[km/s]"
	print " o ram P: ", '%.1e' %(p),"[dyne cm^-2]"
	print " o ram P: ", '%.1e' %(p_K), "[K cm^-3]"
	return p
# unit checked
print "------------"
type2="Lx increasing factor ="
print "------------"
print "NGC 2146: the total energy released by SNe and stellar winds (doesn't include the K.E)"
#p_ram1=ramP(E_xotf_n2146,v_motf_kms_n2146,M_xotf_n2146,rho_xotf_n2146,"thermalization efficiency (lower) =",0.1,type2,1)
p_ram1=ramP(E_xotf_n2146,v_motf_kms_n2146,M_xotf_n2146,rho_xotf_n2146,"thermalization efficiency =",effi_x_thrm,type2,1)
p_ram1=ramP(E_xotf_n2146,v_motf_kms_n2146,M_xotf_n2146,rho_xotf_n2146,"thermalization efficiency =",0.1,type2,1)
p_ram1=ramP(E_xotf_n2146,v_motf_kms_n2146,M_xotf_n2146,rho_xotf_n2146,"thermalization efficiency =",1.0,type2,1)
#p_ram1=ramP(E_xotf_n2146,v_motf_kms_n2146,M_xotf_n2146,rho_xotf_n2146,"thermalization efficiency =",0.5,type2,1)
#p_ram1=ramP(E_xotf_n2146,v_motf_kms_n2146,M_xotf_n2146,rho_xotf_n2146,"thermalization efficiency (upper) =",1,type2,1)
print "------------"
print "NGC 2146: radiating the mechanical energy supplied by the starburst"
p_ram1=ramP(E_xotf_n2146,v_motf_kms_n2146,M_xotf_n2146,rho_xotf_n2146,"starburst energy injection rate (thin-disk) =",0.01,type2,10)
print "------------"
print "NGC 3628: the total energy released by SNe and stellar winds (doesn't include the K.E)"
#p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"thermalization efficiency (lower) =",0.1,type2,1)
p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"thermalization efficiency =",effi_x_thrm,type2,1)
p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"thermalization efficiency =",0.1,type2,1)
p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"thermalization efficiency =",1.0,type2,1)
#p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"thermalization efficiency =",0.5,type2,1)
#p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"thermalization efficiency (upper) =",1,type2,1)
print "------------"
print "NGC 3628: radiating the mechanical energy supplied by the starburst"
p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"starburst energy injection rate (thin-disk) =",0.01,type2,10)
p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"starburst energy injection rate (thick-disk, lower) =",0.05,type2,3)
p_ram2=ramP(E_xotf_n3628,v_motf_kms_n3628,M_xotf_n3628,rho_xotf_n3628,"starburst energy injection rate (thick-disk, upper) =",0.2,type2,3)

# --- SN explosions pressure effect on hot ISM (Thompson et al 2005) --	#
print "------------"
print "+[ shock P = 10^-12*E_xry^(17/14)*n_mol^(-4/7)*SNrate/Vol ]+"
def A_pc2(R):
	A=math.pi*R**2
#	print "Starburst Area = ", '%.1e' %(A) , "[pc^2]"
	return A

def V_pc3(R,z):
	V=math.pi*R**2*z
	return V
# SNrate_V=SNrate/V_starburst
V_conti=V_pc3(R_conti_pc,z_gas_pc)
#V_conti=V_pc3(R_conti_pc,z_starburst_pc)
V_greve1=V_pc3(R_starburst_pc_greve,z_starburst_pc_greve)
V_greve2=2.0e10 # (Greve 2000)
E_init_n2146=E_xotf_n2146
n_ambi=n_mol

def p_SNhot(V,E_init,type):
	rate_V=SNrate/V
	P=1.0e-12*(E_init/1.0e51)**(17.0/14)*(n_ambi/0.01)**(-4.0/7)*(rate_V/1.0e-13) # [erg cm^-3]
	print "    data from", type
	print "    starburst Volume = ", '%.1e' %(V), "[pc^3]"
	print " o SN shock-heated P: ",  '%.1e' %(P)
#	print "SN explosion P (shock-heated hot ISM): ", P
	return P
# E_init [erg]
# n_ambi [cm^-3]
# SNrate_V [yr^-1 pc^-3]
# SNrate_V=SNrateate per volume
p_SNhot_conti=p_SNhot(V_conti,E_init_n2146,"89GHz Continuum")
p_SNhot_greve1=p_SNhot(V_greve1,E_init_n2146,"Greve 2000 (1)")
p_SNhot_greve2=p_SNhot(V_greve2,E_init_n2146,"Greve 2000 (2)")

# unit checked

# --- thermal pressure --------------------------------	#
print "------------"
print "+[ thermal P = n*k*T ]+"
p_thm_mol=n_mol*k_B*T_mol
p1=1000*k_B*100
p2=100*k_B*10
print "pppp",p1,p2
p_thm_xotf=2*n_xotf_n2146*kT_xotf
p_thm_xotf_inui=4.9e-12*fill**(-0.5)
print " o molecular gas thermal P: ", p_thm_mol
print " o ionized gas thermal P: ",  '%.1e' %(p_thm_xotf)
print " o ionized gas thermal P (Inui): ", p_thm_xotf_inui
# unit checked

# --- radiation pressure (Thompson et al 2005) --------	#
print "------------"
print "+[ radiation P = effic*SFR/Area*c ]+"
# SFR_A=SFR/(A_starburst)
A_starburst=A_pc2(R_conti_pc)*pc**2
SFR_A=SFR/(A_starburst)
# when tau << 1
p_rad_thin=c*effi_mass2rad*SFR_A
# when tau >= 1
p_rad_thick=c*effi_mass2rad*SFR_A*(1.0/2)*tau
#print " o optically thin radiation P: ",  '%.1e' %(p_rad_thin)
print " o optically thick radiation P: ",  '%.1e' %(p_rad_thick)
# unit checked

# --- SN explosion pressure affect on cold ISM (Thompson et al 2005) --	#
print "------------"
print "+[ SN explosion P = 5*n_mol^(-1/4)*E_xry^(13/14)*P_rad ]+"
# E_init=E_xotf_n2146
# n_ambi=n_mol
p_SN_cold=5*(n_ambi/1.0)**(-1.0/4)*(E_init_n2146/1.0e51)**(13.0/14)*p_rad_thick
print " o SN explosion P (cold ISM): ",  '%.1e' %(p_SN_cold)
print "------------"
f1=0.1
f2=0.01
n_plm1=6.86e-3*f1**-0.5
n_plm2=6.86e-3*f2**-0.5
rho_plm1=n_plm1*m_p
rho_plm2=n_plm2*m_p
v_plm=340.0e5
gg=980.0
h=2.0*kpc
p_plm_th1=1.0e-11
p_plm_th2=3.2e-11
p_plm_ke1=0.5*rho_plm1*v_plm**2
p_plm_ke2=0.5*rho_plm2*v_plm**2
p_plm_total1=p_plm_th1+p_plm_ke1
p_plm_total2=p_plm_th2+p_plm_ke2
p_plm_pe1=rho_plm1*gg*h
p_plm_pe2=rho_plm2*gg*h
print "p_plm_total = p_plm_th + p_plm_ke"
print "p_plm_total =",p_plm_total1, p_plm_total2
print "p_plm_th =",p_plm_th1,p_plm_th2
print "p_plm_ke =",p_plm_ke1,p_plm_ke2
#print "p_plm_pe =",p_plm_pe
print "------------"
n_mol1=100.0
n_mol2=1000.0
rho_mol1=n_mol1*m_p
rho_mol2=n_mol2*m_p
T_mol1=10.0
T_mol2=100.0
v_mol=200.0e5
p_mol_th1=n_mol1*k_B*T_mol1
p_mol_th2=n_mol2*k_B*T_mol2
p_mol_ke1=0.5*n_mol1*m_p*v_mol**2
p_mol_ke2=0.5*n_mol2*m_p*v_mol**2
p_mol_total1=p_mol_th1+p_mol_ke1
p_mol_total2=p_mol_th2+p_mol_ke2
p_mol_pe1=rho_mol1*gg*h
p_mol_pe2=rho_mol2*gg*h
print "p_mol_total = p_mol_th + p_mol_ke"
print "p_mol_total =",p_mol_total1,p_mol_total2
print "p_mol_th =",p_mol_th1,p_mol_th2
print "p_mol_ke =",p_mol_ke1,p_mol_ke2
#print "p_mol_pe =",p_mol_pe
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

