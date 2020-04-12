#!/bin/bash


set terminal postscript enhanced color
set output "z0.ps"
set style data line
set xlabel "radius [kpc]"
set ylabel "disk thickness [pc]"
set label "{/Symbol s}_R={/Symbol s_f}={/Symbol s}_z=10" at 1,580
set label "{/Symbol s}_R=5, {/Symbol s_f}=11.2" at 1,500
set label "{/Symbol s}_R=5, {/Symbol s_f}=15" at 1,400
set label "{/Symbol s}_R=5, {/Symbol s_f}=20" at 1,250
set label "{/Symbol s}_R={/Symbol s_f}=11.2, {/Symbol s}_z=5.6" at 1,140
plot "dispv09v10.dat" using 1:4,  "dispv09v15.dat" using 1:4,  "dispv09v20.dat" using 1:4,  "dispv11v.dat" using 1:2, "dispv11v.dat" using 1:4
#set terminal x11


