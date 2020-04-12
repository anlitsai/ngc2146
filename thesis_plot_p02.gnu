#

#set term png
#set output 'thesis_plot_p.png'
set term postscript solid color enhanced
set output 'thesis_plot_p_ram.ps'
set style data boxes
set size 0.6,0.6
#set style data boxes
set title 'Pressure Produced from Starburst Activities'
set boxwidth 0.2 absolute
set xrange[0:3]
set yrange[1.0e-14:1.0e-7]
set ylabel 'Pressure [dyne cm^-2]' 
set xlabel 'Galaxy' 
set xtics ('NGC 2146' 1, 'NGC 3628' 2) 
set logscale y
set label 'R = 2kpc' at 0.8,1.0e-9
set label 'R = 500pc' at 1.8,1.0e-9

set style fill solid border -1

#'thesis_plot_p_ram.dat' using ($1-0.3):5 ti 'Dynamic pressure of molecular gas' w boxes fs pattern 1, \
plot 'thesis_plot_p_ram.dat' using ($1-0.2):3 ti '' w boxes fs pattern 0.5, \
'thesis_plot_p_ram.dat' using ($1-0.2):2 ti 'Thermal P of plasma outflow' w boxes fs pattern 1, \
'thesis_plot_p_ram.dat' using 1:5 ti '' w boxes fs pattern 0.5, \
'thesis_plot_p_ram.dat' using 1:4 ti 'Ram P of plasma outflow' w boxes fs pattern 1, \
'thesis_plot_p_ram.dat' using ($1+0.2):7 ti '' w boxes fs pattern 0.5, \
'thesis_plot_p_ram.dat' using ($1+0.2):6 ti 'Thermal P of molecular outflow' w boxes fs pattern 2 

set term x11
