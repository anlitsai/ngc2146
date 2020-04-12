#!/usr/bin/env python

# --- import constant ------------------------- #
import math
#import pyfits
from string import *
#from numeric import *
# --- constant -------------------------------- #
c=3.0e10 # light speed
yr=365*86400.0
pc=3.26*c*yr
myr=1.0e6*yr
kpc=pc*1.0e3
ev=1.6e-12
G=6.67e-8 # gravitational constant
k_B=1.38e-16 # boltzmann constant
Msun=1.99e33 # solar mass
Msun_pc2=Msun/pc**2
Lsun=3.9e33 # solar luminosity
N_A=6.02e23 # Avogadro constant
m_p=1.67e-24
rad2as=180.0/math.pi*3600
#E_ion_ev=13.6  # [eV]
#E_bnd_ev=4.52  # [eV]
c_cms=2.99792458e10
#  --- parameter -------------------------------        #

#n=`cat property.dat | wc -l`

#http://pentangle.net/python/handbook/node41.html

fin=open("property.dat","r")
#line=fin.readline()
line=fin.read()
#print line
data=split(line)
print data
#x=int(data[2])
x=float(data[2])
print x





exit
