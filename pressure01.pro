PRO pressure

; --- constant --------------------------------	;
pc_to_cm=3.26*3e10*365*86400
ind_pc_to_cm=alog10(pc_to_cm)
ev_to_erg=1.6e-12
G=6.67e-8 ; gravitational constant
k_B=1.38e-16 ; boltzmann constant
c=3.0e10 ; light speed
M_sun=1.99e33 ; solar mass
L_sun=3.9e33 ; solar luminosity
N_A=6.02e23 ; Avogadro constant
m_p=1.67e-24
; --- parameter -------------------------------	;
v_otf_kms=200.0 ; km/s (Tsai et al. 2009)
v_otf_cms=v_otf_kms*1.0e5 ; cm/s
T_mol=30.0 ; K (Tsai et al. 2009)
T_xry=1.0e6 ; K
n_mol=100.0 ; cm^-3 (Tsai et al. 2009)
M_mol=3.4e8*L_sun ; (Tsai et al. 2009)
ind_EI=62.0+alog10(8.0) ; (Inui et al. 2005)
ind_V_xryotf=alog10(3.0/4.0*!pi)+3*alog10(6.3*1000*4.8/3.5*pc_to_cm) ; (Inui et al. 2005)
fill=0.03 ; (Inui et al. 2005)
ind_fill=alog10(fill)
; n_xry=(EI/V*f)^(-0.5) ; cm^-3 (Iuni et al. 2005)
ind_n_xry=0.5*(ind_EI-ind_V_xryotf-ind_fill) ; cm^-3 (Iuni et al. 2005)
n_xry=10^ind_n_xry
kT_xry=0.5*100*ev_to_erg
; M_xry=n_xry*m_p*V_xryotf*fill
ind_M_xry=ind_n_xry+alog10(m_p)+ind_V_xryotf+ind_fill
M_xry=10^ind_M_xry
print,ind_EI,ind_V_xryotf,ind_fill,ind_n_xry,n_xry
; E_xry=1.0e56
ind_E_xry=56.0 ; (Inui et al. 2005)
R_mol=2.0e3*pc_to_cm ; (Tsai et al. 2009)
SFR=10.0 ; M_sun/yr (Greve et al. 2000)
ind_SFR=alog10(SFR)
SNRate= 0.15 ; yr^-1 (Tarchi et al. 2000)
ind_SNRate=alog10(0.15)
effi=0.001 ; (Thompson et al. 2005)
as_to_pc=80.0
I_CO_gal_pc2=1.8e3 ; within 1.0e7 pc^2 (Tsai et al. 2009)
I_CO_otf_pc2=150.0 ; (Tsai et al. 2009)
I_CO_sbl_pc2=115.0 ; (Tsai et al. 2009)
I_CO_disk_pc2=I_CO_gal_pc2-I_CO_otf_pc2-I_CO_sbl_pc2
; I_CO_gal_as2=I_CO_gal_pc2/(1.0e7/as_to_pc^2)
I_CO_otf_as2=I_CO_otf_pc2/(1.0e7/as_to_pc^2)
; I_CO_sbl_as2= 
thick_pc=300.0
R_starburst_pc=700.0 ; (@tau=1; Thompson et al. 2005)
R_starburst_pc=1000.0 ; (our data)
tau=10.0

; --- gravitational pressure (Gunn & Gott 1972) -------	;
I_CO_disk_pc2=I_CO_gal_pc2-I_CO_otf_pc2-I_CO_sbl_pc2
; I_CO_gal_as2=I_CO_gal_pc2/(1.0e7/as_to_pc^2)
; I_CO_gal=I_CO_gal-I_CO_otf-I_CO_sbl
; surf_den_mol[M_sun/pc^2]=6.5e2*I(CO)[Jy km/s as^(-2)] ; (Sakamoto et al. 1995)
; surf_den_mol[M_g/cm^2]=surf_den_mol[M_sun/pc^2]*Msun_pc2_to_Mg_cm2
Msun_pc2_to_Mg_cm2=M_sun/pc_to_cm^2
; surf_den_gal=6.5e2*I_CO_gal*Msun_pc2_to_Mg_cm2
a_I=6.5e2*Msun_pc2_to_Mg_cm2
ind_a_I=alog10(a_I)
ind_surf_den_mol=ind_a_I+alog10(I_CO_otf_as2)+2*ind_pc_to_cm
surf_den_mol=10^ind_surf_den_mol
surf_den_xry=surf_den_mol*n_xry/n_mol*M_xry/M_mol
ind_surf_den_xry=ind_surf_den_mol+ind_n_xry-alog10(n_mol)+ind_M_xry-alog10(M_mol)
print,surf_den_xry,surf_den_mol
print,M_sun/pc_to_cm^2
print,ind_surf_den_xry,ind_surf_den_mol
; ind_surf_den_gal=ind_a_I+alog10(I_CO_gal)
; surf_den_otf=6.5e2*I_CO_otf*Msun_pc2_to_Mg_cm2
; ind_surf_den_otf=ind_a_I+alog10(I_CO_otf)
; p_grav=2*!pi*G*surf_den_gal*surf_den_otf
; ind_p_grav=alog10(2*!pi*G)+ind_surf_den_gal+ind_surf_den_otf
ind_p_grav=alog10(2*!pi*G)+ind_surf_den_mol+ind_surf_den_xry
; surf_den_gal:surface mass density of galaxy
; surf_den_otf:surface mas density of outflow
print, "grav P, log", ind_p_grav
; unit checked

