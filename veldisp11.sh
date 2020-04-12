#!/bin/bash

./veldisp09.py
./veldisp11.py
gnuplot < veldisp11.gnu

ps2pdf z0.ps


rm -f z0.ps dispv09v*.dat dispv11v*.dat

exit

http://phi.sinica.edu.tw/tyuan/old.pages/pcfarm.19991228/aspac/aspac/reports/94/94002/plot-6
