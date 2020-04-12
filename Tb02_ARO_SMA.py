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
c_cms=2.99792458e10
HCN_1_0_lamda=c_cms/88.63e9
ff_cont_n2146_lamda=c_cms/88.644e9
ff_cont_n3628_lamda=c_cms/94.667e9
Kb=1.38e-16	# [erg/K]
Jy=1.0e-23	# [erg/s/cm2/Hz]
mJy=Jy/1000	# [erg/s/cm2/Hz]
#  --- parameter -------------------------------	#
n3628_theta_maj_as=3.01
n3628_theta_min_as=2.36
n2146_theta_maj_as=3.3
n2146_theta_min_as=2.8


# =============================================================
# calculate for ARO and SMA
# =============================================================
# http://www.nro.nao.ac.jp/~nma/status/status-e.html#sensitivity
eta_a_nma110=0.6	# aperture efficiency (value from NMA)
eta_q_nma110=0.85	# quantization efficiency of the correlator (value from NMA)
# http://iopscience.iop.org/1538-4357/616/1/L1/fulltext/18511.text.html
eta_a_sma230=0.72	# aperture efficiency (value from SMA)
eta_a_sma345=0.72	# aperture efficiency (value from SMA)
eta_misc_sma=0.88	# quantization efficiency of the correlator (value from NMA)
eta_a_12m70=0.52	# aperture efficiency (value from 12m)
eta_a_12m115=0.49	# aperture efficiency (value from 12m)

print "======================================================="
print "ARO 12m vs. SMA"
print "------------"
print "Imaging sensitivity"
print "------------"
# S_mJy=(sqrt(2)*Kb*Tsys)/(Ap_m*eta_a*eta_q*sqrt(n_baseline*BW*t_integ))
#def S_mJy(Tsys, dish_radius_m,n_antenna, BW_MHz, t_integ_hr,type):
def S_mJy(Tsys, dish_diameter_m, eta_a, eta_q, n_baseline, BW_MHz, t_integ_hr,type):
	Ap_m2=(dish_diameter_m/2)**2*math.pi
	Ap_cm2=Ap_m2*10000
#	n_baseline=n_antenna*(n_antenna-1)/2
	BW=BW_MHz*1.0e6
	t_integ=t_integ_hr*3600.0
	S_mJy=(math.sqrt(2)*Kb*Tsys)/(Ap_cm2*eta_a*eta_q*math.sqrt(n_baseline*BW*t_integ))/mJy
	print "Tsys = ", '%.0f' %Tsys,"[K] | Aperture = ", '%.2f' %Ap_m2, "[m^2] | # of baseline = " ,'%.0f' %n_baseline,"| BW = ", '%.1f' %BW_MHz,"[MHz] | ", '%.2f' %t_integ_hr, "[hr] | S_mJy = ", '%.2f' %S_mJy, "[mJy] | ", type
	return S_mJy
print "------------"
#S_mJy(Tsys, dish_diameter_m,n_baseline, BW_MHz, t_integ_hr,type):
S_mJy(300,6,eta_a_sma230,eta_misc_sma,28,4092,5.35,"this is test for SMA @ 110 GHz")
S_mJy(300,6,eta_a_sma230,eta_misc_sma,28,4092,5.35,"this is test for SMA @ 110 GHz")
S_mJy(300,6,eta_a_sma230,eta_misc_sma,28,4092,5.35,"this is test for SMA @ 110 GHz")
S_mJy(300,12,eta_a_12m115,eta_q_nma110,1,4092,5.35,"this is test for 12M @ 115 GHz")
S_mJy(270,12,eta_a_12m115,eta_q_nma110,1,4092,5.35,"this is test for 12M @ 115 GHz")
S_mJy(270,12,eta_a_12m115,eta_q_nma110,1,1024,10,"this is test for 12M @ 115 GHz")
S_mJy(270,12,eta_a_12m115,eta_q_nma110,1,1024,20,"this is test for 12M @ 115 GHz")
S_mJy(270,12,eta_a_12m115,eta_q_nma110,1,1024,30,"this is test for 12M @ 115 GHz")
S_mJy(270,12,eta_a_12m115,eta_q_nma110,1,600,4,"this is test for 12M @ 115 GHz")
#S_mJy(Tsys, dish_diameter_m,n_baseline, BW_MHz, t_integ_hr,type):
print "------------"


print "------------"
print "Conversion between flux density (S) and brightness temperature (Tb)"
print "------------"
#Tb_mK=(lambda^2*S_mJy)/(2*Kb*solid_angle_as2)
#solid_angle_as2=(math.pi*theta_maj*theta_min)/(4*ln(2))
def Tb_mK(lambda_mm, S_mJy, theta_maj_as, theta_min_as,type):
#	lambda_cm=lambda_mm*0.1
#	S_erg=S_mJy*mJy
#	solid_angle=(math.pi*theta_maj_as*theta_min_as)/(4*math.log(2))
#	Tb_mK=(lambda_cm**2)/(2*Kb*solid_angle)*S_erg*1000
	Tb_mK=13.6*lambda_mm**2*S_mJy/(theta_maj_as*theta_min_as)
        print "lambda = ",'%.0f' %lambda_mm, "[mm] | S_mJy = ", '%.2f' %S_mJy,"[mJy] | beam size =", '%.1f' %theta_maj_as,"x",'%.1f' %theta_min_as,"[arcs2] | Tb = ", '%.2f' %Tb_mK ,"[mK] | ", type
#	print "solid angle =",'%.2f' %solid_angle,"[arc^2]" # , S =",'%.2e' %S_mJy_bm,"[mJy/bm], Tb =", '%.4e' %Tb,"[mK] |", type
        return Tb_mK
print "------------"
#Tb_mK(lambda_mm, S_mJy, theta_maj_as, theta_min_as,type):
Tb_mK(1,1,1,1,"this is test")
Tb_mK(1,2, 3,3,"this is test")
Tb_mK(2,2, 3,3,"this is test")
Tb_mK(3,2, 3,3,"this is test")
Tb_mK(3,0.6, 5,5,"this is test")
Tb_mK(2,0.6, 5,5,"this is test")
#Tb_mK(lambda_mm, S_mJy, theta_maj_as, theta_min_as,type):
print "------------"
print "======================================================="

# --- reference -------------------------------	#
# Sakamoto et al. 1995, AJ, 110, 2075
# http://www.nro.nao.ac.jp/~nma/status/status-e.html#sensitivity


exit

