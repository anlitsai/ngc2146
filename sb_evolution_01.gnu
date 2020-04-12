#

set terminal postscript enhanced color;
set output "sb_evolution.ps";
set size 0.6,0.6;
set style line;
#set style fill solid border -1
set xlabel "Starburst Progress  {/Symbol t} [%]";
set ylabel "Starburst Enhance Ratio  {/Symbol e}";
set title "Starburst Evolution Progress";
#plot "sb_evolution.dat" using 1:2:3:4 with xyerrorbars
set xrange[0:10];
set yrange[0:6];
set style line;





f(x)=a+b*x;
#a=3;b=1
set fit logfile 'fit.log';
fit f(x) "sb_evolution_enh.dat" using 1:3:4 via a,b with yerrorbars;
plot f(x) ti "{/Symbol e}({/Symbol t}) = 0.4 + 0.004{/Symbol t}" lt 3 lw 3,"sb_evolution_enh_data.dat" using 1:3:2:4 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, "sb_evolution_enh_ref.dat" using 1:3:2:4 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4;
#plot f(x) ti "{/Symbol e}({/Symbol t}) = 2.5 - 0.03{/Symbol t}" lt 3 lw 3,"sb_evolution.dat" using 1:3:2:4 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, "sb_evolution.dat" using 1:3:2:4 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4;
#plot f(x) ti "{/Symbol e}({/Symbol t}) = 2.5 - 0.03{/Symbol t}" lt 3 lw 3,"sb_evolution_enh_u.dat" using 1:($3*$5):2:($4*$5) w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, "sb_evolution_enh_o.dat" using 1:($3*$5):2:($4*$5) w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4;









# exit
