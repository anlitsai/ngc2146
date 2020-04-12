#!/usr/bin/env python

# --- import constant -------------------------	#
from math import *
from Numeric import *  
# --- constant --------------------------------	#
n1=4
n2=9
n3=17
# --- claim --------------------------------	#
array_f1=zeros(n1,Float)
array_f2=zeros(n2,Float)
array_f3=zeros(n3,Float)
array_ff1=[5.66,5.28,4.74,5.70]
array_ff2=[4.24,4.49,4.29,3.95,5.12,4.07,4.52,4.78,4.473]
array_ff3=[5.56,5.38,6.00,5.80,5.21,6.25,5.95,5.49,5.33,5.62,5.63,6.02,5.03,5.03,5.72,5.462]
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
	sd2=0
	for i in range(n):
		sum=sum+ary[i]
	mean=sum/n
	for i in range(n):
		sd2=sd2+(ary[i]-mean)**2
	sd=math.sqrt(sd2/n)
	print "n =", n, "| sum =",sum,"| mean =", mean,"| stddev =",sd
	return sd


print "---------------------------------"
array_f1[0]=flux(33.08,5.42,0.00108,"1055+018")
array_f1[1]=flux(57.29,5.42,0.00108,"1055+018")
array_f1[2]=flux(86.15,5.42,0.00108,"1055+018")
array_f1[3]=flux(116.25,5.42,0.00108,"1055+018")
print array_f1
stddv(array_f1)
print "---------------------------------"
array_f2[0]=flux(12.71,4.25,0.00206,"3C84")
array_f2[1]=flux(54.58,4.25,0.00206,"3C84")
array_f2[2]=flux(62.54,4.25,0.00206,"3C84")
array_f2[3]=flux(78.60,4.25,0.00206,"3C84")
array_f2[4]=flux(81.50,4.25,0.00206,"3C84")
array_f2[5]=flux(106.42,4.25,0.00206,"3C84")
array_f2[6]=flux(119.46,4.25,0.00206,"3C84")
array_f2[7]=flux(137.38,4.25,0.00206,"3C84")
array_f2[8]=flux(152.33,4.25,0.00206,"3C84")
print array_f2
stddv(array_f2)
print "---------------------------------"
array_f3[0]=flux(13.13,5.78,0.00239,"3C345")
array_f3[1]=flux(17.67,5.78,0.00239,"3C345")
array_f3[2]=flux(37.56,5.78,0.00239,"3C345")
array_f3[3]=flux(38.52,5.78,0.00239,"3C345")
array_f3[4]=flux(38.63,5.78,0.00239,"3C345")
array_f3[5]=flux(45.65,5.78,0.00239,"3C345")
array_f3[6]=flux(46.60,5.78,0.00239,"3C345")
array_f3[7]=flux(54.58,5.78,0.00239,"3C345")
array_f3[8]=flux(62.54,5.78,0.00239,"3C345")
array_f3[9]=flux(74.54,5.78,0.00239,"3C345")
array_f3[10]=flux(74.58,5.78,0.00239,"3C345")
array_f3[11]=flux(81.50,5.78,0.00239,"3C345")
array_f3[12]=flux(100.33,5.78,0.00239,"3C345")
array_f3[13]=flux(106.42,5.78,0.00239,"3C345")
array_f3[14]=flux(119.46,5.78,0.00239,"3C345")
array_f3[15]=flux(137.38,5.78,0.00239,"3C345")
array_f3[16]=flux(152.31,5.78,0.00239,"3C345")
print array_f3
stddv(array_f3)
print "---------------------------------"
print "---------------------------------"
print "---------------------------------"
print "---------------------------------"
print "---------------------------------"
print "---------------------------------"




exit

