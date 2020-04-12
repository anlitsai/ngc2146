#!/bin/bash

log1=fit1.log
log2=fit2.log
log3=fit3.log
rm -f $log1 $log2 $log3

gnuplot obslog_n3628_fluxSD10.gnu 
kpdf obslog_n3628_fluxSD.ps

a1=`grep -A3 "Final" $log1 | tail -1 | cut -d "=" -f2 | cut -d "+" -f1`
ad1=`grep -A3 "Final" $log1 | tail -1 | cut -d "=" -f2 | cut -d "-" -f2 | cut -d "(" -f1 | cut -d "+" -f1`
b1=`grep -A4 "Final" $log1 | tail -1 | cut -d "=" -f2 | cut -d "+" -f1`
bd1=`grep -A4 "Final" $log1 | tail -1 | cut -d "=" -f2 | cut -d "-" -f2 | cut -d "(" -f1 | cut -d "+" -f1`


a2=`grep -A3 "Final" $log2 | tail -1 | cut -d "=" -f2 | cut -d "+" -f1`
ad2=`grep -A3 "Final" $log2 | tail -1 | cut -d "=" -f2 | cut -d "-" -f2 | cut -d "(" -f1 | cut -d "+" -f1`
b2=`grep -A4 "Final" $log2 | tail -1 | cut -d "=" -f2 | cut -d "+" -f1`
bd2=`grep -A4 "Final" $log2 | tail -1 | cut -d "=" -f2 | cut -d "-" -f2 | cut -d "(" -f1 | cut -d "+" -f1`

a3=`grep -A3 "Final" $log3 | tail -1 | cut -d "=" -f2 | cut -d "+" -f1`
ad3=`grep -A3 "Final" $log3 | tail -1 | cut -d "=" -f2 | cut -d "-" -f2 | cut -d "(" -f1 | cut -d "+" -f1`
b3=`grep -A4 "Final" $log3 | tail -1 | cut -d "=" -f2 | cut -d "+" -f1`
bd3=`grep -A4 "Final" $log3 | tail -1 | cut -d "=" -f2 | cut -d "-" -f2 | cut -d "(" -f1 | cut -d "+" -f1`


echo $a1 $ad1 $b1 $bd1 $a2 $ad2 $b2 $bd2 $a3 $ad3 $b3 $bd3

