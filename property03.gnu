#

set terminal postscript enhanced color
set size 0.7,0.7
#set size 0.6,0.6
#set style fill solid border -1
#plot "sb_evolution.dat" using 1:2:3:4 with xyerrorbars
set style line
set fit logfile 'fit.log'
# ----------------------------

set output "property_R_V_fit.ps"
set xlabel "Size  [pc]"
set ylabel "Expanding Vlocity  [km/s]"
#set title "R vs. v_{exp}"
unset label
set label 1 "(a)" at 100,360 font "Helvetica,24"
set label 11 "{/Symbol G}^2 = 0.47" at 1800,25 font "Helvetica,24"

#f1(x)=a1+b1*x
#fit [x=0:2500][0:300]f1(x) "property.2.dat" using 3:5:6 via a1,b1 w yerrorbars
f11(x)=a11+b11*x
fit [x=0:2500][0:300]f11(x) "property.2.dat" using 3:5 via a11,b11 


plot [x=0:2500][0:400]\
f11(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12


# ----------------------------

set output "property_R_M_fit.ps"
set xlabel "Size  [pc]"
set ylabel "Mass  [10^6 M_{sun}]"
#set title "R vs. M"
unset label
set label 2 "(b)" at 100,560 font "Helvetica,24"
set label 21 "{/Symbol G}^2 = 0.75" at 1800,50 font "Helvetica,24"


#f2(x)=a2+b2*x
#fit [x=0:2500][0:500]f2(x) "property.2.dat" using 3:9:10 via a2,b2 w yerrorbars
f21(x)=a21+b21*x
fit [x=0:2500][0:500]f21(x) "property.2.dat" using 3:9 via a21,b21

plot [x=0:2500][0:600] \
f21(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12

# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_V_M_fit.ps"
set xlabel "Expanding Velocity  [km/s]"
set ylabel "Mass  [10^6 M_{sun}]"
#set title "v_{exp} vs. M"
unset label
set label 8 "(c)" at 10,560 font "Helvetica,24"
set label 81 "{/Symbol G}^2 = 0.63" at 220,50 font "Helvetica,24"

#f8(x)=a8+b8*x
#fit [x=0:300][0:500]f8(x) "property.2.dat" using 5:9:10 via a8,b8 w yerrorbars
f81(x)=a81+b81*x
fit [x=0:300][0:500]f81(x) "property.2.dat" using 5:9 via a81,b81


plot [x=0:300][0:600] \
f81(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12


# ----------------------------
set output "property_R_E_fit.ps"
set size 0.7,0.7

set xlabel "Size  [pc]"
set ylabel "Kinetic Energy  [10^{53} erg]"
#set title "R vs. E_{kinetic}"
unset label
set label 3 "(d)" at 100,560 font "Helvetica,24"
set label 31 "{/Symbol G}^2 = 0.61" at 1800,50 font "Helvetica,24"

#f3(x)=a3+b3*x
#fit [x=0:2500][0:400]f3(x) "property.2.dat" using 3:11:12 via a3,b3 w yerrorbars
f31(x)=a31+b31*x
fit [x=0:2500][0:400]f31(x) "property.2.dat" using 3:11 via a31,b31

plot [x=0:2500][0:600] \
f31(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12




# ----------------------------
set output "property_R_dM_fit.ps"
set xlabel "Mass Loss Rate  [M_{sun} / yr]"
set ylabel "Size  [pc]"
#set title "R vs. dM/dt"
unset label
set label 4 "(f)" at 5,2800 font "Helvetica,24"
set label 41 "{/Symbol G}^2 = 0.42" at 36,200 font "Helvetica,24"

#f4(x)=a4+b4*x 
#fit [x=0:2500][0:200]f4(x) "property.2.dat" using 3:13:14 via a4,b4 w yerrorbars
f41(x)=a41+b41*x 
fit [x=0:200][0:3000]f41(x) "property.2.dat" using 13:3 via a41,b41 


plot [x=0:50][0:3000] \
f41(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $13 : 1/0):3:14:4 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $13 : 1/0):3:14:4 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $13 : 1/0):3:14:4 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $13 : 1/0):3:14:4 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $13 : 1/0):3:14:4 w xyerrorbars ti "" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $13 : 1/0):3:14:4 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12



# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_E_dM_fit.ps"
set xlabel "Kinetic Energy  [10^{53} erg]"
set ylabel "Mass Loss Rate  [M_{sun} / yr]"
#set title "E_{kinetic} vs. dM/dt"
unset label
set label 6 "(f)" at 15,56 font "Helvetica,24"
set label 61 "{/Symbol G}^2 = 0.92" at 290,5 font "Helvetica,24"

#f6(x)=a6+b6*x 
#fit [x=0:2500][0:50]f6(x) "property.2.dat" using 11:13:14 via a6,b6 w yerrorbars
f61(x)=a61+b61*x 
fit [x=0:2500][0:50]f61(x) "property.2.dat" using 11:13 via a61,b61 


plot [x=0:400][0:60] \
f61(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<-1 && $2<1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12
#"property.dat" using ($1<1 && $1>-1 && $2<1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \





# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_T_M_fit.ps"
set xlabel "Expanding Timescale  [Myr]"
set ylabel "Mass  [10^{6} M_{sun}]"
#set title "t_{exp} vs. M"
unset label
set label 10 "(g)" at 2,560 font "Helvetica,24"
set label 101 "{/Symbol G}^2 = 0.20" at 37,70 font "Helvetica,24"

#f10(x)=a10+b10*x
#fit [x=0:50][0:500]f10(x) "property.2.dat" using 7:9:10 via a10,b10 w yerrorbars
f101(x)=a101+b101*x
fit [x=0:50][0:500]f101(x) "property.2.dat" using 7:9 via a101,b101


#f101(x) ti "" lt 2 lw 2, \
plot [x=0:50][0:600] \
"property.dat" using ($1>3 && $2>1 ? $7 : 1/0):9:8:10 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $7 : 1/0):9:8:10 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $7 : 1/0):9:8:10 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $7 : 1/0):9:8:10 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $7 : 1/0):9:8:10 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $7 : 1/0):9:8:10 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12

# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_T_E_fit.ps"
set xlabel "Expanding Timescale  [Myr]"
set ylabel "Kinetic Energy  [10^{53} erg]"
#set title "t_{exp} vs. E_{kinetic}"
unset label
set label 11 "(h)" at 2,560 font "Helvetica,24"
set label 111 "{/Symbol G}^2 = 0.03" at 37,50 font "Helvetica,24"

#f11(x)=a11+b11*x
#fit [x=0:50][0:500]f11(x) "property.2.dat" using 7:9:10 via a11,b11 w yerrorbars
f111(x)=a111+b111*x
fit [x=0:50][0:500]f111(x) "property.2.dat" using 7:9 via a111,b111


#f111(x) ti "" lt 2 lw 2, \
plot [x=0:50][0:600] \
"property.dat" using ($1>3 && $2>1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12


# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_T_dM_fit.ps"
set xlabel "Expanding Timescale  [Myr]"
set ylabel "Mass Loss Rate  [10^6 M_{sun} yr^{-1}]"
#set title "t_{exp} vs. E_{kinetic}"
unset label
set label 11 "(j)" at 2,56 font "Helvetica,24"
set label 111 "{/Symbol G}^2 = 0.0" at 37,5 font "Helvetica,24"

#f11(x)=a11+b11*x
#fit [x=0:50][0:500]f11(x) "property.2.dat" using 7:9:10 via a11,b11 w yerrorbars
f151(x)=a151+b151*x
fit [x=0:50][0:50]f151(x) "property.3.dat" using 7:13 via a151,b151


plot [x=0:50][0:60] \
f151(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $7 : 1/0):13:8:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $7 : 1/0):13:8:14 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $7 : 1/0):13:8:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $7 : 1/0):13:8:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $7 : 1/0):13:8:14 w xyerrorbars ti "" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $7 : 1/0):13:8:14 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12



# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_SFR_dM.png"
set output "property_SFR_dM.ps"
set xlabel "SFR  [M_{sun} / yr]"
set ylabel "dM/dt  [M_{sun} / yr]"
#set title "SFR vs. dM/dt"
unset label
set label 13 "" at 10,46 font "Helvetica,24"
#set label 131 "{/Symbol G}^2 = 0.02" at 37,5 font "Helvetica,24"


f13(x)=a13+b13*x
fit [x=0:50][0:50]f13(x) "property.dat" using 15:13:14 via a13,b13 w yerrorbars
f131(x)=a131+b131*x
fit [x=0:50][0:50]f131(x) "property.dat" using 15:13 via a131,b131
f132(x)=x

plot [x=0:30][0:50] \
f132(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $15 : 1/0):13:16:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1<3 && $1>1 ? $15 : 1/0):13:16:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 4, \
"property.dat" using ($1<1 && $1>-1 ? $15 : 1/0):13:16:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 12
#property.dat" using ($1>3 && $2<1 ? $13 : 1/0):15:4:16 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \


# -------------------------------------------

set terminal postscript enhanced color
set size 0.7,0.7

set output "property_SFR_dM.ps"
set xlabel "SFR  [M_{sun} / yr]"
set ylabel "dM/dt  [M_{sun} / yr]"
#set title "SFR vs. dM/dt"
unset label
set label 13 "" at 10,46 font "Helvetica,24"
#set label 131 "{/Symbol G}^2 = 0.02" at 37,5 font "Helvetica,24"


f16(x)=a16+b16*x
fit [x=0:50][0:50]f16(x) "property.dat" using 19:13:14 via a16,b16 w yerrorbars
f161(x)=a161+b161*x
fit [x=0:50][0:50]f161(x) "property.dat" using 19:13 via a161,b161
f162(x)=x

plot [x=0:30][0:50] \
f162(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $19 : 1/0):13:20:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1<3 && $1>1 ? $19 : 1/0):13:20:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 4, \
"property.dat" using ($1<1 && $1>-1 ? $19 : 1/0):13:20:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 12






# -------------------------------------------

set output "property_SFR_zeta.ps"
set xlabel "SFR  [M_{sun} / yr]"
set ylabel "{/Symbol z}"
#set title "SFR vs. {/Symbol z}"
unset label
set label 14 "" at 10,46 font "Helvetica,24"
#set label 141 "{/Symbol G}^2 = 0.00" at 37,0.5 font "Helvetica,24"

f140(x)=a140
fit [x=0:50][0:5]f140(x) "property.dat" using 15:17 via a140
f14(x)=a14+b14*x
fit [x=0:50][0:5]f14(x) "property.dat" using 15:17:18 via a14,b14 w yerrorbars
f141(x)=a141+b141*x
fit [x=0:50][0:5]f141(x) "property.dat" using 15:17 via a141,b141


plot [x=0:50][0:5] \
f140(x) ti "" lt 2 lw 2,\
"property.dat" using ($1>3 && $2>1 ? $15 : 1/0):17:16:18 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1<3 && $1>1 ? $15 : 1/0):17:16:18 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 2, \
"property.dat" using ($1<1 && $1>-1 ? $15 : 1/0):17:16:18 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 12
#"property.dat" using ($1<-1  ? $15 : 1/0):17:16:18 w xyerrorbars ti "NGC 253 (Sturm et al. 2011)" lt 3 lw 2 pt 11




# exit
