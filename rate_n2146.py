#!/usr/bin/env python

import math

# --- SN rate -----------------------------------------	;
# r_SN=2.3e-12*L_FIR
# r_SN: SN rate [yr^-1]
# L_FIR: IRAS FIR luminosity [L_sun]
L_FIR=6.6e10	# IRAS (Tarchi 2000)
r_SN=2.3e-12*L_FIR	# (van Buren & Greenhouse 1994)
print "NGC 2146 SN rate (FIR) [per yr]", r_SN
# unit checked

# --- SF rate -----------------------------------------	;
Lsun_to_Lerg=3.98e33
pc_to_cm=3.26*3.0e10*365*86400
dia_n2146=64.0*80
r_mpc=21.0

F_Ha=32.0e-12	# [erg/s/cm2] in 64" (Young 1988)
L_Ha=F_Ha*4*math.pi*(r_mpc*1.0e6*pc_to_cm)**2
SFR=1.0e-41*L_Ha	# (Thronson 1991)
print "NGC 2146 SFR(Ha) [M_sun/yr]",SFR

L_Ha=2.0e11*Lsun_to_Lerg	# ref?
SFR=1.0e-41*L_Ha	# (Thronson 1991)
print "NGC 2146 SFR(Ha) [M_sun/yr]",SFR

# -----------------------------------------------------	;
# Tarchi et al. 2000, AA, 358, 95
# Thronson et al. 1991, MNRAS, 252,543
# van Buren & Greenhouse 1994, ApJ, 431, 640
# Young et al. 1988 ApJ, 334, L63

exit
