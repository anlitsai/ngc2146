#
#set term postscript enhanced color
set term postscript solid
set output 'thesis_plot.ps'
#set title '1055+018 / 3C84 / 3C345'
#set xlabel 'Day'
#set ylabel 'Flux [Jy]'
#set multiplot

slp_1055_018(x)=a1+b1*x;
slp_3c84(x)=a2+b2*x;
slp_3c345(x)=a3+b3*x;

a1=5.0; b1=0.002;
a2=5.0; b2=0.002;
a3=5.0; b3=0.002;
t1b=0; t1e=200;
t2b=0; t2e=200;
t3b=0; t3e=200;

set fit logfile 'fit1.log'
fit [t1b:t1e]slp_1055_018(x) "obslog_n3628_cal_1055018_1.dat" using 1:2 via a1,b1;

set fit logfile 'fit2.log'
fit [t2b:t2e]slp_3c84(x) "obslog_n3628_cal_3c84.dat" using 1:2 via a2,b2;

set fit logfile 'fit3.log'
fit [t3b:t3e]slp_3c345(x) "obslog_n3628_cal_3c345.dat" using 1:2 via a3,b3;




set title '1055+018'
plot "obslog_n3628_cal_1055018_1.dat" using 1:2 with points, slp_1055_018(x);

set title '3C84'
plot "obslog_n3628_cal_3c84.dat" using 1:2 with points, slp_3c84(x);

set title '3C345'
plot "obslog_n3628_cal_3c345.dat" using 1:2 with points, slp_3c345(x);
