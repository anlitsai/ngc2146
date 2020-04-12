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

def fit4(ary_f,ary_t,type):
	n=len(ary_f)
	sum_f=0
	sum_ff=0
	sum_t=0
	sum_tt=0
	sum_ft=0
	sum_fabt=0
	for i in range(n):
		sum_f=sum_f+ary_f[i]
		sum_t=sum_t+ary_t[i]
		sum_ff=sum_ff+(ary_f[i])**2
		sum_tt=sum_tt+(ary_t[i])**2
		sum_ft=sum_ft+(ary_f[i])*(ary_t[i])
	a=(sum_f*sum_t-n*sum_ft)/(sum_t**2-n*sum_tt)
	b=(sum_ft*sum_t-sum_f*sum_tt)/(sum_t**2-n*sum_tt)
	for i in range(n):
		sum_fabt=sum_fabt=(ary_f[i]-a*ary_t[i]-b)**2
	sigma=math.sqrt((sum_fabt)/(n-2))
	sigma_t=sigma/math.sqrt(sum_tt)
	sigma_f=sigma/math.sqrt(sum_ff)
	sigma_b=sigma/math.sqrt(n)
	d=(sum_t**2)-n*sum_tt
	gamma=(n*sum_ft-sum_f*sum_t)/math.sqrt((n*sum_tt-sum_t**2)*(n*sum_ff-sum_f**2))
#	print type, "| n =", n, "| a =", '%.5f' %a,"| b =", '%.3f' %b
	print type, "| n =", n, "| flux =", '%.3f' %b,"+", '%.5f' %a, "x [day since 1101]"
	print "         | sigma =",'%.3f' %sigma, "| sigma_b =",'%.3f' %sigma_b
	print "         | sigma_t =",'%.5f' %sigma_t,  "| sigma_f =",'%.5f' %sigma_f
#	print "         | 1-sigma_t =",'%.5f' %(1-sigma_t),  "| 1-sigma_f =",'%.5f' %(1-sigma_f)
	print "         | d =",'%.3f' %d, "| gamma =", '%.3f' %gamma
	print sigma_f/(sum_f/n)
	return a,b,d,sigma,gamma
	



# http://mathworld.wolfram.com/LeastSquaresFitting.html
def fit5(ary_f,ary_t,type):
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
	b=(n*sum_ft-sum_f*sum_t)/nab
#	b=ssum_ft/ssum_tt
	ave_t=sum_t/n
	ave_f=sum_f/n
	ssum_tt=sum_t2-n*ave_t**2
	ssum_ff=sum_f2-n*ave_f**2
	ssum_ft=sum_ft-n*ave_f*ave_t
	sig_t2=ssum_tt/n
	sig_f2=ssum_ff/n
	cov_ft=ssum_ft/n
	sig_t=math.sqrt(sig_t2)
	sig_f=math.sqrt(sig_f2)
	gamma2=ssum_ft**2/(ssum_tt*ssum_ff)
	gamma=math.sqrt(gamma2)
	s=math.sqrt((ssum_ff-b*ssum_ft)/(n-2))
	sd_error_a=s*math.sqrt(1/n+ave_t**2/ssum_tt)
	sd_error_b=s/math.sqrt(ssum_tt)
	uncert_f=sig_f/ave_f
	uncert_t=sig_t/ave_t
#	print type, "| n =", n, "| a =", '%.5f' %a,"| b =", '%.3f' %b
	print type, "| n =", n, "| flux =", '%.3f' %a,"+", '%.5f' %b, "x [day since 1101]"
	print "         | sd_error_a =",'%.5f' %sd_error_a, "| sd_error_b =",'%.5f' %sd_error_b, "| gamma =",'%.3f' %gamma
	print "         | ssum_ff =",'%.3f' %ssum_ff, "| ssum_tt =",'%.3f' %ssum_tt, "| ssum_ft =",'%.3f' %ssum_ft
	print "         | sig_f =",'%.3f' %sig_f, "| sig_t =",'%.3f' %sig_t
#	print "         | sigma =",'%.3f' %sigma, "| sigma_t =",'%.5f' %sigma_t, "| sigma_b =",'%.3f' %sigma_b
#	print "         | d =",'%.3f' %d, "| gamma =", '%.3f' %gamma
	print "         | sum_f =",'%.3f' %sum_f, "| sum_t =",'%.3f' %sum_t
	print "         | ave_f =",'%.3f' %ave_f, "| ave_t =",'%.3f' %ave_t
	print "         | uncert_f =",'%.3f' %uncert_f, "| uncert_t =",'%.3f' %uncert_t
	print "         | accur_f =",'%.3f' %(1-uncert_f), "| accur_t =",'%.3f' %(1-uncert_t)
	return a,b,s
	


print "---------------------------------"
fit_0155=fit4(array_f1,array_d1,"1055+018")
fit_3c84=fit4(array_f2,array_d2,"3C84    ")
fit_3c345=fit4(array_f3,array_d3,"3C345   ")
print "---------------------------------"
fit_0155=fit5(array_f1,array_d1,"1055+018")
fit_3c84=fit5(array_f2,array_d2,"3C84    ")
fit_3c345=fit5(array_f3,array_d3,"3C345   ")
print "---------------------------------"







exit

