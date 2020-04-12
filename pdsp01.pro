PRO pdsp

;Vr(R,i) = Vsys + V(R)sin(i)cos(phi)
;----- const -----
pi = !pi/180
;pi = 3.14159267D/180
R_rig=10
R_fla=30
R=R_rig+R_fla
;----- default -----
!P.MULTI=[0,3,2]
window,0,retain=2,xsize=1200,ysize=800
device,set_character_size=[16,18]
;set_plot,'PS'
;device,filename='rotation_curve_5types.ps',/landscape
;----- constant -----
Ei=7
n0i=2
tyri=4

T_k=fltarr(Ei,n0i,tyri)

for i=0,Ei-1 do begin
  E=10.0^i
  for j=0,n0i-1 do begin
    n0=100.0*10.0^j
    for k=0,tyri-1 do begin
      t_yr=1.0e4*10.0^k
      T_k[i,j,k]=5.4e6*(E/1.0e51/n0)^(2.0/5)*(t_yr/1.0e4)^(-6.0/5)
    endfor
  endfor
endfor




;========== content ==========

;plot,vc_rig,vc_vor,vc_fla,vc_elm,vc_mod
plot,T_k,title="T_k", xtitle="radius",ytitle="velocity"



; ---------------------------------------------------------------
;device,/close_file

RETURN
END


