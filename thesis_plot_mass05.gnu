#

set term png 
set output 'thesis_plot_mass.png'
#set term postscript solid color enhanced
#set output 'thesis_plot_mass.ps'
set style data boxes
set size 0.6,0.6
#set style data boxes
set style fill solid border -1
set title 'Molecular Gas Mass'
set boxwidth 0.2 absolute
set xrange[0:3]
set yrange[0:*]
set ylabel 'Gas Mass [10^8 M_{sun}]'
set xlabel 'Galaxy'
set xtics ('NGC 2146' 1, 'NGC 3628' 2)

plot 'thesis_plot_mass.dat' using ($1-0.2):3 ti 'Molecular Outflow', \
'thesis_plot_mass.dat' using ($1):4 ti 'Plasma Outflow', \
'thesis_plot_mass.dat' using ($1+0.2):5 ti 'Ionized Gas in Starburst Region'

set term x11
