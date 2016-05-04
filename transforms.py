# !/usr/bin/env python -tt
#
#
#   transforms.py
#
#
#
#   Code to be a wrapper for all of the transforms that are done in order to clean up the central codes

from __future__ import division
import numpy as np
import numpy.fft as fft
from rwt import dwt, idwt
from rwt.wavelets import daubcqf

def fft2c(data_to_fft,axis=(-2,-1)):
    FFTdata = 1/np.sqrt(data_to_fft.size)*fft.fft2(data_to_fft,axis=axis)
    return FFTdata

def ifft2c(data_to_ifft,axis=(-2,-1)):
    IFFTdata = np.sqrt(data_to_ifft.size)*fft.ifft2(data_to_ifft,axis=axis)
    return IFFTdata

def xfm(data_to_xfm,scaling_factor = 4,L = 2):
    h = daubcqf(scaling_factor)[0]
    XFMdata = dwt(data_to_xfm,h,L)
    return XFMdata

def ixfm(data_to_ixfm,scaling_factor = 4,L = 2):
    h = daubcqf(scaling_factor)[0]
    IXFMdata = idwt(data_to_ixfm,h,L)
    return IXFMdata

def TV(data)
	   
	'''
	A finite differences sampling operation done on datasets to spply some 
	smoothing techniques.
	
	Note that the output comes back such that the stacking dimension is dimension 0
	'''
	shp = data.shape
	
	if len(shp) == 2:
		Dx = data[np.hstack([range(1,shp[0]),shp[0]]),...] - data
		Dy = data[...,np.hstack([range(1,shp[1]),shp[1]])] - data
		
		res = np.array([Dx,Dy])
	elif len(data.shape) == 3:
		Dx = data[np.hstack([range(1,shp[0]),shp[0]]),...,...] - data
		Dy = data[...,np.hstack([range(1,shp[0]),shp[0]]),...] - data
		Dz = data[...,...,np.hstack([range(1,shp[2]),shp[2]])] - data

		res = np.array([Dx,Dy,Dz])
	
	return res

	
def iDx(data,shp):
	res = data[np.hstack([range(shp[0]-1),shp[0]-1],...,...] - data
	res[0,...,...] = -data[0,...,...]
	res[-1,...,...] = data[-2,...,...]
	

def iDy(data,shp):
	res = data[...,np.hstack([range(shp[1]-1),shp[1]-1],...] - data
	res[...,0,...] = -data[...,0,...]
	res[...,-1,...] = data[...,-2,...]

def iDz(data,shp):
	res = data[...,...,np.hstack([range(shp[2]-1),shp[2]-1],...] - data
	res[...,...,0] = -data[...,...,0]
	res[...,...,-1] = data[...,...,-2]
	

def iTV(data):
	'''
	Inverse of the finite differences sampling operation done. Attempting to build back
	the data after it's been TV'd
	
	Note that the input must be put in such that the stacking dimension is dimension 0
	'''
	
	shp = data.shape
	
	res = iDx(data[0,...,...,...])+ iDy(data[1,...,...,...])
	
	if len(shp) == 3:
		res = res + iDz(data[2,...,...,...])
	
	return res
	