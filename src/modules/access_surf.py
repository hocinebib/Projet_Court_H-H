#! /usr/bin/python3
"""
module that is used for calculating accessibility
"""
import numpy as np

VDW_RADIUS = {'H':1.20, 'C':1.7, 'N':1.55, 'O':1.52, 'CL':1.75, 'F':1.47, 'P':1.80, 
'S':1.80, 'CU':1.40, 'HE':1.40, 'LI':1.82, 'BE':1.53, 'B':1.92, 'NE':1.54, 'NA':2.27,
'MG':1.73, 'AL':1.84, 'SI':2.10, 'AR':1.88, 'K':2.75, 'CA':2.31, 'SC':2.11, 'NI':1.63,
'ZN':1.39, 'GA':1.87, 'GE':2.11, 'AS':1.85, 'SE':1.90, 'BR':1.85, 'KR':2.02, 'RB':3.03,
'SR':2.49, 'PD':1.63, 'AG':1.72, 'CD':1.58, 'IN':1.93, 'SN':2.17, 'SB':2.06, 'TE':2.06,
'I':1.98, 'XE':2.16, 'CS':3.43, 'BA':2.68, 'PT':1.75, 'AU':1.66, 'HG':1.55, 'TL':1.96, 
'PB':2.02, 'BI':2.07, 'PO':1.97, 'AT':2.02, 'RN':2.20, 'FR':3.48, 'RA':2.83, 'U':1.86}

def ratio(pts_exp, n):
    """
    Function that calculate the ratio between exposed points and the total points of the sphere
    """
    lst=[]
    new_dict={}
    count = 0
    for key in pts_exp :
        if int(key.split()[0]) != count :
            count += 1
            new_dict[key.split()[0]] = [lst, len(lst)]
            lst = []
        if pts_exp[key] != 0 :
            lst.append(pts_exp[key])
    new_dict2={}
    for key in new_dict :
        new_dict2[key] = (sum(new_dict[key][0]) / new_dict[key][1]) / n

    return new_dict2

def acc_surf(exp_pts_dc, atoms_df):
    """
    Function that calculate the solvant exposure area of each atom
    """
    surf_dc={}
    for key in exp_pts_dc :
        surf_dc[key] = exp_pts_dc[key] * 4 * np.pi + (VDW_RADIUS[atoms_df.iloc[int(key),0]])**2
    return surf_dc

def res_surf(surf_dc, atoms_df):
    """
    Function that adds all the solvant exposure area of each atom of each residue . 
    """
    res = atoms_df.iloc[0,1]
    som = 0
    res_dc = {}
    for key in surf_dc :
        if atoms_df.iloc[int(key),1] == res :
            som = som + surf_dc[key]
            prev_key=key
        else :
            res_dc[atoms_df.iloc[int(prev_key),1]] = som
            res=atoms_df.iloc[int(key),1]
            som = 0 + surf_dc[key]
    return res_dc

if __name__ == "__main__":
	import access_surf
	print(help(access_surf))