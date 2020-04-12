#

#set term png
#set output 'thesis_plot_ostar.png'
set term postscript solid color enhanced
set output 'thesis_plot_ostar.ps'
set style data boxes
set size 0.6,0.6
#set style data boxes
set title 'Energy Produced from Starburst Activities'
set boxwidth 0.4 absolute
set xrange[0:3]
set yrange[0:*]
set ylabel 'Number of Object [10^3]' 
set xlabel 'Galaxy' 
set xtics ('NGC 2146' 1, 'NGC 3628' 2) 



set style fill solid border -1

plot 'thesis_plot_ostar.dat' using ($1-0.2):3 ti 'SN (upper)' w boxes fs pattern 0.5, \
 'thesis_plot_ostar.dat' using ($1-0.2):2 ti 'SN (lower)' w boxes fs pattern 1 , \
'thesis_plot_ostar.dat' using ($1+0.2):4 ti 'O-type star' w boxes fs pattern 2

set term x11
