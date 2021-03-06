#! /usr/bin/python3
"""
module used for calculating surface accessibility
"""
import numpy as np

VDW_RADIUS = {'H': 1.20, 'C': 1.7, 'N': 1.55, 'O': 1.52, 'CL': 1.75,
              'F': 1.47, 'P': 1.80, 'S': 1.80, 'CU': 1.40, 'HE': 1.40,
              'LI': 1.82, 'BE': 1.53, 'B': 1.92, 'NE': 1.54, 'NA': 2.27,
              'MG': 1.73, 'AL': 1.84, 'SI': 2.10, 'AR': 1.88, 'K': 2.75,
              'CA': 2.31, 'SC': 2.11, 'NI': 1.63, 'ZN': 1.39, 'GA': 1.87,
              'GE': 2.11, 'AS': 1.85, 'SE': 1.90, 'BR': 1.85, 'KR': 2.02,
              'RB': 3.03, 'SR': 2.49, 'PD': 1.63, 'AG': 1.72, 'CD': 1.58,
              'IN': 1.93, 'SN': 2.17, 'SB': 2.06, 'TE': 2.06, 'I': 1.98,
              'XE': 2.16, 'CS': 3.43, 'BA': 2.68, 'PT': 1.75, 'AU': 1.66,
              'HG': 1.55, 'TL': 1.96, 'PB': 2.02, 'BI': 2.07, 'PO': 1.97,
              'AT': 2.02, 'RN': 2.20, 'FR': 3.48, 'RA': 2.83, 'U': 1.86}


def ratio(pts_exp, n):
    """
    Function that calculate the ratio between exposed points and the total
    points of the sphere
    Arguments :
        pts_exp : the exposed points (dictionary)
        n : number of points (int)
    Return :
        new_dict2 : dictionary with the ratio of exposed points of each atom

    """
    lst = []
    new_dict = {}
    prev = '0'
    for key in pts_exp:
        if key.split()[0] != prev:
            new_dict[prev] = [lst, len(lst)]
            lst = []
        if pts_exp[key] != 0:
            lst.append(pts_exp[key])
        prev = key.split()[0]
    new_dict[prev] = [lst, len(lst)]
    new_dict2 = {}
    for key in new_dict:
        if new_dict[key][1] != 0:
            new_dict2[key] = (sum(new_dict[key][0]) / (new_dict[key][1]*n))
        else:
            new_dict2[key] = 0

    return new_dict2


def acc_surf(exp_pts_dc, atoms_df):
    """
    Function that calculate the solvant exposure area of each atom
    Arguments :
        exp_pts_dc : the ratio of the exposed points (dictionary)
        atoms_df : the atoms dataframe (dataframe)
    Return :
        surf_dc : a dictionary of the surface accessibility values for each
        atom
    """
    surf_dc = {}
    for key in exp_pts_dc:
        surf_dc[key] = exp_pts_dc[key] * 4 * np.pi + \
         (VDW_RADIUS[atoms_df.iloc[int(key), 0]])**2
    return surf_dc


def res_surf(surf_dc, atoms_df):
    """
    Function that adds all the solvant exposure area of each atom of each
    residue
    Arguments :
        surf_dc : the surfaces values (dictionary)
        atoms_df : the atoms dataframe (dataframe)
    Return :
        res_dc : dictionary with residus accessible surface
    """
    dic = {}
    i = 0

    for r in atoms_df.iterrows():
        if r[0] == 0:
            prev = str(r[1][1])+' '+str(r[1][2])
        if str(r[1][1])+' '+str(r[1][1]) == prev:
            if str(i)+' '+str(r[1][1]) not in dic:
                dic[str(i)+' '+str(r[1][1])] = []
            dic[str(i)+' '+str(r[1][1])].append(r[0])
        elif str(r[1][1])+' '+str(r[1][1]) != prev:
            prev = str(r[1][1])+' '+str(r[1][1])
            i += 1
            if str(i)+' '+str(r[1][1]) not in dic:
                dic[str(i)+' '+str(r[1][1])] = []
            dic[str(i)+' '+str(r[1][1])].append(r[0])

    res_dc = {}

    for k in dic:
        for a in dic[k]:
            if k not in res_dc:
                res_dc[k] = 0
            res_dc[k] += surf_dc[str(a)]

    return res_dc


if __name__ == "__main__":
    import access_surf
    print(help(access_surf))
