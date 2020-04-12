#

set terminal postscript enhanced color
unset log 
set size 0.7,0.7
#set size 0.6,0.6
set style line
#set style fill solid border -1
set xlabel "Starburst Activity Progess Factor  {/Symbol t}"
set ylabel "Starburst Enhanced Ratio  {/Symbol e}"
set title ""
#plot "sb_evolution.dat" using 1:2:3:4 with xyerrorbars
set style line
set fit logfile 'fit.log'


set output "sb_evolution.ps"
unset label
set label 1 "NGC 2146" at 0.25,1.5
set label 2 "NGC 3628" at 0.02,0.8
set label 3 "M82" at 0.8,0.35


f0(x)=1

f1(x)=a1+b1*x
fit [x=0:1][0:3]f1(x) "sb_evolution.dat" using 1:3:4 via a1,b1 w yerrorbars
f11(x)=a11+b11*x
fit [x=0:1][0:3]f11(x) "sb_evolution.dat" using 1:3 via a11,b11

f2(x)=a2+b2*x+c2*x**2
fit [x=0:1.05][0:3]f2(x) "sb_evolution.dat" using 1:3:4 via a2,b2,c2 w yerrorbars
f21(x)=a21+b21*x+c21*x**2
fit [x=0:1.05][0:3]f21(x) "sb_evolution.dat" using 1:3 via a21,b21,c21 
#fit [x=0:1.05][0:3]f2(x) "sb_evolution.dat" using 1:3:4 via a2,b2,c2 w yerrorbars;

set ytics nomirror
#set yrange [0:1]
#set ytics 0, 0.5
set y2range [0:30]
set y2tics 0,5

plot [x=0:1][0:2.5] \
f0(x) ti "" lt 3 lw 3, \
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4


set terminal png
set output "sb_evolution.1.png"
set output "sb_evolution.2.png"
set xlabel "Starburst Activity Progess Factor"
set ylabel "Starburst Enhanced Ratio"



plot [x=0:1][0:2.5] \
f0(x) ti "" lt 3 lw 3, \
f21(x) ti "" lt 2 lw 3, \
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4

"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):9:2:10 w xyerrorbars ti "Our data" lt 3 lw 2 pt 13  axis x1y2, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):9:2:10 w xyerrorbars ti "Literature data" lt 3 lw 2 pt 12 axis x1y2



set output "sb_evolution_quench.ps"
set y2range [0:2]
set y2tics 0.5
set autoscale

plot [x=0:1][0:2]\
plot [x=0:1]\
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):(log($9)):2:(log($10)) w xyerrorbars ti "Our data" lt 3 lw 2 pt 13  axis x1y2, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):(log($9)):2:(log($10)) w xyerrorbars ti "Literature data" lt 3 lw 2 pt 12 axis x1y2

plot [x=0:1]\
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):(log($9)):2:(log($10)) w xyerrorbars ti "Our data" lt 3 lw 2 pt 13, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):(log($9)):2:(log($10)) w xyerrorbars ti "Literature data" lt 3 lw 2 pt 12





plot [x=0:1][0:3] \
f0(x) ti "{/Symbol e}({/Symbol t}) = 1" lt 3 lw 3, \
f1(x) ti "{/Symbol e}({/Symbol t}) = 1.6 - 1.5{/Symbol t}" lt 2 lw 3, \
f2(x) ti "{/Symbol e}({/Symbol t}) = 1.4 + 0.1{/Symbol t} - 1.5{/Symbol t}^2" lt 5 lw 3, \
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4



f3(x)=a3
fit [x=0:1][0:120]f3(x) 'sb_evolution.dat' using 1:3:4 via a4 w yerrorbars;
plot [x=0:1][0:3]
f3(x) ti "{/Symbol e}({/Symbol t}) = 1.4 - 0.02{/Symbol t}" lt 2 lw 3, \
f2(x) ti "{/Symbol e}({/Symbol t}) = 1.2 + 0.04{/Symbol t} - 0.1{/Symbol t}^2" lt 3 lw 3, \
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4


f4(x)=a4*(1-erf(-b4))
fit [x=0:1.05][0:3]f4(x) "sb_evolution.dat" using 1:3 via a4,b4,c4;
fit [x=0:1.05][0:3]f4(x) "sb_evolution.dat" using 1:3:4 via a4,b4,c4 w yerrorbars;
plot [x=0:1][0:3]\
f4(x) ti "{/Symbol e}({/Symbol t}) = 1.2 + 0.04{/Symbol t} - 0.1{/Symbol t}^2" lt 3 lw 3,\ 
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):3:2:4 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4


# -------------------------------------------
set terminal postscript enhanced color
set size 0.6,0.6
set style line

set xlabel "Starburst Progress  {/Symbol t} [%]"
set ylabel "Outflow Return Timescale  t"
set title "Outflow"

set output "sb_evolution_t.ps"

set label "NGC 2146" at 0.33,40
set label "NGC 3628" at 0.05,7
set label "M82" at 0.7,103




g1(x)=a+b*x
fit [x=0:1][0:120]g1(x) 'sb_evolution.dat' using 1:5:6 via a,b w yerrorbars;

plot [x=0:1][0:200]\
g1(x) ti "{/Symbol e}({/Symbol t}) = 1.3 + 161{/Symbol t}" lt 3 lw 3, \
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4


 
set ytics nomirror
#set yrange [0:1]
#set ytics 0, 0.5
set y2range [0:30]
set y2tics 0,5 


plot [x=0:1][0:120]\
"sb_evolution.dat" using ($1<0.5 ? $1 : 1/0):9:2:10 w xyerrorbars ti "Our data" lt 3 lw 2 pt 13  axis x1y2, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):9:2:10 w xyerrorbars ti "Literature data" lt 3 lw 2 pt 12 axis x1y2





# -------------------------------------------
plot [x=0:1][0:120]\
g1(x) ti "{/Symbol e}({/Symbol t}) = 1.3 + 161{/Symbol t}" lt 3 lw 3 axis x1y2, \
"quench.dat" using :5:2:6 w xyerrorbars ti "Our data" lt 1 lw 2 pt 5 axis x1y2, \
"sb_evolution.dat" using ($1>0.5 ? $1 : 1/0):5:2:6 w xyerrorbars ti "Literature data" lt 1 lw 2 pt 4 axis x1y2



# -------------------------------------------
set ylabel "t_{back}/t_{cons}"
# -------------------------------------------



# exit
