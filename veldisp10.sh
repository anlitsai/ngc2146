#!/bin/bash

./veldisp09.py
./veldisp10.py
gnuplot < veldisp10.gnu

ps2pdf z0.ps


rm -f z0.ps dispv09v*.dat dispv10v*.dat

exit

http://phi.sinica.edu.tw/tyuan/old.pages/pcfarm.19991228/aspac/aspac/reports/94/94002/plot-6
