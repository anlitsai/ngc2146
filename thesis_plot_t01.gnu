#

set term png
set output 'thesis_plot_t.png'
#set term postscript solid color enhanced
#set output 'thesis_plot_t.ps'
set style data boxes
set size 0.6,0.6
#set style data boxes
set title 'Timescale related to Starburst Activities'
set boxwidth 0.2 absolute
set xrange[0:3]
set yrange[0:80]
set ylabel 'Timescale [Myr]' 
set xlabel 'Galaxy' 
set xtics ('NGC 2146' 1, 'NGC 3628' 2) 



set style fill solid border -1

plot 'thesis_plot_t.dat' using ($1-0.2):3 ti '' w boxes fs pattern 0.5, \
 'thesis_plot_t.dat' using ($1-0.2):2 ti 'Outflow expanding timescale' w boxes fs pattern 1 , \
'thesis_plot_t.dat' using ($1):5 ti '' w boxes fs pattern 0.5, \
'thesis_plot_t.dat' using ($1):4 ti 'Starburst timescale' w boxes fs pattern 1, \
'thesis_plot_t.dat' using ($1+0.2):6 ti 'Outflow return timescale' w boxes fs pattern 1 


set term x11
