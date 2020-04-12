#!/usr/bin/env python
# for skyview
# /iapetus/data/satoki_data/ngc2146/imsize

# --- import constant -------------------------	#
import math
#import pyfits
# --- constant --------------------------------	#
#  --- parameter ------------------------------	#
px2as=0.2
#  --------------------------------------------	#

def imsize(pxsize,coord_incr,note):
	imsize_as=pxsize*coord_incr
	imsize_deg=imsize_as/3600.0
	print '%.3f' %coord_incr,"[arcsec/px] |",'%.2f' %imsize_as, "[arcsec] =", '%.4f' %imsize_deg, "[degree] |", '%.0f' %pxsize, "[px] |",note
	return imsize_deg

def pxsize(imsize_as,coord_incr,note):
	imsize_deg=imsize_as/3600.0
	pxsize=imsize_as/coord_incr
	print '%.3f' %coord_incr,"[arcsec/px] |",'%.2f' %imsize_as, "[arcsec] =", '%.4f' %imsize_deg, "[degree] |", '%.0f' %pxsize, "[px] |",note
	return pxsize

def coord_incr(imsize_deg,pxsize,note):
	imsize_as=imsize_deg*3600.0
	coord_incr=imsize_as/pxsize
	print '%.3f' %coord_incr,"[arcsec/px] |",'%.2f' %imsize_as, "[arcsec] =", '%.4f' %imsize_deg, "[degree] |", '%.0f' %pxsize, "[px] |",note
	return pxsize


print "------------"
ims=imsize(2560,px2as,"n3628")
ims=imsize(1014,px2as,"n3628")
ims=imsize(1024,px2as,"n3628")
ims=imsize(1024,px2as,"n3628")
pxs=pxsize(180,px2as,"n3628")
pxs=pxsize(360,px2as,"n3628")
coordin=coord_incr(0.05,1014,"n3628")
coordin=coord_incr(0.05,1024,"n3628")
coordin=coord_incr(0.06,1014,"n3628")
coordin=coord_incr(0.06,1024,"n3628")
coordin=coord_incr(0.0563,1014,"n3628")
coordin=coord_incr(0.1,900,"n3628")
coordin=coord_incr(0.2,900,"n3628")
coordin=coord_incr(0.2,3600,"n3628")
coordin=coord_incr(0.2,1800,"n3628")
coordin=coord_incr(1,900,"n3628")
print "------------"

# --- reference -------------------------------	#

exit

