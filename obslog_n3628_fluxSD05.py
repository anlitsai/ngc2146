#!/usr/bin/env python

# --- import constant -------------------------	#
from math import *
from Numeric import *  
from numpy import *

# --- constant --------------------------------	#
n1=4
n2=9
n3=17
m=2
# --- claim --------------------------------	#
array_v1=[1.311,0.936,0.85,1.27]
array_f1=[5.66,5.28,4.74,5.70]
array_d1=[33.08,57.29,86.15,116.25]
array_f2=[4.24,4.49,4.29,3.95,5.12,4.07,4.52,4.78,4.473]
array_d2=[12.71,54.58,62.54,78.60,81.50,106.42,119.46,137.38,152.33]
array_f3=[5.56,5.38,5.84,6.00,5.80,5.21,6.25,5.95,5.49,5.33,5.62,5.63,6.02,5.03,5.03,5.72,5.462]
array_d3=[13.13,17.67,37.56,38.52,38.63,45.65,46.60,54.58,62.54,74.54,74.58,81.50,100.33,106.42,119.46,137.38,152.31]
array_f4=[2.91,2.8,2.8,3.1,3.2]
array_test=[120.0,125.0,160.0,150.0]

# --------------------------------------------- #
def flux(day,a,b,type):
	flux=a-b*day
#	print flux, "[Jy]"
	return flux


# http://mathworld.wolfram.com/LeastSquaresFitting.html
def fit(ary_f,ary_t,type):
	n=len(ary_f)
	sum_f=0
	sum_f2=0
	sum_t=0
	sum_t2=0
	sum_ft=0
	sum_fabt2=0
	for i in range(n):
		sum_f=sum_f+ary_f[i]
		sum_t=sum_t+ary_t[i]
		sum_f2=sum_f2+(ary_f[i])**2
		sum_t2=sum_t2+(ary_t[i])**2
		sum_ft=sum_ft+(ary_f[i])*(ary_t[i])
	nab=n*sum_t2-sum_t**2
	a=(sum_f*sum_t2-sum_t*sum_ft)/nab
	b=(sum_ft*sum_t-sum_f*sum_t2)/nab
	ave_t=sum_t/n
	ave_f=sum_f/n
	ssum_tt=sum_t2-n*ave_t**2
	ssum_ff=sum_f2-n*ave_f**2
	ssum_ft=sum_ft-n*ave_f*ave_t
#	sig_t2=ssum_tt/n
#	sig_f2=ssum_ff/n
#	cov_ft=ssum_ft/n
	gamma2=ssum_ft**2/(ssum_tt*ssum_ff)
	gamma=math.sqrt(gamma2)
	s=math.sqrt(abs(ssum_ff-b*ssum_ft)/(n-2))
	sd_error_a=s*math.sqrt(1/n+ave_t**2/ssum_tt)
	sd_error_b=s/math.sqrt(ssum_tt)
#	print type, "| n =", n, "| a =", '%.5f' %a,"| b =", '%.3f' %b
	print type, "| n =", n, "| flux =", '%.3f' %b,"+", '%.5f' %a, "x [day since 1101]"
	print "         | sd_error_a =",'%.3f' %sd_error_a, "| sd_error_b =",'%.3f' %sd_error_b, "| gamma =",'%.3f' %gamma
	print "         | ssum_ff =",'%.3f' %ssum_ff, "| ssum_tt =",'%.3f' %ssum_tt, "| ssum_ft =",'%.3f' %ssum_ft
#	print "         | sigma =",'%.3f' %sigma, "| sigma_t =",'%.5f' %sigma_t, "| sigma_b =",'%.3f' %sigma_b
#	print "         | d =",'%.3f' %d, "| gamma =", '%.3f' %gamma
	print "         | sum_f =",'%.3f' %sum_f, "| sum_t =",'%.3f' %sum_t
	print "         | ave_f =",'%.3f' %ave_f, "| ave_t =",'%.3f' %ave_t
	return a,b,s
	

def flux(a,b,day,volt):
	flux=(a+b*day)*volt
	print "flux=",'%.5f' %flux
	return flux


def sd(a,b,array_day,array_flux,type):
	n=len(array_flux)
	sd2_f=0
	for i in range(n):
		fit_flux=a+b*array_day[i]
		data_flux=array_flux[i]
		del_flux=fit_flux-data_flux
		print fit_flux,data_flux,del_flux
		sd2_f=sd2_f+del_flux**2
	sd_f=math.sqrt(sd2_f/n)
	print type, "| n =", n,"| stddev =",'%.3f' %sd_f
	return sd_f

print "---------------------------------"
fit_0155=fit(array_f1,array_d1,"1055+018")
fit_3c84=fit(array_f2,array_d2,"3C84    ")
fit_3c345=fit(array_f3,array_d3,"3C345   ")
print "---------------------------------"







exit

