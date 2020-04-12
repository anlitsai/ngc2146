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
surf_den_mdsk=0.0014		# data	# pressure14.py
surf_den_mdsk_Msunpc2=6.9	# data	# pressure14.py
surf_den_dyn_3500pc_Msunpc2=3700		# rotation01.py
surf_den_dyn_3500pc=surf_den_dyn_3500pc_Msunpc2*Msun_pc2
#surf_den_galdsk=2.09e-2		# pressure14.py
v_rms=11.16	# r<2.4kpc(30as)	# v_resi_rms_x_n2146_r30as.pro
#v_rms=8.5	# r<1.2kpc(15as)	# v_resi_rms_x_n2146_r15as.pro
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


print "============"

def z0(dispv_z_kms,surf_den_Msunpc2):
	v_z=dispv_z_kms*1.0e5
	surf_den=surf_den_Msunpc2*Msun_pc2
        z_pc=(v_z**2/(2*math.pi*G_cgs*surf_den))/pc2cm
	print "z =",'%.2f' %(z_pc),"[pc] dpv_z=",dispv_z_kms,"[km/s] surf.den.=",surf_den_Msunpc2,"[M_sun/pc^2]"
	return z_pc

z=z0(v_rms,50)
z=z0(v_rms,100)
#z=z0(v_rms,1000)
z=z0(v_sun,50)
z=z0(v_sun,100)
#z=z0(v_sun,1000)
z=z0(v_1kpc,50)
z=z0(v_1kpc,100)
#z=z0(v_1kpc,1000)
print "------------"
z=z0(v_rms,surf_den_mdsk_Msunpc2)

print "============"

def surf_den(dispv_z_kms,z_kpc):
	v_z=dispv_z_kms*1.0e5
	z=z_kpc*kpc2cm
        surf_den_Msunpc2=(v_z**2/(2*math.pi*G_cgs*z))/Msun_pc2
#	print "------------"
	print "surf.den.=",'%.2f' %(surf_den_Msunpc2),"[M_sun/pc^2]","(z =",z_kpc,"kpc) dpv_z =",dispv_z_kms,"[km/s]"
#	print "dispersion velocity (z =",z_kpc,"kpc) =",dispv_z_kms,"[km/s]"
#	print "surface mass density =",'%.2f' %(surf_den_Msunpc2),"[M_sun/pc^2]"
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
        v_z_kms=math.sqrt(2*math.pi*G_cgs*z*surf_den)/1.0e5
	print "v_z_kms =",'%.2f' %(v_z_kms),"[km/s] (z =",z_kpc,"kpc) surf.den.=",surf_den_Msunpc2,"[Msun/pc^2]"
	return v_z_kms
	
vz=dispv_z(0.7,90.0)


print "============"
def surf_den_kin(v_kms,r_kpc):
        v=v_kms*1.0e5
        r=r_kpc*kpc2cm
	m_dyn=r*v**2/G_cgs
        sd_dyn=m_dyn/(math.pi*r**2)
        sd_dyn_Msunpc2=sd_dyn/Msun_pc2
#	print "------------"
#        print name,"disp.v.=",v_kms,"km/s (z <",r_kpc,"kpc)"
#        print "ttl.surf.mass den.=",'%.2f' %(sd_kin_Msunpc2),"[M_sun/pc^2]"
        print "kin.surf.den.="'%.2f' %(sd_dyn_Msunpc2),"[M_sun/pc^2] <",r_kpc,"kpc ; dpv_z =",v_kms,"km/s"
        return sd_dyn
print "------------"
print n2146
print "------------"
sd=surf_den_kin(v_rms,0.5)
sd=surf_den_kin(v_rms,0.8)
sd=surf_den_kin(v_rms,1)
sd=surf_den_kin(v_rms,1.2)
sd=surf_den_kin(v_rms,1.25)
sd=surf_den_kin(v_rms,1.5)
sd=surf_den_kin(v_rms,2)
sd=surf_den_kin(v_rms,2.5)
sd=surf_den_kin(v_rms,3)
print "------------"
print "Galaxy"
print "------------"
sd=surf_den_kin(17,0.7)
sd=surf_den_kin(20,0.8)
sd=surf_den_kin(20,1)
sd=surf_den_kin(20,0.25)
sd=surf_den_kin(30,1)


exit

