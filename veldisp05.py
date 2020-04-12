#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
incli=60
phi_ttl=180
w=10.0
dispv_r=10.0
alpha=0.3
beta=0.32
gamma=256.39

# --- parameter -------------------------------	#
# ---------------------------------------------	#

#def vdisp_r():
	
#def vdisp_phi(v_disp_r,):
#	return 0.5*v_disp_r**2*(1+w)
#def vdisp_z(i,r,phi):
#	return i,r,phi
# w=dvc/dr
#dispv_phi=dispv_r*2
dispv_z=0.5*dispv_r
dispv_phi=dispv_r*math.sqrt(0.5*(1+w))


def vr(r): 
	vr=gamma*r/(r**alpha+r**(1-beta))
	return vr  

def wr(r):  
	wr=gamma*(1/(r**alpha+r**(1-beta))-r*(r**alpha+r**(1-beta))**(-2)*(alpha*r**(alpha-1)+(1-beta)*r**(-beta)))
	return wr


def disp_v(i,phi):
	ii=i/180.0*math.pi
	phii=phi/180.0*math.pi
	xi=math.cos(phii)
	yi=math.sin(phii)
	dispv_maj=math.sqrt((dispv_phi*math.sin(ii))**2+(dispv_z*math.cos(ii))**2)
	dispv_min=math.sqrt((dispv_r*math.sin(ii))**2+(dispv_z*math.cos(ii))**2)
	dispv=math.sqrt(dispv_r**2+dispv_phi**2+dispv_z**2)
	dispv_los=math.sqrt((dispv_r*math.sin(phii)*math.sin(ii))**2+(dispv_phi*math.cos(phii)*math.sin(ii))**2+(dispv_z*math.cos(ii))**2)
#	print  phi, i, xi, yi, dispv_r, dispv_z, dispv_phi, dispv_maj, dispv_min, dispv, dispv_los
	return  phi, i, xi, yi, dispv_r, dispv_z, dispv_phi, dispv_maj, dispv_min, dispv, dispv_los
#	return dispv_los


fout = open("dispv04.dat", "w")
phi_ttl=180
for phi in range(0,phi_ttl):
	dispv=disp_v(incli,phi)
	for i_arr in range(3,11):
		fout.write(str(dispv[i_arr]))
		fout.write(" ")
	fout.write("\n")
fout.close()


from pyx import *
import pyfits

# http://mail.scipy.org/pipermail/astropy/2009-April/000714.html

exit

