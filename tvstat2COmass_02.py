#!/usr/bin/env python
# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
pc=3.26*c*365*86400
kpc=pc*1.0e3
mpc=pc*1.0e6
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
#  --- parameter ------------------------------	#
D_Mpc_N2146=17.2
D_Mpc_N3628=10.04
bmaj_N2146=3.4
bmin_N2146=2.8
bmaj_N3628=3.01
bmin_N3628=2.36
px2as=0.2
#  --- readfile ------------------------------	#
f=open('lst_all.txt','r')
for line in f.read():
#	f.readline()
	mean=float(f.read(10))
	f.read(1)
	rms=float(f.read(10))
	f.read(1)
	pix=float(f.read(8))
	f.read(1)
	flux=float(f.read(10))
	f.read(1)
	S=mean*5.2*1000
	mass=COmass(S,pix,0.26,bmaj_N3628,bmin_N3628,px2as,D_Mpc_N3628,"NGC 3628 ; tvstat ; total mass")

f.close()
#  --- function ------------------------------	#
#  -------------------------------------------	#
def I_JyAs2(S_JyBm,px,bmaj,bmin,px2as,type):
	bm2as2=bmaj*bmin
	bm2px=bm2as2/px2as**2
	n_bm=px/bm2px
	n_as=px*px2as**2
	S_Jy=S_JyBm*n_bm
	I_JyAs2=S_Jy/n_as
	print "----------------------------------------"
	print type
	print "S_JyBm = ",'%.2e' %S_JyBm,"[Jy/Bm] ; over ",px,"[pixels]" 
	print "bmaj = ", bmaj, "[as] ; bmin = ",bmin,  "[as] ; beam = ", '%.1f' %bm2as2,"[as2] = ",bm2px,"[px]"
	print "# of bm = ", '%.1f' %n_bm," ; # of as = ", '%.1f' %n_as
	print "S = ",'%.3e' %S_Jy,"[Jy] ; I = ",'%.2e' %I_JyAs2,"[Jy/as2]"
	return I_JyAs2

def COmass(S_JyBmMS,px,lamb_cm,bmaj,bmin,px2as,D_Mpc,galaxy):
	bm2as2=bmaj*bmin
	bm2px=bm2as2/px2as**2
	n_bm=px/bm2px
	S_JyMS=S_JyBmMS*n_bm
	T=13.6*(lamb_cm*10)**2/bm2as2*S_JyMS/1000
	colden=T*1.4e20
	surfden=colden*m_p/Msun_pc2
	D=D_Mpc*mpc
	A_cm2=bm2as2*(D/rad2as)**2
	A_pc2=A_cm2/pc**2
	m=surfden*A_pc2
	print '%.3e' %T,"[K]", '%.0f' %n_bm, "[bm]",'%.3e' %m,"[Msun]",galaxy
	return surfden


def COmass2(S_JyBmMS,px,bmaj,bmin,px2as,D_Mpc,galaxy):
	mass=S_JyBmMS/1000*px/(bmaj*bmin)*px2as**2*1.8e4*D_Mpc**2*1.4e20/3.0e20#*1.36
	print '%.3e' %mass,"[Msun]",galaxy
	return mass



#  -------------------------------------------	#
