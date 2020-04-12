#!/usr/bin/env python
# Initial Mass Function

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
def imf(b,N_known,M_known,M_up,M_low,type):
	b1=b+1
	a=N_known*b1/(M_known**b1-M_up**b1)
	N=a/b1*(M_low**b1-M_up**b1)
	print "a =",'%.1f' %a, "| index =", '%.2f' %b,\
	"| N ( M =",'%.0f' %M_known,"-",'%.0f' %M_up,") =", '%.1f' %N_known, \
	"| N_ttl ( M =",'%.1f' %M_low,"-",'%.0f' %M_up,") =", '%.2f' %N, type
	return N
print "-----------------------------------------------"
print "Salpeter IMF: dN/dM=a*M**-2.35"
print "-----------------------------------------------"
# imf(b,N_known,M_known,M_up,M_low,type)
#imf_salpeter=imf(-2.35,15,5,10,0.1,"| Salpeter")
#imf_salpeter=imf(-2.35,3,5,10,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,10,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,20,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,30,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,0.1,"| Salpeter")
imf_salpeter=imf(-1.35,1,5,100,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,30,0.5,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,20,0.5,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,10,0.5,"| Salpeter")
#imf_salpeter=imf(-2.35,3,5,10,0.5,"| Salpeter")
#imf_salpeter=imf(-2.35,15,5,10,0.5,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,4,"| Salpeter")
imf_salpeter=imf(-2.5,1,5,100,1,"| test")
imf_salpeter=imf(-2.35,1,10,100,1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,20,1,"| Salpeter")
#imf_salpeter=imf(-1.35,1,5,100,1,"| test")
#imf_salpeter=imf(-1.35,1,5,100,0.1,"| test")
#imf_salpeter=imf(-2,1,5,100,1,"| test")
#imf_salpeter=imf(-2,1,5,100,0.1,"| test")
#imf_salpeter=imf(-3,1,5,100,1,"| test")
#imf_salpeter=imf(-3,1,5,100,0.1,"| test")
# imf(b,N_known,M_known,M_up,M_low,type)
imf_salpeter=imf(-2.35,1,10,100,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,0.6,10,100,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,100,15,100,20,"| Salpeter")
imf_salpeter=imf(-2.35,100,15,100,25,"| Salpeter")
imf_salpeter=imf(-2.35,100,15,100,30,"| Salpeter")
imf_salpeter=imf(-2.35,100,15,100,35,"| Salpeter")
imf_salpeter=imf(-2.35,100,15,100,40,"| Salpeter")
imf_salpeter=imf(-2.5,1,8,100,5,"| test")





exit
