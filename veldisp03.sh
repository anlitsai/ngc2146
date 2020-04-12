#!/bin/bash

callcalc=calc.txt
# similar to veldisp01.py




echo 'import math' >> $callcalc
echo 'incli=60' >> $callcalc
echo 'phi_ttl=180' >> $callcalc
echo 'alpha=0.3' >> $callcalc
echo 'beta=0.32' >> $callcalc
echo 'gamma=256.39' >> $callcalc
# v=gamma*r/(r**alpha+r**(1-beta)
echo 'def vr(r):' >> $callcalc
echo '	vr=gamma*r/(r**alpha+r**(1-beta))'>> $callcalc
echo '	return vr' >> $callcalc
# w=dv/dr=gamma*(1/(r**alpha+r**(1-beta))-2*r*(r**alpha+r+*(1-beta))**(-2)*(alpha*r**(alpha-1)+(1-beta)*r**(-beta)))
echo 'def wr(r):' >> $callcalc
echo '	wr=gamma*(1/(r**alpha+r**(1-beta))-2*r*(r**alpha+r+*(1-beta))**(-2)*(alpha*r**(alpha-1)+(1-beta)*r**(-beta)))' >> $callcalc
echo '	return wr' >> $callcalc
echo '' >> $callcalc
echo 'dispv_r=10.0' >> $callcalc
echo 'dispv_z=0.5*dispv_r' >> $callcalc
echo 'dispv_phi=dispv_r*math.sqrt(0.5*(1+w))' >> $callcalc
echo 'def disp_v(i,phi):' >> $callcalc
echo '	ii=i/180.0*math.pi' >> $callcalc
echo '	phii=phi/180.0*math.pi' >> $callcalc
echo '	xi=math.cos(phii)' >> $callcalc
echo '	yi=math.sin(phii)' >> $callcalc
echo '	dispv_maj=math.sqrt((dispv_phi*math.sin(ii))**2+(dispv_z*math.cos(ii))**2)' >> $callcalc
echo '	dispv_min=math.sqrt((dispv_r*math.sin(ii))**2+(dispv_z*math.cos(ii))**2)' >> $callcalc
echo '	dispv=math.sqrt(dispv_r**2+dispv_phi**2+dispv_z**2)' >> $callcalc
echo '	dispv_los=math.sqrt((dispv_r*math.sin(phii)*math.sin(ii))**2+(dispv_phi*math.cos(phii)*math.sin(ii))**2+(dispv_z*math.cos(ii))**2)' >> $callcalc
echo '	return  phi, i, xi, yi, dispv_r, dispv_z, dispv_phi, dispv_maj, dispv_min, dispv, dispv_los' >> $callcalc
echo '' >> $callcalc
echo 'fout = open("dispv02.dat", "w")' >> $callcalc
echo 'for phi in range(0,phi_ttl):' >> $callcalc
echo '	dispv=disp_v(incli,phi)' >> $callcalc
echo '	for i_arr in range(0,11):' >> $callcalc
echo '		fout.write(str(dispv[i_arr]))' >> $callcalc
echo '		fout.write(" ")' >> $callcalc
echo '	fout.write("\n")' >> $callcalc
echo 'fout.close()' >> $callcalc
echo 'exit' >> $callcalc
echo '' >> $callcalc
python < $callcalc

callplot=plot.txt

echo 'time=5' >> $callplot
echo 'set style data line' >> $callplot
echo 'plot "dispv02.dat" using 3:11' >> $callplot
echo 'pause time' >> $callplot
echo '' >> $callplot
gnuplot < $callplot

rm -f $callcalc $callplot dispv02.dat

exit

