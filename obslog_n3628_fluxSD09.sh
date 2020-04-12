#!/bin/bash

log1=fit1.log
log2=fit2.log
log3=fit3.log
rm -f $log1 $log2 $log3

echo "set term postscript solid; \
set output 'obslog_n3628_fluxSD.ps'; \
set xlabel 'Day'; \
set ylabel 'Flux [Jy]'; \
slp_1055_018(x)=a1+b1*x; \
slp_3c84(x)=a2+b2*x; \
slp_3c345(x)=a3+b3*x; \
set fit logfile $log1; \
fit [t1b:t1e]slp_1055_018(x) 'obslog_n3628_cal_1055018_1.dat' using 1:2 via a1,b1; \
set fit logfile $log2; \
fit [t2b:t2e]slp_3c84(x) 'obslog_n3628_cal_3c84.dat' using 1:2 via a2,b2; \
set fit logfile $log3; \
fit [t3b:t3e]slp_3c345(x) 'obslog_n3628_cal_3c345.dat' using 1:2 via a3,b3;" | gnuplot 




kpdf obslog_n3628_fluxSD.ps



