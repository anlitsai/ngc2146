#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
g_mks=6.67e-11
g_cgs=6.67e-8
M_sun=1.99e33 # solar mass
pc2cm=3.26*3e10*365*86400
kpc2cm=pc2cm*1.0e3
Msun_pc2=M_sun/pc2cm**2

# --- parameter -------------------------------	#
inclin=63
phi_ttl=180
dispv_r=10.0
alpha=0.3
beta=0.32
gamma=256.39
surf_den_mdsk=0.00144		# data	# pressure14.py	
surf_den_mdsk_Msunpc2=6.9	# data	# pressure14.py
surf_den_dyn_3500pc_Msunpc2=3700	# rotcur01.py
surf_den_dyn_3500pc=surf_den_dyn_3500pc_Msunpc2*Msun_pc2
surf_den_data_dsk1kpc_Msunpc2=400	# rotcur01.py
surf_den_data_dsk1kpc=surf_den_data_dsk1kpc_Msunpc2*Msun_pc2	# rotcur01.py
surf_den_dyn_1kpc_Msunpc2=400	# rotcur01.py
surf_den_dyn_1kpc=surf_den_dyn_1kpc_Msunpc2*Msun_pc2	# rotcur01.py
#surf_den_galdsk=2.09e-2		# rotcur05.py
#dispv_maj=(10.0,15.0,20.0)
dispv_min=5.0
v_rms=11.16	# r<2.4kpc(30as)	# v_resi_rms_x_n2146_r30as.pro
v_rms=8.5	# r<1.2kpc(15as)	# v_resi_rms_x_n2146_r15as.pro
# --- parameter -------------------------------	#
# ---------------------------------------------	#

#def vdisp_r():
	
#def vdisp_phi(v_disp_r,):
#	return 0.5*v_disp_r**2*(1+w)
#def vdisp_z(i,r,phi):
#	return i,r,phi
# w=dvc/dr
print ((11.2*1.0e5)**2/(2*math.pi*g_cgs*1200/9*Msun_pc2))/pc2cm
print ((11.2*1.0e5)**2/(2*math.pi*g_cgs*300*Msun_pc2))/pc2cm
print ((11.2*1.0e5)**2/(2*math.pi*g_cgs*400*Msun_pc2))/pc2cm
print ((11.2*1.0e5)**2/(2*math.pi*g_cgs*600*Msun_pc2))/pc2cm
print ((11.2*1.0e5)**2/(2*math.pi*g_cgs*1200*Msun_pc2))/pc2cm


def vr(r): 
	vr=gamma*r/(r**alpha+r**(1-beta))
	return vr  

def z0(dispv_z):
        z_pc=((dispv_z*1.0e5)**2/(2*math.pi*g_cgs*surf_den_mdsk))/pc2cm
	return z_pc


def disp_v0(dispv_maj,dispv_min,i,r_kpc):
        r=r_kpc
        ii=i/180.0*math.pi
        xi=r*math.cos(ii)
        yi=r*math.sin(ii)
        sin2i=(math.sin(ii))**2
        cos2i=(math.cos(ii))**2
	wr=gamma*(1/(r**alpha+r**(1-beta))-r*(r**alpha+r**(1-beta))**(-2)*(alpha*r**(alpha-1)+(1-beta)*r**(-beta)))
        dispv_r=math.sqrt((dispv_maj**2-dispv_min**2)/(sin2i*0.5*(wr-1)))
        dispv_z=math.sqrt((dispv_min**2-(dispv_r**2*sin2i))/cos2i)
        dispv_phi=dispv_r*math.sqrt(0.5*(1+wr))
        zi=z0(dispv_z)
        return r, zi, xi, yi, dispv_z, dispv_r, dispv_phi,dispv_maj,dispv_min

def disp_v1(dispv_los):
	dispv_z=dispv_los
        zi=z0(dispv_z)
	return zi, dispv_z

def disp_v2(dispv_los,i):
        ii=i/180.0*math.pi
	sin2i=math.sin(ii)
	cos2i=math.cos(ii)
	dispv_z=dispv_los/math.sqrt(4*sin2i+cos2i)
	dispv_r=2*dispv_z
        zi=z0(dispv_z)
	return zi, dispv_z, dispv_r

def disp_v3(dispv_los,i,phi):
        ii=i/180.0*math.pi
        phii=phi/180.0*math.pi
        sin2i=math.sin(ii)
        sin2phii=math.sin(phii)
        dispv_z=dispv_los/math.sqrt(sin2i+2*sin2i*sin2phii+1)
	dispv_r=2*dispv_z
	dispv_phi=math.sqrt(2)*dispv_z
        zi=z0(dispv_z)
        return zi, dispv_z, dispv_r, dispv_phi

v_min=dispv_min
v_maj=v_rms
fout = open("dispv14v11v0.dat", "w")
for ri in range(1,350):
        radi=ri*0.01
        disp=disp_v0(v_maj,v_min,inclin,radi)
        for j in range(0,9):
                fout.write(" ")
                fout.write(str(disp[j]))
        fout.write("\n")
fout.close()

fout = open("dispv14v11v1.dat", "w")
for ri in range(1,350):
	radi=ri*0.01
	dispv1=disp_v1(v_rms)
	fout.write(str(radi))
        for j in range(0,2):
                fout.write(" ")
                fout.write(str(dispv1[j]))
	fout.write("\n")
fout.close()

fout = open("dispv14v11v2.dat", "w")
for ri in range(1,350):
	radi=ri*0.01
	dispv2=disp_v2(v_rms,inclin)
	fout.write(str(radi))
        for j in range(0,3):
                fout.write(" ")
                fout.write(str(dispv2[j]))
	fout.write("\n")
fout.close()

fout = open("dispv14v11v3.dat", "w")
for ri in range(1,350):
        radi=ri*0.01
	phi=0
        dispv3=disp_v3(v_rms,inclin,phi)
	fout.write(str(radi))
        for j in range(0,4):
                fout.write(" ")
                fout.write(str(dispv3[j]))
        fout.write("\n")
fout.close()


# http://mail.scipy.org/pipermail/astropy/2009-April/000714.html

exit

