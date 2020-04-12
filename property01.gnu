#

set terminal postscript enhanced color
set size 0.7,0.7
#set size 0.6,0.6
#set style fill solid border -1
#plot "sb_evolution.dat" using 1:2:3:4 with xyerrorbars
set style line
# ----------------------------

set output "property_R_V.ps"

#set label "NGC 2146" at 0.3,1.5
#set label "NGC 3628" at 0.02,0.8
#set label "M82" at 0.6,0.35

set xlabel "Size  R [pc]"
set ylabel "Velocity  v [km/s]"
set title ""





plot [x=0:2500][0:300] \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):5:4:6 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 7, \
"property.dat" using ($1<1  ? $3 : 1/0):5:4:6 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9


# ----------------------------

set output "property_R_M.ps"
set xlabel "Size  R [pc]"
set ylabel "Mass  10^7 [M_{sun}]"
set title ""

plot [x=0:2500][0:50] \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):9:4:10 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 7, \
"property.dat" using ($1<1  ? $3 : 1/0):9:4:10 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9


# ----------------------------
set output "property_R_E.ps"
set xlabel "Size  R [pc]"
set ylabel "E_{kinetic}  10^{53} [erg]"
set title ""

plot [x=0:2500][0:500] \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 7, \
"property.dat" using ($1<1 ? $3 : 1/0):11:4:12 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9


# ----------------------------
#set output "property_R_logE.ps"
#set xlabel "Size  R [pc]"
#set ylabel "log 10^{53} E_{kinetic} [erg]"
#set title ""
#
#plot [x=0:2500][1:500] \
#"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):(53+log($11)):4:(log($12)) w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
#"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):(53+log($11)):4:(log($12)) w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
#"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):(53+log($11)):4:(log($12)) w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 7, \
#"property.dat" using ($1<1  ? $3 : 1/0):(53+log($11)):4:(log($12)) w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9





# ----------------------------
set output "property_R_dM.ps"
set xlabel "Size  R [pc]"
set ylabel "dM/dt  [M_{sun} / yr]"
set title ""

plot [x=0:2500][0:50] \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 7, \
"property.dat" using ($1<1  ? $3 : 1/0):13:4:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9


# ----------------------------
set output "property_R_dM.ps"
set xlabel "Size  R [pc]"
set ylabel "dM/dt  [M_{sun} / yr]"
set title ""

plot [x=0:2500][0:50] \
"property.dat" using ($1>3 && $2>1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
"property.dat" using ($1>3 && $2<1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $3 : 1/0):13:4:14 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 7, \
"property.dat" using ($1<1  ? $3 : 1/0):13:4:14 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9




# ----------------------------
set output "property_dM_SFR.ps"
set xlabel "dM/dt  [M_{sun} / yr]"
set ylabel "SFR  [M_{sun} / yr]"
set title ""

plot [x=0:2500][0:50] \
"property.dat" using ($1>3 && $2>1 ? $13 : 1/0):15:4:16 w xyerrorbars ti "NGC 2146 OF" lt 1 lw 2 pt 5, \
#property.dat" using ($1>3 && $2<1 ? $13 : 1/0):15:4:16 w xyerrorbars ti "NGC 2146 SB" lt 1 lw 2 pt 4, \
"property.dat" using ($1<3 && $1>1 ? $13 : 1/0):15:4:16 w xyerrorbars ti "NGC 3628 OF" lt 1 lw 2 pt 7, \
"property.dat" using ($1<1  ? $13 : 1/0):15:4:16 w xyerrorbars ti "M82 OF (Walter et al. 2002)" lt 3 lw 2 pt 9








# -------------------------------------------



# exit
