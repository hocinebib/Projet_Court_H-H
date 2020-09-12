#! /usr/bin/python3
"""



"""
import numpy as np
import pandas as pd

VDW_RADIUS = {'H':1.20, 'C':1.7, 'N':1.55, 'O':1.52, 'CL':1.75, 'F':1.47, 'P':1.80, 
'S':1.80, 'CU':1.40, 'HE':1.40, 'LI':1.82, 'BE':1.53, 'B':1.92, 'NE':1.54, 'NA':2.27,
'MG':1.73, 'AL':1.84, 'SI':2.10, 'AR':1.88, 'K':2.75, 'CA':2.31, 'SC':2.11, 'NI':1.63,
'ZN':1.39, 'GA':1.87, 'GE':2.11, 'AS':1.85, 'SE':1.90, 'BR':1.85, 'KR':2.02, 'RB':3.03,
'SR':2.49, 'PD':1.63, 'AG':1.72, 'CD':1.58, 'IN':1.93, 'SN':2.17, 'SB':2.06, 'TE':2.06,
'I':1.98, 'XE':2.16, 'CS':3.43, 'BA':2.68, 'PT':1.75, 'AU':1.66, 'HG':1.55, 'TL':1.96, 
'PB':2.02, 'BI':2.07, 'PO':1.97, 'AT':2.02, 'RN':2.20, 'FR':3.48, 'RA':2.83, 'U':1.86}

def atom_coor(pdbfile):
	"""
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

def spheres(atom_tpl, n):
	"""
	"""

	indices = np.arange(0, n, dtype=float) + 0.5
	golden_angle = np.pi * (1 + 5**0.5)
	phi = np.arccos(1 - 2*indices/n)
	theta = golden_angle * indices
	center = atom_tpl['coor']#atom_tpl[1][2]
	
	radius = VDW_RADIUS[atom_tpl['atom']] + VDW_RADIUS['O']#VDW_RADIUS[atom_tpl[1][1]]

	points = np.zeros((n, 3))
	points[:,0] = radius * np.cos(theta) * np.sin(phi) + center[0]
	points[:,1] = radius * np.sin(theta) * np.sin(phi) + center[1]
	points[:,2] = radius * np.cos(phi) + center[2]

	return points

def roll_sphere(atoms_df):
	"""
	"""
	for row in atoms_df.iterrows():
		spheres(row)
