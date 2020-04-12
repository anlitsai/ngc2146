PRO property

l=18
m=8
openr, lun, 'property.2.dat',/get_lun
data=fltarr(l,m)
readf,lun,data
close, lun
radi=fltarr(m)

radi=fltarr(m)
vexp=fltarr(m)
texp=fltarr(m)
mass=fltarr(m)
Ekin=fltarr(m)
dm=fltarr(m)


for i=0,m-1 do begin
	radi[i]=data[3,i]
	vexp[i]=data[5,i]
	texp[i]=data[7,i]
	mass[i]=data[9,i]
	Ekin[i]=data[11,i]
	dm[i]=data[13,i]
endfor
;help,radi,vexp,texp,mass,Ekin,dm

std_r=stddev(radi, /double)
print,"stddev radius", std_r
std_v=stddev(vexp, /double)
print,"stddev v_exp", std_v
std_t=stddev(texp, /double)
print,"stddev t_exp", std_t
std_m=stddev(mass, /double)
print,"stddev mass", std_m
std_e=stddev(Ekin, /double)
print,"stddev E_kin", std_e
std_dm=stddev(dm, /double)
print,"stddev mass loss rate", std_dm

print,"mean radius",mean(radi)
print,"variance radius", variance(radi)
print
print,"regression R-V",regress(radi,vexp)
print,"regression R-M",regress(radi,mass)
print,"regression V-M",regress(vexp,mass)
print,"regression R-E",regress(radi,Ekin)
print,"regression R-dM",regress(radi,dm)
print,"regression E-dM",regress(Ekin,dm)
print,"regression t-M",regress(texp,mass)
print,"regression t-E",regress(texp,Ekin)
print


print
print,"R^2 r-V",correlate(radi,vexp)^2,correlate(radi,vexp)
print,"R^2 r-M",correlate(radi,mass)^2,correlate(radi,mass)
print,"R^2 V-M",correlate(vexp,mass)^2,correlate(vexp,mass)
print,"R^2 R-E",correlate(radi,Ekin)^2,correlate(radi,Ekin)
print,"R^2 R-dM",correlate(radi,dm)^2,correlate(radi,dm)
print,"R^2 E-dM",correlate(Ekin,dm)^2,correlate(Ekin,dm)
print,"R^2 t-M",correlate(texp,mass)^2,correlate(texp,mass)
print,"R^2 t-E",correlate(texp,Ekin)^2,correlate(texp,Ekin)
print



RETURN
END
