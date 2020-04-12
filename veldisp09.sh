#!/bin/bash

./veldisp09.py
gnuplot < veldisp09.gnu

ps2pdf z0.ps


rm -f z0.ps dispv09v*.dat

exit

http://phi.sinica.edu.tw/tyuan/old.pages/pcfarm.19991228/aspac/aspac/reports/94/94002/plot-6
