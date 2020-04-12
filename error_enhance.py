#!/usr/bin/env python
# error propagation

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
Lsun=3.98e33	# [erg/s]
Msun=1.99e33	# solar mass
k_B=1.38e-16
N_A=6.02e23	# Avogadro constant
c=2.99e10	# [cm/s]
yr=365*86400	# [sec]
lyr=c*yr	# [cm]
pc=3.26*lyr	# [cm]
kpc=1000*pc	# [cm]
mpc=1.0e6*pc	# [cm]
Jy=1.0e-23	# [ergs cm-2 s-1 Hz-1]
ev=1.6e-12	# [erg]
m_p=1.67e-24	# [g]
m_e=9.11e-28	# [g]


# --- IMF -----------------------------------------	#
def err_enhance(N_SN, t_exp, t_OV, N_OV, err_N_SN, err_t_exp, err_Q_Lyc, err_t_OV,  type):
	err=math.sqrt(err_N_SN**2+err_t_exp**2+err_Q_Lyc**2+err_t_OV**2)
	enh=N_OV*t_exp/(N_SN*t_OV)
	enh1=enh*(1-err)
	enh2=enh*(1+err)
	print '%.1f' %enh, "+/-", '%.1f' %(err*100), "% (",'%.1f' %enh1, "-",'%.1f' %enh2, ")", type
	return enh
print "-----------------------------------------------"
t_15_20M=(11.5*35+19*5.6)/(19+35)
t_15_25M=(11.5*35+19*5.6+3.2*12)/(19+35+12)
t_15_30M=(11.5*35+19*5.6+3.2*12+2.0*8)/(19+35+12+8)
err_enhance((1.7e5+4.0e5)/2,15.0,t_15_20M,3.3e5,0.4,0.33, 0.1,0.35,"NGC2146 O=15-20M")
err_enhance((1.7e5+4.0e5)/2,15.0,t_15_25M,3.3e5,0.4,0.33, 0.1,0.56,"NGC2146 O=15-25M")
err_enhance((1.7e5+4.0e5)/2,15.0,t_15_30M,3.3e5,0.4,0.33, 0.1,0.77,"NGC2146 O=15-30M")




exit
