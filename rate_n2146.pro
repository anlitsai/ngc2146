PRO rate

; --- SN rate -----------------------------------------	;
; r_SN=2.3e-12*L_FIR
; r_SN: SN rate [yr^-1]
; L_FIR: IRAS FIR luminosity [L_sun]
L_FIR_n2146=6.6e10	; IRAS (Tarchi 2000)
r_SN_n2146=2.3e-12*L_FIR_n2146	; (van Buren & Greenhouse 1994)
print,"NGC 2146 SN rate [per yr]", r_SN_n2146
; unit checked

; --- SF rate -----------------------------------------	;
; Lsun_to_Lerg=3.98e33
ind_Lsun_to_Lerg=33+alog10(3.98)
pc_to_cm=3.26*3.0e10*365*86400
ind_pc_to_cm=alog10(pc_to_cm)
dia_n2146=64.0*80
r_mpc=21.0

F_Ha=32.0e-12	; [erg/s/cm2] in 64" (Young 1988)
ind_F_Ha=alog10(F_Ha)
; L_Ha=F_ha*4*!pi*(r_mpc*1.0e6*pc_to_cm)^2
ind_L_Ha=ind_F_Ha+alog10(4*!pi)+2*(alog10(r_mpc)+6+ind_pc_to_cm)
; SFR=1.0e-41*L_Ha	; (Thronson 1991)
ind_SFR=-41+ind_L_Ha
SFR=10^ind_SFR
print,"NGC 2146 SFR [M_sun/yr]",SFR

; L_Ha=2.0e11*Lsun_to_Lerg
ind_L_Ha=11.0+alog10(2.0)+ind_Lsun_to_Lerg
ind_SFR=-41+ind_L_Ha
SFR=10^ind_SFR/86400/365
print,"NGC 2146 SFR [M_sun/yr]",SFR

; -----------------------------------------------------	;
; Tarchi et al. 2000, AA, 358, 95
; Thronson et al. 1991, MNRAS, 252,543
; van Buren & Greenhouse 1994, ApJ, 431, 640
; Young et al. 1988 ApJ, 334, L63

RETURN
END