; --- ram pressure (Gunn & Gott 1972) -----------------	;
; p_ram=rho_mol*v_xry^2
; p_ram=rho_mol*v_xry^2=(m/V)(2*E_xry/m)=2*E_xry/(1/2*4/3*!pi*R^3)=E_xry/R^3
;p_ram=E_xry/R_mol^3
; ind_p_ram=ind_E_xry-3*alog10(R_mol)
; p_ram=rho_mol*v_otf^2
rho_mol=n_mol/N_A
ind_p_ram=alog10(rho_mol)+2*alog10(v_otf_cms)
print, "ram P, log ",ind_p_ram
; unit checked

; --- shock heated pressure (Thompson et al 2005) -----	;
; SNRate_V=SNRate/V_starburst
; V_starburst=A_starburst*thick
; A_starburst=!pi*R_starburst^2
A_starburst_pc2=!pi*R_starburst_pc^2
V_starburst_pc3=A_starburst_pc2*thick_pc
SNRate_V=SNRate/V_starburst_pc3
ind_SNRate_V=alog10(SNRate_V)
ind_E_init=ind_E_xry
n_ambi=n_mol
; p_shk=1.0e-12*(E_init/1.0e51)^(17/14)*(n_ambi/0.01)^(-4/7)*(SNRate_V/1.0e-13) [erg cm^-3]
; E_init [erg]
; n_ambi [cm^-3]
; SNRate_V [yr^-1 pc^-3]
ind_p_shk=0.0-12.0+(17.0/14.0)*(ind_E_init-51.0)-(4.0/7.0)*alog10(n_ambi/0.01)+ind_SNRate_V-13.0
; SNRate_V=SNRateate per volume
print, "remnant expanded shock P, log", ind_p_shk
; unit checked

; --- thermal pressure --------------------------------	;
p_thm_mol=n_mol*k_B*T_mol
ind_p_thm_mol=alog10(p_thm_mol)
p_thm_xry=n_xry*kT_xry
ind_p_thm_xry=alog10(p_thm_xry)
p_thm_xry_inui=4.9e-12*fill^(-0.5)
ind_p_thm_xry_inui=alog10(p_thm_xry_inui)
print, "molecular gas thermal P, log", ind_p_thm_mol
print, "ionized gas thermal P, log", ind_p_thm_xry
print, "ionized gas thermal P(Inui), log", ind_p_thm_xry_inui
; unit checked

; --- radiation pressure (Thompson et al 2005) --------	;
; SFR_A=SFR/(A_starburst)
; A_starburst_cm2=A_starburst_pc2*pc_to_cm^2
ind_A_starburst_pc2=alog10(A_starburst_pc2)
ind_A_starburst_cm2=ind_A_starburst_pc2+2*ind_pc_to_cm
; SFR_A_cm2=SFR/(A_starburst_cm2)
ind_SFR_A_cm2=alog10(SFR)-ind_A_starburst_cm2
; when tau << 1
; p_rad_thin=c*effi*SFR_A
ind_p_rad_thin=alog10(c)+alog10(effi)+ind_SFR_A_cm2
; when tau >= 1
; p_rad_thick=c*effi*SFR_A*(1/2)*tau
ind_p_rad_thick=ind_p_rad_thin+alog10(0.5)+alog10(tau)
print, "optically thin radiation P, log", ind_p_rad_thin
print, "optically thick radiation P, log", ind_p_rad_thick
; unit checked

; --- SN explosion pressure (Thompson et al 2005) -----	;
; E_init=E_xry
; n_ambi=n_mol
; p_SN=5*(n_ambi/1.0)^(-1/4)*(E_init/1.0e51)^(13/14)*p_ram
ind_p_SN=alog10(5.0)-0.25*alog10(n_ambi)+(13.0/14.0)*(ind_E_init-51.0)+ind_p_rad_thick
print, "SN explosion pressure, log",  ind_p_SN
; unit checked

; ---------------------------------------------	;

; --- reference -------------------------------	;
; Greve et al. 2000, AA, 364, 409
; Gunn & Gott 1972, ApJ, 176, 1
; Inui et al. 2005, PASJ, 57, 135
; Sakamoto et al. 1995, AJ, 110, 2075
; Tarchi et al. 2000, 358, 95
; Tsai et al. 2009, PASJ, 61, 237
; Thompson et al. 2005, ApJ, 630, 167
; Vollmer et al. 2001, ApJ, 561, 708
; Vollmer et al. 2005, AA, 441, 473

RETURN
END

