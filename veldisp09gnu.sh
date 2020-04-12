#!/bin/bash


callplot=plot.txt

#echo 'time=20' >> $callplot
echo 'set terminal postscript' >> $callplot
echo 'set output "z0.ps"' >> $callplot
echo 'set style data line' >> $callplot
echo 'set xlabel "radius [kpc]"' >> $callplot
echo 'set ylabel "disk thickness [pc]"' >> $callplot
echo 'plot "dispv09v15.dat" using 1:4,"dispv09v10.dat" using 1:4,"dispv09v20.dat" using 1:4' >> $callplot
#echo 'pause time' >> $callplot
echo 'set terminal x11' >> $callplot
echo '' >> $callplot
gnuplot < $callplot



rm -f $callplot

exit

http://phi.sinica.edu.tw/tyuan/old.pages/pcfarm.19991228/aspac/aspac/reports/94/94002/plot-6
