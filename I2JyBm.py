#!/usr/bin/env python
# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
c=3.0e10 # light speed
pc=3.26*c*365*86400
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
def I_JyAs2(S_JyBm,px,bmaj,bmin,px2as,type):
	bm2as=bmaj*bmin
	bm2px=bm2as/px2as**2
	n_bm=px/bm2px
	n_as=px*px2as**2
	S_Jy=S_JyBm*n_bm
	I_JyAs2=S_Jy/n_as
	print "----------------------------------------"
	print type
	print "S_JyBm = ",'%.2e' %S_JyBm,"[Jy/Bm] ; over ",px,"[pixels]" 
	print "bmaj = ", bmaj, "[as] ; bmin = ",bmin,  "[as] ; beam = ", '%.1f' %bm2as,"[as2] = ",bm2px,"[px]"
	print "number of bm = ", '%.1f' %n_bm," ; number of as = ", '%.1f' %n_as
	print "S = ",'%.3e' %S_Jy,"[Jy] ; I = ",'%.2e' %I_JyAs2,"[Jy/as2]"
	return I_JyAs2

print "----------------------------------------"
I_n2146=I_JyAs2(2.866E-03,2959,5.24,3.74,0.4,"NGC 2146 ; tvstat")
I_n2146=I_JyAs2(2.645E-03,3150,5.24,3.74,0.4,"NGC 2146 ; imstat; rot 43d")
I_n3628=I_JyAs2(1.678E-03,1488,2.5,1.9,0.25,"NGC 3628 ; tvstat")
I_n3628=I_JyAs2(8.534E-04,3392,2.5,1.9,0.25,"NGC 3628 ; imstat")
I_m82=I_JyAs2(5.607E-03,5842,2.3,1.9,0.25,"M82 High Resolution ; tvstat")
I_m82=I_JyAs2(3.954E-03,8696,2.3,1.9,0.25,"M82 High Resolution ; tvstat")
I_m82=I_JyAs2(1.036E-02,9703,3.7,3.3,0.25,"M82 Low Resolution ; tvstat")
I_m82=I_JyAs2(1.033E-02,9729,3.7,3.3,0.25,"M82 Low Resolution ; tvstat")
I_m82=I_JyAs2(1.191E-02,7509,2.5,1.9,0.25,"M82 Low Resolution; imstat")
print "----------------------------------------"
I_n3628=I_JyAs2(8.208E+03/(141*5.2e3),4542,3.01,2.36,0.2,"NGC 3628 ; tvsat; total mass")
I_n3628=I_JyAs2(8.177E+0/(141*5.2e3),4560,3.01,2.36,0.2,"NGC 3628 ; tvsat; total mass")
I_n3628=I_JyAs2(8.168E+03/(141*5.2e3),45658,3.01,2.36,0.2,"NGC 3628 ; tvsat; total mass")
print "----------------------------------------"
I_n2146=I_JyAs2(3.760E-03,8401,5.24,3.74,0.2,"NGC 2146 ; 3mm conti.;bm=5x4;tvstat")
I_n3628=I_JyAs2(3.901E-03,4699,5.24,3.74,0.2,"NGC 3628 ; 3mm conti.;bm=5x4;tvstat")
print "----------------------------------------"
I_n2146=I_JyAs2(2.197E-03,6381,3.3,2.8,0.2,"NGC 2146(1) ; 3mm conti.;bm=3x3;tvstat")
I_n2146=I_JyAs2(1.352E-03,10502,3.3,2.8,0.2,"NGC 2146(2) ; 3mm conti.;bm=3x3;tvstat")
I_n3628=I_JyAs2(1.031E-03,6918,3.01,2.35,0.2,"NGC 3628(1) ; 3mm conti.;bm=3x2;tvstat")
I_n3628=I_JyAs2(1.298E-03,5252,3.01,2.35,0.2,"NGC 3628(1) ; 3mm conti.;bm=3x2;tvstat")
print "----------------------------------------"
