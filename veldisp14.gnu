#!/bin/bash


set terminal postscript enhanced color
set output "z0.ps"
set style data line
set xlabel "radius [kpc]"
set ylabel "disk thickness [pc]"
set label "{/Symbol s}_{los}=11.2 km/s, {/Symbol s}_R={/Symbol s_f}={/Symbol s}_z=11.2" at 0.5,580
set label "{/Symbol s}_{los}=11.2 km/s, {/Symbol s}_R=[0.67-2.88], {/Symbol s_f}=[11.26-11.61], {/Symbol s}_z=[10.93-9.45]" at 0.5,450
set label "{/Symbol s}_{los}=11.2 km/s, {/Symbol s}_R=16.29, {/Symbol s_f}=11.52, {/Symbol s}_z=8.14" at 0.5,305
set label "{/Symbol s}_{los}=11.2 km/s, {/Symbol s}_R={/Symbol s_f}=11.17, {/Symbol s}_z=5.59" at 0.5,138
plot "dispv14v11v0.dat" using 1:2,  "dispv14v11v1.dat" using 1:2,  "dispv14v11v2.dat" using 1:2,  "dispv14v11v3.dat" using 1:2
#set terminal x11


