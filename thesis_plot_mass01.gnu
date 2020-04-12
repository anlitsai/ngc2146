#
set style data boxes
set title 'Molecular Gas Mass'
set boxwidth 0.9 absolute
set xrange[0:3]
set yrange[0:*]
set ylabel 'Mass [10^8 M_{sun}]'
set xlabel 'Galaxy'
set xtics ('NGC 2146' 1, 'NGC 3628' 2)

#plot 'thesis_plot_mass.dat' using 1:2, 'thesis_plot_mass.dat' using 1:3, 'thesis_plot_mass.dat' using 1:4
plot 'thesis_plot_mass.dat' using 1:3, 'thesis_plot_mass.dat' using 1:4, 'thesis_plot_mass.dat' using 1:5
