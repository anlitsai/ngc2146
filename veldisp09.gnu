#!/bin/bash


set terminal postscript
set output "z0.ps"
set style data line
set xlabel "radius [kpc]"
set ylabel "disk thickness [pc]"
plot "dispv09v15.dat" using 1:4,"dispv09v10.dat" using 1:4,"dispv09v20.dat" using 1:4
#set terminal x11


