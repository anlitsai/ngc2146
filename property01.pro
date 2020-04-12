PRO property

l=18
m=8
openr, lun, 'property.2.dat',/get_lun
data=fltarr(l,m)
readf,lun,data
close, lun
radi=fltarr(m)


radi=data[3,*]
vexp=data[5,*]
texp=data[7,*]
mass=data[9,*]
Ekin=data[11,*]
dm=data[13,*]
help,radi,vexp,texp,mass,Ekin,dm

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
print,"regression",regress(radi[1,*],vexp[1,*])


RETURN
END
