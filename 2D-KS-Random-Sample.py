#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 09:06:59 2019

@author: samchristian
2KS-random sample
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:25:24 2019

@author: samchristian
2D-KS
"""
#print(type(data))
import sys
import numpy as np
import pandas as pd
from astropy.coordinates import SkyCoord
from astropy import units as u
import matplotlib.pyplot as plt
from scipy.stats import kstwobign, pearsonr
import statistics
print(pd.__file__)
sys.path.append('/Users/samchristian/Downloads/2DKS-master')
sys.path.append('/Users/samchristian/Downloads/ndtest-master')
import KS2D
import ndtest
data = pd.read_csv(r'/Users/samchristian/Downloads/grb-frompaper.csv')
#plt.figure()
#plt.subplot(111, projection='aitoff')
#coord_final = SkyCoord(ra=data.loc[:, ['ra']].values, dec=data.loc[:, ['dec']].values, unit=(u.degree, u.degree))
#plt.scatter(coord_final.galactic.l.deg, coord_final.galactic.b.deg)
print(len(data[(data['dec'] < 20) & (data['dec'] > -20)])) #TODO: change to l
print(len(data))
coord_final = SkyCoord(ra=data.loc[:, ['ra']].values, dec=data.loc[:, ['dec']].values, unit=(u.degree, u.degree))
print(len(data[(coord_final.galactic.b.deg < 20) & (coord_final.galactic.b.deg > -20)]))
data = data.loc[(data['z'] <= 2.1) & (data['z'] >= 1.6)]
zs1 = data.loc[(data['z'] <= 2.1) & (data['z'] >= 1.6)]
ras1 = data.loc[:, ['ra']].values
decs1 = data.loc[:, ['dec']].values
def random_point_on_unit_sphere():
    while True:
        R   = np.random.rand(3) #Random point in box
        R   = 2*R - 1
        rsq = sum(R**2)
        if rsq < 1: break       #Use r only if |r|<1 in order not to favor corners of box
    return R / np.sqrt(rsq)     #Normalize to unit vector

def random_point_on_sky():
    p     = random_point_on_unit_sphere()
    r     = np.linalg.norm(p)
    theta = 90 - (np.arccos(p[2] / r)    / np.pi * 180)            #theta and phi values in degrees
    phi   =       np.arctan(p[1] / p[0]) / np.pi * 180
    c     = SkyCoord(ra=phi, dec=theta, unit=(u.degree, u.degree)) #Create coordinate
    return c.ra.deg, c.dec.deg                                     

def print_random_star_coords(nstars):
    for n in range(nstars):
        RA,dec = random_point_on_sky()
        print(ras22)
        #ras22 = np.append(ras22, RA)
        #decs22 = np.append(decs22, dec)
points1 = []
num = 44
iter_2 = 2
l = 0
#while l < (num*iter_2 + 1): 
#   # print(l)
#    point = print_random_star_coords(1)
#    #print(point)
#    points1.append(point)
#    l += 1
slice_number = 0
k = 0
points_iters = []
points_actual = []
test_stats = []
    
while k < iter_2:
    ras11 = []
    decs11  = []
    ras22 = []
    decs22 = []
    l = 0
    while l < 29: 
        RA,dec = random_point_on_sky()
        coord = SkyCoord(ra=RA, dec=dec, unit=(u.degree, u.degree))
        b = coord.galactic.b.deg        
        if (b > 20 or b < -20):
            ras22 = np.append(ras22, RA)
            decs22 = np.append(decs22, dec)
            l += 1
    c = 0
    while c < 29:
         RA1, dec1 = random_point_on_sky()
         coord = SkyCoord(ra=RA1, dec=dec1, unit=(u.degree, u.degree))
         b = coord.galactic.b.deg
         if (b > 20 or b < -20):
            ras11 = np.append(ras11, RA1)
            decs11 = np.append(decs11, dec1)
            c += 1           
    a = 0
    while a < 15:
        RA,dec = random_point_on_sky()
        coord = SkyCoord(ra=RA, dec=dec, unit=(u.degree, u.degree))
        b = coord.galactic.b.deg            
        if (b < 20 and b > -20):
            ras22 = np.append(ras22, RA)
            decs22 = np.append(decs22, dec)
            a += 1
    b = 0    
    while b < 15:
         RA1, dec1 = random_point_on_sky()
         coord = SkyCoord(ra=RA1, dec=dec1, unit=(u.degree, u.degree))
         b = coord.galactic.b.deg
         if (b < 20 and b > -20):
            ras11 = np.append(ras11, RA1)
            decs11 = np.append(decs11, dec1)
            b += 1            
         
    test_stat = ndtest.ks2d2s(ras11, decs11, ras22, decs22, extra=True)[1]
    test_stats.append(test_stat)
    k += 1
print(statistics.mean(test_stats))
print(statistics.variance(test_stats))
plt.hist(test_stats, 100)
df = pd.DataFrame(test_stats)
df.to_csv(r'/Users/samchristian/Downloads/KS-2D.csv')
plt.figure()
plt.subplot(111, projection='aitoff')
coord_final = SkyCoord(ra=ras1, dec=dec1, unit=(u.degree, u.degree))
plt.scatter(coord_final.galactic.l.deg, coord_final.galactic.b.deg)