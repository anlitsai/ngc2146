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
def imf(a,M_OB,m_OB,m_top,m_low,type):
	a2=a+2
	b=M_OB/(m_top**a2-m_OB**a2)
#	c=M_OB/(m_top**(-a1)-m_OB**(-a1))
	M_tot=b*(m_top**a2-m_low**a2)
#	M_tot=c*(m_top**(-a1)-m_low**(-a1))
	print "b =",'%.2f' %b, "| index =", '%.2f' %a,\
	"| M ( m =",'%.0f' %m_OB,"-",'%.0f' %m_top,") =", '%.1f' %M_OB, \
	"[Msun/yr] | M_tot ( m =",'%.2f' %m_low,"-",'%.0f' %m_top,") =",\
	 '%.2f' %M_tot, "[Msun/yr]", type
	return M_tot
print "-----------------------------------------------"
print "Salpeter IMF: dN = b*d(m**-a) = -a*b*m**(-a-1)dm"
print "Salpeter IMF: dM = m*dN = -a*b*m**(-a)dm = -a*b/(-a-1)* dm**(-a+1) = c*dm**(-a+1)"
print "-----------------------------------------------"
# imf(b,N_known,M_known,M_up,M_low,type)
#imf_salpeter=imf(-2.35,15,5,10,0.1,"| Salpeter")
#imf_salpeter=imf(-2.35,3,5,10,0.1,"| Salpeter")
#imf_salpeter=imf(-2.35,1,5,10,0.1,"| Salpeter")
#imf_salpeter=imf(-2.35,1,5,20,0.1,"| Salpeter")
#imf_salpeter=imf(-2.35,1,5,30,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,10,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,2,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,0.1,"| Salpeter")
imf_salpeter=imf(-1.35,1,5,100,0.1,"| Salpeter")
#imf_salpeter=imf(-2.35,1,5,30,0.5,"| Salpeter")
#imf_salpeter=imf(-2.35,1,5,20,0.5,"| Salpeter")
#imf_salpeter=imf(-2.35,1,5,10,0.5,"| Salpeter")
#imf_salpeter=imf(-2.35,3,5,10,0.5,"| Salpeter")
#imf_salpeter=imf(-2.35,15,5,10,0.5,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,1,"| Salpeter")
imf_salpeter=imf(-2.35,1,5,100,4,"| Salpeter")
imf_salpeter=imf(-2.5,1,5,100,1,"| test")
imf_salpeter=imf(-2.5,1,5,100,0.1,"| test")
imf_salpeter=imf(-2.35,1,10,100,1,"| Salpeter")
#imf_salpeter=imf(-2.35,1,5,20,1,"| Salpeter")
#imf_salpeter=imf(-1.35,1,5,100,1,"| test")
#imf_salpeter=imf(-1.35,1,5,100,0.1,"| test")
#imf_salpeter=imf(-2,1,5,100,1,"| test")
#imf_salpeter=imf(-2,1,5,100,0.1,"| test")
#imf_salpeter=imf(-3,1,5,100,1,"| test")
#imf_salpeter=imf(-3,1,5,100,0.1,"| test")
# imf(b,N_known,M_known,M_up,M_low,type)
imf_salpeter=imf(-2.35,1,10,100,0.1,"| Salpeter")
imf_salpeter=imf(-2.35,100,15,100,20,"| Salpeter")
imf_salpeter=imf(-2.35,100,15,100,30,"| Salpeter")
imf_salpeter=imf(-2.35,100,15,100,40,"| Salpeter")
imf_salpeter=imf(-2.35,1,10,100,5,"| Salpeter")
imf_salpeter=imf(-2.5,1,5,100,1,"| test")
imf_salpeter=imf(-2.5,1,5,100,0.1,"| test")
imf_salpeter=imf(-2.5,1,8,100,0.1,"| test")
imf_salpeter=imf(-2.5,1,8,100,5,"| test")





exit
