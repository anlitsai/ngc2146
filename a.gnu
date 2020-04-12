set term postscript solid color 

set output 'obslog_n3628_fluxSD.ps' 

set xlabel 'Day' 

set ylabel 'Flux [Jy]' 

f1(x)=a1+b1*x; 

f1e(x)=a1e+b1e*x; 

f2(x)=a2+b2*x; 

f3(x)=a3+b3*x; 

set fit logfile 'fit.log' 

fit [0:200]f1(x) 'obslog_n3628_cal_1055018_1.dat' using 1:2 via a1,b1; 

fit [0:200]f1e(x) 'obslog_n3628_cal_1055018_1.dat' using 1:2:3 via a1e,b1e; 

fit [0:200]f2(x) 'obslog_n3628_cal_3c84.dat' using 1:2 via a2,b2; 

fit [0:200]f3(x) 'obslog_n3628_cal_3c345.dat' using 1:2 via a3,b3; 

set title 'y= 5.42332          + -0.00107001      *x' 

set yrange[0:10] 

plot 'obslog_n3628_cal_1055018_1.dat' using 1:2, f1(x),f1e(x); 

plot 'obslog_n3628_cal_1055018_1.dat' using 1:2, 'obslog_n3628_cal_3c84.dat' using 1:2, 'obslog_n3628_cal_3c345.dat' using 1:2, f1(x),f2(x),f3(x); 

plot 'obslog_n3628_cal_1055018_1.dat' using 1:2 with points, f1(x); 

set title 'y= 4.25135          + 0.00207421       *x' 

plot 'obslog_n3628_cal_3c84.dat' using 1:2 with points, f2(x); 

set title 'y= 5.77586          + -0.00238695      *x' 

plot 'obslog_n3628_cal_3c345.dat' using 1:2 with points, f3(x); 


