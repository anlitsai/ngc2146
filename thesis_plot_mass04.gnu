#

set term postscript solid color
set output 'thesis_plot_mass.ps'
set style data boxes
#set style data boxes
set style fill solid border -1
set title 'Molecular Gas Mass'
set boxwidth 0.8 absolute
set xrange[0:3]
set yrange[0:*]
set ylabel '% or Total Molecular Gas Mass'
set xlabel 'Galaxy'
set xtics ('NGC 2146' 1, 'NGC 3628' 2)

plot 'thesis_plot_mass.dat' using 1:($3+$4+$5)/($3+$4+$5)*100 ti 'Mass of Molecular Outflow', \
'thesis_plot_mass.dat' using 1:($4+$5)/($3+$4+$5)*100 ti 'Mass of Plasma Outflow', \
'thesis_plot_mass.dat' using 1:($5)/($3+$4+$5)*100 ti 'Mass of Ionized Gas in SBR'

