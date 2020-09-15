#! /usr/bin/python3
"""



"""
import numpy as np
import pandas as pd
from scipy.spatial import distance_matrix

VDW_RADIUS = {'H':1.20, 'C':1.7, 'N':1.55, 'O':1.52, 'CL':1.75, 'F':1.47, 'P':1.80, 
'S':1.80, 'CU':1.40, 'HE':1.40, 'LI':1.82, 'BE':1.53, 'B':1.92, 'NE':1.54, 'NA':2.27,
'MG':1.73, 'AL':1.84, 'SI':2.10, 'AR':1.88, 'K':2.75, 'CA':2.31, 'SC':2.11, 'NI':1.63,
'ZN':1.39, 'GA':1.87, 'GE':2.11, 'AS':1.85, 'SE':1.90, 'BR':1.85, 'KR':2.02, 'RB':3.03,
'SR':2.49, 'PD':1.63, 'AG':1.72, 'CD':1.58, 'IN':1.93, 'SN':2.17, 'SB':2.06, 'TE':2.06,
'I':1.98, 'XE':2.16, 'CS':3.43, 'BA':2.68, 'PT':1.75, 'AU':1.66, 'HG':1.55, 'TL':1.96, 
'PB':2.02, 'BI':2.07, 'PO':1.97, 'AT':2.02, 'RN':2.20, 'FR':3.48, 'RA':2.83, 'U':1.86}

TRSHD = (VDW_RADIUS['H'] + VDW_RADIUS['O'] + VDW_RADIUS['H'] + ((VDW_RADIUS['C'] * 3) +  VDW_RADIUS['N']))
#eau 1.4 A

def atom_coor(pdbfile):
	"""
	extracts atom coordinates
	"""
	atoms_dict = {'residu':[], 'atom':[], 'coor':[]}

	with open(pdbfile, 'r') as pdb:
		
		for line in pdb:

			if line.startswith("ATOM"):

				atoms_dict['residu'].append(line[17:20].strip())
				atoms_dict['atom'].append(line[76:].strip())
				atoms_dict['coor'].append([float(line[32:40].strip()),float(line[40:47].strip()),float(line[48:56].strip())])
	atoms_df = pd.DataFrame(atoms_dict)

	return atoms_df

def spheres(n):#atom_tpl, n):
	"""
	creates a sphere
	"""

	indices = np.arange(0, n, dtype=float) + 0.5
	golden_angle = np.pi * (1 + 5**0.5)
	phi = np.arccos(1 - 2*indices/n)
	theta = golden_angle * indices
	#center = atom_tpl['coor']#atom_tpl[1][2]
	
	#radius = VDW_RADIUS[atom_tpl['atom']] + VDW_RADIUS['O']#VDW_RADIUS[atom_tpl[1][1]]

	points = np.zeros((n, 3))
	points[:,0] = np.cos(theta) * np.sin(phi) #radius * np.cos(theta) * np.sin(phi) + center[0]
	points[:,1] = np.sin(theta) * np.sin(phi) #radius * np.sin(theta) * np.sin(phi) + center[1]
	points[:,2] = np.cos(phi) #radius * np.cos(phi) + center[2]

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

def threshold_dict(trsh, mtx):
	"""
	creates a dictionary having as keys the atom and as values the atom neighbors
	"""
	r=[]
	i=[]

	for index, row in mtx.iterrows():
		r.append(row)
		i.append(index)

	dico_trsh={}
	for a in range(len(i)):
		lst=[]
		for b in range(len(r[a])-1):
			if (r[a][b]<trsh) & (a!=b):
				lst.append(b)
		dico_trsh[a]=lst

	return dico_trsh

def link_fct(df_coor, dico_trsh, n):
	"""
	link between roll_sphere_bis and distance calculation
	"""
	new_dico = {}
	for key in dico_trsh:
		lst=[]
		lst.append(key)
		for neighb in dico_trsh[key]:
			lst.append(neighb)
		sph_lst = roll_sphere_bis(df_coor.iloc[lst,], n) #return

		new_dico[key]=[]
		for i in range(len(sph_lst)):
			if spheres_dist(sph_lst[0], sph_lst[i]):
				new_dico[key].append(dico_trsh[key][i])
	return new_dico

		#une boucle sur len(liste de spheres) appel a spheres_dist(listedesphere[0], listedespheres[i])
		#nous retourne si dist entre atome1 et ses voisins permet mol d'eau

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

def spheres_dist(s1, s2):
	"""
	calculates distance between points of 2 spheres
	"""
	low_dst = 100
	dsts=[]
	for i in range(len(s1)):
		for j in range(len(s1)):
			new = pts_dist(s1[i],s2[j])
			dsts.append(new)
			if new < low_dst :
				low_dst = new
	if low_dst > 1.8:
		return True
	else :
		return False
	#if low_dst < valeur molécule d'eau (1.8 ?) -> non accessible ?
