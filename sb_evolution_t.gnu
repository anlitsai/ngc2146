#
set terminal postscript enhanced color
set size 0.6,0.6
set style line

set xlabel "Starburst Progress  {/Symbol t} [%]"
set ylabel "Outflow Return Timescale  t_{return}"
set title "Outflow"

set output "sb_evolution_t.ps"

set label "NGC 2146" at 0.33,40
set label "NGC 3628" at 0.05,7
set label "M82" at 0.7,103

set key right bottom




set ytics nomirror
set yrange [0:1]  
set ytics 0, 0.5
set y2range [0:120]  
set y2tics 0, 20

g1(x)=c1+d1*x
fit [x=0:1][0:120]g1(x) 'sb_evolution.dat' using 1:5:6 via c1,d1 w yerrorbars;

plot [x=0:1][0:120]\
g1(x) ti "t_{return}({/Symbol t}) = 1.3 + 161{/Symbol t}" lt 3 lw 3, \
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4

plot [x=0:1][0:120]\
g1(x) ti "t({/Symbol t}) = 1.3 + 161{/Symbol t}" lt 3 lw 3 axis x1y1, \
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5 axis x1y1, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4 axis x1y1


plot [x=0:1][0:120]\
g1(x) ti "t({/Symbol t}) = 1.3 + 161{/Symbol t}" lt 3 lw 3 axis x1y2, \
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5 axis x1y2, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4 axis x1y2


# -----------------
p


