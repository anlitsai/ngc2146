#

set terminal postscript enhanced color
set output "sfr_enhance.png"
set output "sfr_enhance.ps"
set size 0.7,0.7
set style line
#set style fill solid border -1
set xlabel "Starburst Progress  {/Symbol t} [%]"
set ylabel "SFR  [M_{sun}/yr]"
set title "SFR in the whole lifetime of starburst"
#plot "sb_evolution.dat" using 1:2:3:4 with xyerrorbars
set xrange[0:100]
set style line




plot [x=0:100][0:5]"sfr_enhance.dat" using 1:4 w histep ti "SFR" lt 1 lw 2 

set xrange[1:100]
set logscale y
set autoscale
set yrange[1:1e7]
plot "sfr_enhance_2.dat" using 1:4 w histep ti "SFR" lt 1 lw 2 


# exit
