#

set term png
set output 'thesis_plot_sfr.png'
#set term postscript solid color enhanced
#set output 'thesis_plot_sfr.ps'
set style data boxes
set size 0.6,0.6
#set style data boxes
set title 'Molecular Gas Mass Consumption'
set boxwidth 0.4 absolute
set xrange[0:3]
set yrange[0:80]
set ylabel 'dM/dt [M_sun/yr]' 
set xlabel 'Galaxy' 
set xtics ('NGC 2146' 1, 'NGC 3628' 2) 



set style fill solid border -1

plot 'thesis_plot_sfr.dat' using ($1-0.2):3 ti '' w boxes fs pattern 0.5, \
 'thesis_plot_sfr.dat' using ($1-0.2):2 ti '' w boxes fs pattern 1 , \
 'thesis_plot_sfr.dat' using ($1-0.2):2 ti '' w boxes fs pattern 1 , \
 'thesis_plot_sfr.dat' using ($1-0.2):2 ti 'Molecular Outflow Rate' w boxes fs pattern 1 , \
'thesis_plot_sfr.dat' using ($1+0.2):($4*1.1) ti '' w boxes fs pattern 0, \
'thesis_plot_sfr.dat' using ($1+0.2):($4*1.1) ti '' w boxes fs pattern 0, \
'thesis_plot_sfr.dat' using ($1+0.2):($4*1.1) ti '' w boxes fs pattern 0, \
'thesis_plot_sfr.dat' using ($1+0.2):($4*0.9) ti 'SFR in Starburst Region' w boxes fs pattern 2

set term x11
