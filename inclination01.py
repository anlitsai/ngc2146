#!/usr/bin/env python

# --- import constant -------------------------	#
import math
# --- constant --------------------------------	#
pi2d=180.0/math.pi
#  --- parameter ------------------------------	#
print "============"
#print "parameters"
#print "------------"
a=[80.0,70.0,60.0,55.0,50.0,9.0,5.2,7.0]
b=[25.0,20.0,18.0,16.0,15.0,3.0,2.6,3.0]
n=8
#q=0.5
q0=0.2
# --- function --------------------------------	#
def incli_deg_simple(q):
	return math.acos(q)*pi2d
def incli_deg_hubble0(q):
	return math.acos(math.sqrt((q**2-q0**2)/(1-q0**2)))*pi2d
def incli_deg_hubble3(q):
	return math.acos(math.sqrt((q**2-q0**2)/(1-q0**2)))*pi2d+3.0
# --- calculation -----------------------------	#
for i in range(0,n):
	j=b[i]/a[i]
	i1=incli_deg_simple(j)
	i2=incli_deg_hubble0(j)
	i3=incli_deg_hubble3(j)
	print "a = ", a[i]
	print "b = ", b[i]
	print "b/a = ", j
	print "inclination simple = ",i1, "degree"
	print "inclination hubble 0 = ",i2, "degree"
	print "inclination hubble 3 = ",i3, "degree"
	print "------------"
# --- reference -------------------------------	#
# Aaronson 1980, ApJ, 237, 655
# Hubble 1926, ApJ, 64, 321
# Tully 1977, AA, 54, 661
# Ward 2000, (Note: Are Spiral Galaxies Round?)
exit

