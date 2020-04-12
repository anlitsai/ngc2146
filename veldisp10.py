#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
g_mks=6.67e-11
g_cgs=6.67e-8
pc=3.26*3.0e10*36586400
# --- parameter -------------------------------	#
inclin=63
phi_ttl=180
dispv_r=10.0
alpha=0.3
beta=0.32
gamma=256.39
surf_den_mdsk=0.0014
#dispv_maj=(10.0,15.0,20.0)
dispv_min=5.0
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

#def disp_v1_phi(dispv_r,r):
#	dispv_phi=dispv_r*math.sqrt(0.5*(1+wr(r)))

def disp_v1(dispv):
	z0=((dispv*1.0e5)**2/(2*math.pi*g_cgs*surf_den_mdsk))/pc
	return z0

def disp_v2(dispv,i):
        ii=i/180.0*math.pi
	sin2i=math.sin(ii)
	cos2i=math.cos(ii)
	dispv_z=dispv/math.sqrt(4*sin2i+cos2i)
	z0=((dispv_z*1.0e5)**2/(2*math.pi*g_cgs*surf_den_mdsk))/pc
	return dispv_z, z0

fout = open("dispv10v.dat", "w")
for ri in range(1,350):
	radi=ri*0.01
	fout.write(str(radi))
	fout.write(" ")
	fout.write(str(disp_v1(10.0)))
	fout.write(" ")
	fout.write(str(disp_v1(15.0)))
	fout.write(" ")
	fout.write(str(disp_v1(20.0)))
	fout.write(" ")
	fout.write(str(disp_v2(10.0,inclin)[0]))
	fout.write(" ")
	fout.write(str(disp_v2(10.0,inclin)[1]))
	fout.write(" ")
	fout.write(str(disp_v2(15.0,inclin)[0]))
	fout.write(" ")
	fout.write(str(disp_v2(15.0,inclin)[1]))
	fout.write(" ")
	fout.write(str(disp_v2(20.0,inclin)[0]))
	fout.write(" ")
	fout.write(str(disp_v2(20.0,inclin)[1]))
	fout.write("\n")
fout.close()


# http://mail.scipy.org/pipermail/astropy/2009-April/000714.html

exit

