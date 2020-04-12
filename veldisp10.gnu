#!/bin/bash


set terminal postscript color
set output "z0.ps"
set style data line
set xlabel "radius [kpc]"
set ylabel "disk thickness [pc]"
plot "dispv09v15.dat" using 1:4,"dispv09v10.dat" using 1:4,"dispv09v20.dat" using 1:4, "dispv10v.dat" using 1:2, "dispv10v.dat" using 1:3,"dispv10v.dat" using 1:4, "dispv10v.dat" using 1:6, "dispv10v.dat" using 1:8, "dispv10v.dat" using 1:10
#set terminal x11


