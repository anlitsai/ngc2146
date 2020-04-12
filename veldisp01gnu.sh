#!/bin/bash

callplot=plot.txt

echo 'time=10' >> $callplot
echo 'set style data line' >> $callplot
echo 'plot "dispv.dat" using 1:9' >> $callplot
echo 'pause time' >> $callplot
echo '' >> $callplot
gnuplot < $callplot

rm -f $callplot

exit

