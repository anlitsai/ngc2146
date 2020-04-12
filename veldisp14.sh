#!/bin/bash

./veldisp14.py
gnuplot < veldisp14.gnu

ps2pdf z0.ps


rm -f z0.ps dispv14v*.dat 

exit

http://phi.sinica.edu.tw/tyuan/old.pages/pcfarm.19991228/aspac/aspac/reports/94/94002/plot-6
