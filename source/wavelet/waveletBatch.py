from sys import path as syspath
syspath.append("/home/asalerno/Documents/pyDirectionCompSense/")
syspath.append("/home/asalerno/Documents/pyDirectionCompSense/source/")
syspath.append("/home/asalerno/Documents/pyDirectionCompSense/source/wavelet")
from waveletExampleInputs import runCSAlgorithm
import numpy as np

#pctg = [0.125, 0.25, 0.33, 0.50, 0.75]
pctg = 0.25

saveImsPngFile = []
saveImDiffPngFile = []
saveNpyFile = []

#for i in xrange(len(pctg)):
    #saveImsPngFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/waveletTests/'+str(int(pctg[i]*100))+'_spConvergences_kern')
    #saveNpyFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/waveletTests/'+str(int(pctg[i]*100))+'_spConvergences_kern.npy')
    #saveImDiffPngFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/waveletTests/'+str(int(pctg[i]*100))+'_spDifferences_kern')

kern = []

kern.append(np.array([[[ 0.,  0.,  0.], 
                  [ 0.,  0.,  0.], 
                  [ 0.,  0.,  0.]],                
                 [[ 0.,  0.,  0.],
                  [ 0., -1.,  0.],
                  [ 0.,  1.,  0.]],
                 [[ 0.,  0.,  0.],
                  [ 0., -1.,  1.],
                  [ 0.,  0.,  0.]]]))
                  
saveImsPngFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/TV_3x3_spConvergences_kern_norm')
saveNpyFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/TV_3x3_spConvergences_kern_norm.npy')
saveImDiffPngFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/TV_3x3_spDifferences_kern_norm')

kern.append(np.array([[[ 0.,  0.,  0.],
                  [ 0.,  0.,  0.],
                  [ 0.,  0.,  0.]],
                  
                  [[ -1.,  0., 1.],
                  [ -2., 0.,  2.],
                  [ -1.,  0.,  1.]],
                  
                  [[ -1.,  -2.,  -1.],
                  [ 0., 0., 0.],
                  [ 1.,  2., 1.]]]))
kern[0] = kern[0]/np.sum(abs(kern[0][1]))


saveImsPngFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/sobel_3x3_spConvergences_kern_norm')
saveNpyFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/sobel_3x3_spConvergences_kern_norm.npy')
saveImDiffPngFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/sobel_3x3_spDifferences_kern_norm')

kern.append(np.array([[[0., 0., 0.,  0.,  0.],
                  [ 0., 0., 0.,  0.,  0.],
                  [ 0., 0., 0.,  0.,  0.],
                  [ 0., 0., 0.,  0.,  0.],
                  [ 0., 0., 0.,  0.,  0.]],
                  
                  [[ -1., -2., 0.,  2.,  1.],
                  [  -4., -8., 0.,  8.,  4.],
                  [ -6., -12,  0., 12., 6.],
                  [ -4., -8,    0.,  8., 4.],
                  [ -1., -2,   0.,  2., 1.]],
                  
                  [[ -1.,  -4., -6, -4,  -1.],
                  [-2., -8., -12., -8., -2.],
                  [ 0., 0., 0., 0., 0.],
                  [2., 8., 12., 8., 2.],
                  [ 1.,  4., 6., 4.,  1.]]]))
                  
kern[1] = kern[1]/np.sum(abs(kern[1][1]))

saveImsPngFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/sobel_5x5_spConvergences_kern_norm')
saveNpyFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/sobel_5x5_spConvergences_kern_norm.npy')
saveImDiffPngFile.append('/micehome/asalerno/Documents/pyDirectionCompSense/phantomKernTests/sobel_5x5_spDifferences_kern_norm')


    
for i in xrange(len(kern)):
    runCSAlgorithm(pctg=pctg,
                   filename='/home/asalerno/Documents/pyDirectionCompSense/phantom/imFull.npy',
                   sliceChoice = 0,
                   kern=kern[i],
                   saveNpy=True,
                   saveNpyFile=saveNpyFile[i],
                   saveImsPng=True,
                   saveImsPngFile=saveImsPngFile[i],
                   saveImDiffPng=True,
                   saveImDiffPngFile=saveImDiffPngFile[i])