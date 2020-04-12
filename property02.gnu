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
set label 11 "R^2 = 0.69" at 1800,25 font "Helvetica,24"

f1(x)=a1+b1*x
fit [x=0:2500][0:300]f1(x) "property.dat" using 3:5:6 via a1,b1 w yerrorbars
f11(x)=a11+b11*x
fit [x=0:2500][0:300]f11(x) "property.dat" using 3:5 via a11,b11 


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
set label 21 "R^2 = 0.60" at 1800,50 font "Helvetica,24"


f2(x)=a2+b2*x
fit [x=0:2500][0:500]f2(x) "property.dat" using 3:9:10 via a2,b2 w yerrorbars
f21(x)=a21+b21*x
fit [x=0:2500][0:500]f21(x) "property.dat" using 3:9 via a21,b21

plot [x=0:2500][0:600] \
f21(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12


# ----------------------------
set output "property_R_E_fit.ps"
set size 0.7,0.7

set xlabel "Size  [pc]"
set ylabel "Kinetic Energy  [10^{53} erg]"
#set title "R vs. E_{kinetic}"
unset label
set label 3 "(d)" at 100,560 font "Helvetica,24"
set label 31 "R^2 = 0.51" at 1800,50 font "Helvetica,24"

f3(x)=a3+b3*x
fit [x=0:2500][0:400]f3(x) "property.dat" using 3:11:12 via a3,b3 w yerrorbars
f31(x)=a31+b31*x
fit [x=0:2500][0:400]f31(x) "property.dat" using 3:11 via a31,b31

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
set xlabel "Size  [pc]"
set ylabel "Mass Loss Rate  [M_{sun} / yr]"
#set title "R vs. dM/dt"
unset label
set label 4 "(f)" at 100,56 font "Helvetica,24"
set label 41 "R^2 = 0.39" at 1800,5 font "Helvetica,24"

f4(x)=a4+b4*x 
fit [x=0:2500][0:50]f4(x) "property.dat" using 3:13:14 via a4,b4 w yerrorbars
f41(x)=a41+b41*x 
fit [x=0:2500][0:50]f41(x) "property.dat" using 3:13 via a41,b41 


plot [x=0:2500][0:60] \
f41(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12



# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_R_T_fit.ps"
set xlabel "Size  R [pc]"
set ylabel "t  [Myr]"
#set title ""

f5(x)=a5+b5*x 
fit [x=0:2500][0:50]f5(x) "property.dat" using 3:7:8 via a5,b5 w yerrorbars
f51(x)=a51+b51*x 
fit [x=0:2500][0:50]f51(x) "property.dat" using 3:7 via a51,b51 


plot [x=0:2500][0:50] \
f51(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):7:4:8 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):7:4:8 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):7:4:8 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 2, \
"property.dat" using ($1<1 && $1>-1 ? $3 : 1/0):7:4:8 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9


# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_E_dM_fit.ps"
set xlabel "Kinetic Energy  [10^{53} erg]"
set ylabel "Mass Loss Rate  [M_{sun} / yr]"
#set title "E_{kinetic} vs. dM/dt"
unset label
set label 6 "(e)" at 15,56 font "Helvetica,24"
set label 61 "R^2 = 0.94" at 290,5 font "Helvetica,24"

f6(x)=a6+b6*x 
fit [x=0:2500][0:50]f6(x) "property.dat" using 11:13:14 via a6,b6 w yerrorbars
f61(x)=a61+b61*x 
fit [x=0:2500][0:50]f61(x) "property.dat" using 11:13 via a61,b61 


plot [x=0:400][0:60] \
f61(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $11 : 1/0):13:12:14 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12




# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_V_dM_fit.ps"
set xlabel "v [km/s]"
set ylabel "dM/dt  [M_{sun} / yr]"
#set title ""

f7(x)=a7+b7*x
fit [x=0:300][0:50]f7(x) "property.dat" using 5:13:14 via a7,b7 w yerrorbars
f71(x)=a71+b71*x
fit [x=0:300][0:50]f71(x) "property.dat" using 5:13 via a71,b71


plot [x=0:300][0:50] \
f71(x) ti "R^2=0.967" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $5 : 1/0):13:6:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $5 : 1/0):13:6:14 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $5 : 1/0):13:6:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 2, \
"property.dat" using ($1<1 && $1>-1 ? $5 : 1/0):13:6:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9




# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_V_M_fit.ps"
set xlabel "Expanding Velocity  [km/s]"
set ylabel "Mass  [10^6 M_{sun}]"
#set title "v_{exp} vs. M"
unset label
set label 8 "(c)" at 10,560 font "Helvetica,24"
set label 81 "R^2 = 0.03" at 220,50 font "Helvetica,24"

f8(x)=a8+b8*x
fit [x=0:300][0:500]f8(x) "property.dat" using 5:9:10 via a8,b8 w yerrorbars
f81(x)=a81+b81*x
fit [x=0:300][0:500]f81(x) "property.dat" using 5:9 via a81,b81


plot [x=0:300][0:600] \
f81(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $5 : 1/0):9:6:10 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12


# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_M_T_fit.ps"
set xlabel "Mass  [10^{6} M_{sun}]"
set ylabel "Expanding Timescale  [Myr]"
#set title "M vs. t_{exp}"
unset label
set label 9 "" at 2,460 font "Helvetica,24"
set label 91 "R^2 = 0.00" at 37,5 font "Helvetica,24"

f9(x)=a9+b9*x
fit [x=0:50][0:500]f9(x) "property.dat" using 9:7:8 via a9,b9 w yerrorbars
f91(x)=a91+b91*x
fit [x=0:50][0:500]f91(x) "property.dat" using 9:7 via a91,b91


plot [x=0:50][0:500] \
f91(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $9 : 1/0):7:10:8 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $9 : 1/0):7:10:8 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $9 : 1/0):7:10:8 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 2, \
"property.dat" using ($1<1 && $1>-1 ? $9 : 1/0):7:10:8 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9


# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_T_M_fit.ps"
set xlabel "Expanding Timescale  [Myr]"
set ylabel "Mass  [10^{6} M_{sun}]"
#set title "t_{exp} vs. M"
unset label
set label 10 "(g)" at 2,560 font "Helvetica,24"
set label 101 "R^2 = 0.00" at 37,70 font "Helvetica,24"

f10(x)=a10+b10*x
fit [x=0:50][0:500]f10(x) "property.dat" using 7:9:10 via a10,b10 w yerrorbars
f101(x)=a101+b101*x
fit [x=0:50][0:500]f101(x) "property.dat" using 7:9 via a101,b101


plot [x=0:50][0:600] \
f101(x) ti "" lt 2 lw 2, \
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
set label 111 "R^2 = 0.00" at 37,50 font "Helvetica,24"

f11(x)=a11+b11*x
fit [x=0:50][0:500]f11(x) "property.dat" using 7:9:10 via a11,b11 w yerrorbars
f111(x)=a111+b111*x
fit [x=0:50][0:500]f111(x) "property.dat" using 7:9 via a111,b111


plot [x=0:50][0:600] \
f111(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 13, \
"property.dat" using ($1<1 && $1>-1 && $2>1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 1 pt 5, \
"property.dat" using ($1<1 && $1>-1 && $2<1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "M82 SB (Matsushita et al. 2000)" lt 3 lw 1 pt 4, \
"property.dat" using ($1<-1 && $2<1 ? $7 : 1/0):11:8:12 w xyerrorbars ti "NGC 253 SB (Sakamoto et al. 2006)" lt 3 lw 1 pt 12



# ----------------------------
set terminal postscript enhanced color
set size 0.7,0.7

set output "property_E_T_fit.ps"
set xlabel "Kinetic Energy  [10^{53} erg]"
set ylabel "Expanding Timescale  [Myr]"
#set title "E_{kinetic} vs. t_{exp}"
unset label
set label 12 "" at 10,46 font "Helvetica,24"
set label 121 "R^2 = 0.00" at 370,5 font "Helvetica,24"

f12(x)=a12+b12*x
fit [x=0:500][0:50]f12(x) "property.dat" using 7:9:10 via a12,b12 w yerrorbars
f121(x)=a121+b121*x
fit [x=0:500][0:50]f121(x) "property.dat" using 7:9 via a121,b121


plot [x=0:500][0:50] \
f121(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $11 : 1/0):7:12:8 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $11 : 1/0):7:12:8 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $11 : 1/0):7:12:8 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 2, \
"property.dat" using ($1<1 && $1>-1 ? $11 : 1/0):7:12:8 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9




# -------------------------------------------

set output "property_SFR_dM.ps"
set xlabel "SFR  [M_{sun} / yr]"
set ylabel "dM/dt  [M_{sun} / yr]"
#set title "SFR vs. dM/dt"
unset label
set label 13 "" at 10,46 font "Helvetica,24"
set label 131 "R^2 = 0.00" at 37,5 font "Helvetica,24"


f13(x)=a13+b13*x
fit [x=0:50][0:50]f13(x) "property.dat" using 15:13:14 via a13,b13 w yerrorbars
f131(x)=a131+b131*x
fit [x=0:50][0:50]f131(x) "property.dat" using 15:13 via a131,b131


plot [x=0:50][0:50] \
f131(x) ti "" lt 2 lw 2, \
"property.dat" using ($1>3 && $2>1 ? $15 : 1/0):13:16:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1<3 && $1>1 ? $15 : 1/0):13:16:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 2, \
"property.dat" using ($1<1 && $1>-1 ? $15 : 1/0):13:16:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9
#property.dat" using ($1>3 && $2<1 ? $13 : 1/0):15:4:16 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \


# -------------------------------------------

set output "property_SFR_zeta.ps"
set xlabel "SFR  [M_{sun} / yr]"
set ylabel "{/Symbol z}"
#set title "SFR vs. {/Symbol z}"
unset label
set label 14 "" at 10,46 font "Helvetica,24"
set label 141 "R^2 = 0.00" at 37,0.5 font "Helvetica,24"

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
"property.dat" using ($1<1 && $1>-1 ? $15 : 1/0):17:16:18 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9
#"property.dat" using ($1<-1  ? $15 : 1/0):17:16:18 w xyerrorbars ti "NGC 253 (Sturm et al. 2011)" lt 3 lw 2 pt 11




# exit
