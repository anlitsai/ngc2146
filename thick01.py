#!/usr/bin/env python
# copy from veldisp14.py

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
G_cgs=6.67e-8
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
surf_den_mdsk=0.0014
surf_den_dyn_3500pc_Msunpc2=3700		# rotation01.py
surf_den_dyn_3500pc=surf_den_dyn_3500pc_Msunpc2*Msun_pc2
#surf_den_galdsk=2.09e-2		# pressure14.py
v_rms=11.16
v_sun=20.0
v_1kpc=30.0
n2146="NGC 2146"
# --- parameter -------------------------------	#
# ---------------------------------------------	#

#def vdisp_r():
	
#def vdisp_phi(v_disp_r,):
#	return 0.5*v_disp_r**2*(1+w)
#def vdisp_z(i,r,phi):
#	return i,r,phi
# w=dvc/dr



def z0(dispv_z_kms,surf_den_Msunpc2):
	v_z=dispv_z_kms*1.0e5
	surf_den=surf_den_Msunpc2*Msun_pc2
        z_pc=(v_z**2/(2*math.pi*G_cgs*surf_den))/pc2cm
	print "------------"
	print "dispersion velocity (z) =",dispv_z_kms,"[km/s]"
	print "surface mass density =",surf_den_Msunpc2,"[M_sun/pc^2]"
	print "z =",z_pc,"[pc]"
	return z_pc

z=z0(v_rms,50)
z=z0(v_rms,100)
z=z0(v_rms,1000)
z=z0(v_sun,50)
z=z0(v_sun,100)
z=z0(v_sun,1000)
z=z0(v_1kpc,50)
z=z0(v_1kpc,100)
z=z0(v_1kpc,1000)

print "============"

def surf_den(dispv_z_kms,z_kpc):
	v_z=dispv_z_kms*1.0e5
	z=z_kpc*kpc2cm
        surf_den_Msunpc2=(v_z**2/(2*math.pi*G_cgs*z))/Msun_pc2
	print "------------"
	print "dispersion velocity (z =",z_kpc,"kpc) =",dispv_z_kms,"[km/s]"
	print "surface mass density =",'%.2f' %(surf_den_Msunpc2),"[M_sun/pc^2]"
	return surf_den_Msunpc2
	
sd=surf_den(v_rms,1)
sd=surf_den(10,1)
sd=surf_den(20,1)
sd=surf_den(30,1)
sd=surf_den(10,2)
sd=surf_den(20,2)
sd=surf_den(30,2)
sd=surf_den(20,0.25)

print "============"

def dispv_z(z_kpc,surf_den_Msunpc2):
	z=z_kpc*kpc2cm
	surf_den=surf_den_Msunpc2*Msun_pc2
        v_z_kms=2*math.pi*G_cgs*z*surf_den/1.0e5
	print "------------"
	print "surface density (z =",z_kpc,"kpc) =",surf_den_Msunpc2,"[Msun/pc^2]"
	print "v_z_kms =",'%.2f' %(v_z_kms),"[km/s]"
	return v_z_kms
	
vz=dispv_z(0.7,90.0)


print "============"
def surf_den_kin(v_kms,r_kpc,name):
        v=v_kms*1.0e5
        r=r_kpc*kpc2cm
        sd_kin=v**2/(r*G_cgs)
        sd_kin_Msunpc2=sd_kin/Msun_pc2
        print name,"ttl.surf.mass den.=",'%.2f' %(sd_kin_Msunpc2),"[M_sun/pc^2] (z <",r_kpc,"kpc)"
        return sd_kin
sd1=surf_den_kin(v_rms,0.5,n2146)
sd2=surf_den_kin(v_rms,1,n2146)
sd3=surf_den_kin(v_rms,1.25,n2146)
sd4=surf_den_kin(v_rms,1.5,n2146)
sd5=surf_den_kin(v_rms,2,n2146)
sd6=surf_den_kin(v_rms,2.5,n2146)
sd7=surf_den_kin(v_rms,3,n2146)


exit

