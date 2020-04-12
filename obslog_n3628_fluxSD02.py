#!/usr/bin/env python

# --- import constant -------------------------	#
from math import *
from Numeric import *  
# --- constant --------------------------------	#
n1=4
n2=9
n3=17
# --- claim --------------------------------	#
array_f1=[5.66,5.28,4.74,5.70]
array_d1=[33.08,57.29,86.15,116.25]
array_f2=[4.24,4.49,4.29,3.95,5.12,4.07,4.52,4.78,4.473]
array_d2=[12.71,54.58,62.54,78.60,81.50,106.42,119.46,137.38,152.33]
array_f3=[5.56,5.38,5.84,6.00,5.80,5.21,6.25,5.95,5.49,5.33,5.62,5.63,6.02,5.03,5.03,5.72,5.462]
array_d3=[13.13,17.67,37.56,38.52,38.63,45.65,46.60,54.58,62.54,74.54,74.58,81.50,100.33,106.42,119.46,137.38,152.31]
# --------------------------------------------- #
def flux(day,a,b,type):
	flux=a-b*day
#	print flux, "[Jy]"
	return flux

# http://www.daniweb.com/forums/thread177107.html
def SD():
    b = []
    for n in range(r-1):
        if r[n] > a:
             b.append((r[n] - a)**2)
        if r[n] < m:
             b.append((a - r[n])**2)
    SD = (float(b)/r)**0.5 #float because the data includes decimal values
    return SD
print "The standard deviation is", SD




def stddv(ary):
	n=len(ary)
	sum=0
	for i in range(n):
		sum=sum+ary[i]
	mean=sum/n
	sd2=0
	for i in range(n):
		sd2=sd2+(ary[i]-mean)**2
	sd=math.sqrt(sd2/n)
	b0=0
	print "n =", n, "| sum =",sum,"| mean =", mean,"| stddev =",sd
	return mean,sd


def reg(ary_f,ary_t,type):
	n=len(ary_f)
	sum_f=0
	sum_t=0
	for i in range(n):
		sum_f=sum_f+ary_f[i]
		sum_t=sum_t+ary_t[i]
	mean_f=sum_f/n
	mean_t=sum_t/n
	sd2_f=0
	sd2_t=0
	for i in range(n):
		sd2_f=sd2_f+(ary_f[i]-mean_f)**2
		sd2_t=sd2_t+(ary_t[i]-mean_t)**2
	sd_f=math.sqrt(sd2_f/n)
	sd_t=math.sqrt(sd2_t/n)
	err_f=sd_f/math.sqrt(n)
	b1=0
	b2=0
	for i in range(n):
		b1=b1+(ary_f[i]-mean_f)*(ary_t[i]-mean_t)
		b2=b2+(ary_t[i]-mean_t)**2
		b=b1/b2
		a=mean_f-b*mean_t
	print type, "| n =", n, "| sum =",sum_f,"| mean =", '%.3f' %mean_f,"| stddev =",'%.3f' %sd_f, "| err =", '%.3f' %err_f, "| acc = ", '%.3f' %(1-err_f)
	print "flux =",'%.3f' %a,"+", '%.3f' %b,"* day"
#	print "a =", a, "| b =",b, "flux =",a,"+",b,"* day"
	return a,b
	


print "---------------------------------"
sf1=stddv(array_f1)
sf2=stddv(array_f2)
sf3=stddv(array_f3)
sd1=stddv(array_d1)
sd2=stddv(array_d2)
sd3=stddv(array_d3)
print "---------------------------------"
reg(array_f1,array_d1,"1055+019")
reg(array_f2,array_d2,"3C84")
reg(array_f3,array_d3,"3C345")



exit

