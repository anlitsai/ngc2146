#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
g_mks=6.67e-11
g_cgs=6.67e-8
pc=3.26*3.0e10*36586400
# --- parameter -------------------------------	#
incli=60
phi_ttl=180
dispv_r=10.0
alpha=0.3
beta=0.32
gamma=256.39
surf_den_mdsk=0.0014
# --- parameter -------------------------------	#
# ---------------------------------------------	#

#def vdisp_r():
	
#def vdisp_phi(v_disp_r,):
#	return 0.5*v_disp_r**2*(1+w)
#def vdisp_z(i,r,phi):
#	return i,r,phi
# w=dvc/dr


def vr(r): 
	vr=gamma*r/(r**alpha+r**(1-beta))
	return vr  

def wr(r):  
	wr=gamma*(1/(r**alpha+r**(1-beta))-r*(r**alpha+r**(1-beta))**(-2)*(alpha*r**(alpha-1)+(1-beta)*r**(-beta)))
	return wr

#def disp_v_phi(dispv_r,r):
#	dispv_phi=dispv_r*math.sqrt(0.5*(1+wr(r)))

dispv_maj=15.0
dispv_min=5.0
def disp_v(dispv_maj,dispv_min,i,r_kpc):
	r=r_kpc
	ii=i/180.0*math.pi
	sin2i=(math.sin(ii))**2
	cos2i=(math.cos(ii))**2
	dispv_r=math.sqrt((dispv_maj**2-dispv_min**2)/(sin2i*0.5*(wr(r)-1)))
	dispv_z=math.sqrt((dispv_min**2-(dispv_r**2*sin2i))/cos2i)
	dispv_phi=dispv_r*math.sqrt(0.5*(1+wr(r)))
	z0=((dispv_z*1.0e5)**2/(2*math.pi*g_cgs*surf_den_mdsk))/pc
	return dispv_r,dispv_z,dispv_phi,z0


print disp_v(15,5,63,3.0)

from pyx import *
import pyfits

# http://mail.scipy.org/pipermail/astropy/2009-April/000714.html

exit

