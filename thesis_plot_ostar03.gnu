#

set term png
set output 'thesis_plot_energy_rate.png'
#set term postscript solid color enhanced
#set output 'thesis_plot_ostar.ps'
set style data boxes
set size 0.6,0.6
#set style data boxes
set title 'Production Rate from Starburst Activities'
set boxwidth 0.4 absolute
set xrange[0:3]
set yrange[1.0e-3:*]
set ylabel 'Object Production Rate [yr^-1]' 
set xlabel 'Galaxy' 
set xtics ('NGC 2146' 1, 'NGC 3628' 2) 
set logscale y



set style fill solid border -1


plot 'thesis_plot_ostar.dat' using ($1-0.2):($3/$5/1000) ti '' w boxes fs pattern 0.5, \
 'thesis_plot_ostar.dat' using ($1-0.2):($2/$6/1000) ti 'SN (lower)' w boxes fs pattern 1 , \
'thesis_plot_ostar.dat' using ($1+0.2):($4/1000*1.1) ti '' w boxes fs pattern 0, \
'thesis_plot_ostar.dat' using ($1+0.2):($4/1000*0.9) ti 'O-type star' w boxes fs pattern 2

set term x11
