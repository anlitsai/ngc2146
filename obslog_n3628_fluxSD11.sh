#!/bin/bash

log1=fit1.log
log2=fit2.log
log3=fit3.log
rm -f $log1 $log2 $log3
tb=0
te=200
outps=obslog_n3628_fluxSD.ps
gnutxt=a.gnu

echo -e "f1(x)=a1+b1*x; \n
f2(x)=a2+b2*x; \n
f3(x)=a3+b3*x; \n
set fit logfile '$log1' \n
fit [$tb:$te]f1(x) 'obslog_n3628_cal_1055018_1.dat' using 1:2 via a1,b1; \n
set fit logfile '$log2' \n
fit [$tb:$te]f2(x) 'obslog_n3628_cal_3c84.dat' using 1:2 via a2,b2; \n
set fit logfile '$log3' \n
fit [$tb:$te]f3(x) 'obslog_n3628_cal_3c345.dat' using 1:2 via a3,b3; \n
" > $gnutxt

gnuplot $gnutxt


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




echo -e "set term postscript solid color \n
set output '$outps' \n
set xlabel 'Day' \n
set ylabel 'Flux [Jy]' \n
f1(x)=a1+b1*x; \n
f2(x)=a2+b2*x; \n
f3(x)=a3+b3*x; \n
fit [$tb:$te]f1(x) 'obslog_n3628_cal_1055018_1.dat' using 1:2 via a1,b1; \n
set fit logfile '$log2' \n
fit [$tb:$te]f2(x) 'obslog_n3628_cal_3c84.dat' using 1:2 via a2,b2; \n
set fit logfile '$log3' \n
fit [$tb:$te]f3(x) 'obslog_n3628_cal_3c345.dat' using 1:2 via a3,b3; \n
set title 'y=$a1+$b1*x' \n
set yrange[0:10] \n
plot 'obslog_n3628_cal_1055018_1.dat' using 1:2, 'obslog_n3628_cal_3c84.dat' using 1:2, 'obslog_n3628_cal_3c345.dat' using 1:2, f1(x),f2(x),f3(x); \n
plot 'obslog_n3628_cal_1055018_1.dat' using 1:2 with points, f1(x); \n
set title 'y=$a2+$b2*x' \n
plot 'obslog_n3628_cal_3c84.dat' using 1:2 with points, f2(x); \n
set title 'y=$a3+$b3*x' \n
plot 'obslog_n3628_cal_3c345.dat' using 1:2 with points, f3(x); \n
" > $gnutxt

gnuplot $gnutxt




kpdf $outps



