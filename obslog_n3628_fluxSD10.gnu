#
# set term postscript enhanced color solid
set term postscript enhanced solid
set output 'obslog_n3628_fluxSD.ps'
#set title '1055+018 / 3C84 / 3C345'
set xlabel 'Day'
set ylabel 'Flux [Jy]'
#set multiplot

f(x)=a+b*x;
f1(x)=a1+b1*x;
f2(x)=a2+b2*x;
f3(x)=a3+b3*x;

#a=5.0; b=0.002;
tb=0; te=200;

set fit logfile 'fit1.log'
fit [tb:te]f1(x) "obslog_n3628_cal_1055018_1.dat" using 1:2 via a1,b1;

set fit logfile 'fit2.log'
fit [tb:te]f2(x) "obslog_n3628_cal_3c84.dat" using 1:2 via a2,b2;

set fit logfile 'fit3.log'
fit [tb:te]f3(x) "obslog_n3628_cal_3c345.dat" using 1:2 via a3,b3;



set title '1055+018'
plot "obslog_n3628_cal_1055018_1.dat" using 1:2 with points, f1(x);

set title '3C84'
plot "obslog_n3628_cal_3c84.dat" using 1:2 with points, f2(x);

set title '3C345'
plot "obslog_n3628_cal_3c345.dat" using 1:2 with points, f3(x);



