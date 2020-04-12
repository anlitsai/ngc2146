#!/bin/bash

./veldisp13.py
gnuplot < veldisp13.gnu

ps2pdf z0.ps


rm -f z0.ps dispv13v*.dat 

exit

http://phi.sinica.edu.tw/tyuan/old.pages/pcfarm.19991228/aspac/aspac/reports/94/94002/plot-6
