#! /usr/bin/python3
"""

"""
import numpy as np
import pandas as pd
import time
import time_complete as tc
from scipy.spatial import distance_matrix
from progressbar import ProgressBar

VDW_RADIUS = {'H':1.20, 'C':1.7, 'N':1.55, 'O':1.52, 'CL':1.75, 'F':1.47, 'P':1.80, 
'S':1.80, 'CU':1.40, 'HE':1.40, 'LI':1.82, 'BE':1.53, 'B':1.92, 'NE':1.54, 'NA':2.27,
'MG':1.73, 'AL':1.84, 'SI':2.10, 'AR':1.88, 'K':2.75, 'CA':2.31, 'SC':2.11, 'NI':1.63,
'ZN':1.39, 'GA':1.87, 'GE':2.11, 'AS':1.85, 'SE':1.90, 'BR':1.85, 'KR':2.02, 'RB':3.03,
'SR':2.49, 'PD':1.63, 'AG':1.72, 'CD':1.58, 'IN':1.93, 'SN':2.17, 'SB':2.06, 'TE':2.06,
'I':1.98, 'XE':2.16, 'CS':3.43, 'BA':2.68, 'PT':1.75, 'AU':1.66, 'HG':1.55, 'TL':1.96, 
'PB':2.02, 'BI':2.07, 'PO':1.97, 'AT':2.02, 'RN':2.20, 'FR':3.48, 'RA':2.83, 'U':1.86}

TRSHD = VDW_RADIUS['C'] * 3 + VDW_RADIUS['N'] + 1.4

def spheres(n):#atom_tpl, n):
    """
    creates a sphere
    """

    indices = np.arange(0, n, dtype=float) + 0.5
    golden_angle = np.pi * (1 + 5**0.5)
    phi = np.arccos(1 - 2*indices/n)
    theta = golden_angle * indices

    points = np.zeros((n, 3))
    points[:,0] = np.cos(theta) * np.sin(phi)
    points[:,1] = np.sin(theta) * np.sin(phi)
    points[:,2] = np.cos(phi)

    return points

def roll_sphere(atoms_df,n):
    """
    changes sphere's radius and center
    """
    sphere_pts=spheres(n)
    for row in atoms_df.iterrows():
        radius = VDW_RADIUS[row[1][0]]
        sphere_pts[:,0] = sphere_pts[:,0] * radius + row[1][3]
        sphere_pts[:,1] = sphere_pts[:,1] * radius + row[1][4]
        sphere_pts[:,2] = sphere_pts[:,2] * radius + row[1][5]
    

def pts_dist(pt1, pt2):
    """
    calculates distance between two points (or all points of 2 df)
    """

    squared_dist = np.sum((pt1-pt2)**2, axis = 0)
    dist = np.sqrt(squared_dist)

    return dist

def atom_dist_matrix(df_coor):
    """
    creates distance matrix between all atoms
    """
    return pd.DataFrame(distance_matrix(df_coor.iloc[:,3:],df_coor.iloc[:,3:]), index=df_coor.iloc[:,3:].index, columns=df_coor.iloc[:,3:].index)

def threshold_dict(mtx):
    """
    creates a dictionary having as keys the atom and as values the atom neighbors
    """
    pbar = ProgressBar()
    r = []
    i = []
    TRS_MAX = VDW_RADIUS['C'] * 2 + VDW_RADIUS['N'] + (1.4 * 2)

    for index, row in mtx.iterrows():
        r.append(row)
        i.append(index)

    dico_trsh = {}
    for a in pbar(range(len(i))):
        lst = []
        for b in range(len(r[a])-1):
            if (r[a][b] < TRS_MAX) & (a != b):
                lst.append(b)
        dico_trsh[a] = lst

    return dico_trsh

def link_fct(df_coor, dico_trsh, n):
    """
    link between roll_sphere_bis and distance calculation
    """
    START = time.time()
    pbar = ProgressBar()
    new_dico = {}
    for key in pbar(dico_trsh):
        lst = []
        lst.append(key)
        for neighb in dico_trsh[key]:
            lst.append(neighb)
        sph_lst = roll_sphere_bis(df_coor.iloc[lst,], n)

        for i in range(len(sph_lst)-1):
            new_dico[str(key) + " " + str(i+1)] = spheres_dist(sph_lst[0], sph_lst[i+1])
    END = time.time()
    print("time elapsed :" + tc.complete_time(START, END))
    return new_dico

def roll_sphere_bis(atoms_df, n):
    """
    the roll_sphere that I actualy use
    """
    sph_lst=[]
    for row in atoms_df.iterrows():
        sphere_pts=spheres(n)
        radius = VDW_RADIUS[row[1][0]]
        sphere_pts[:,0] = sphere_pts[:,0] * radius + row[1][3]
        sphere_pts[:,1] = sphere_pts[:,1] * radius + row[1][4]
        sphere_pts[:,2] = sphere_pts[:,2] * radius + row[1][5]
        sph_lst.append(sphere_pts)
    return sph_lst

def spheres_dist(s1, s2):#, vdm_r):
    """
    calculates distance between points of 2 spheres
    """
    count = 0
    nonenf = False
    for i in range(len(s1)):
        for j in range(len(s1)):
            if pts_dist(s1[i],s2[j]) < 2.8 :
                nonenf = False
                break
            else :
                nonenf = True
        if nonenf :
            count += 1
    return count
