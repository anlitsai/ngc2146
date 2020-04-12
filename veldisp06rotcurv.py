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

def vr_kms(r_kpc): 
	r=r_kpc
	vr=gamma*r/(r**alpha+r**(1-beta))
	return vr  

def wr_s(r_kpc):  
	r=r_kpc
	wr=gamma*(1.0/(r**alpha+r**(1-beta))-r*(r**alpha+r**(1-beta))**(-2)*(alpha*r**(alpha-1)+(1-beta)*r**(-beta)))
	return wr

print vr_kms(3.0),wr_s(3.0)


exit

