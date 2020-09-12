#! /usr/bin/python3
"""

program that creates a sphere around each atom

"""
import numpy as np

VDW_RADIUS = {'H':1.20, 'C':1.7, 'N':1.55, 'O':1.52, 'CL':1.75, 'F':1.47, 'P':1.80, 
'S':1.80, 'CU':1.40, 'HE':1.40, 'LI':1.82, 'BE':1.53, 'B':1.92, 'NE':1.54, 'NA':2.27,
'MG':1.73, 'AL':1.84, 'SI':2.10, 'AR':1.88, 'K':2.75, 'CA':2.31, 'SC':2.11, 'NI':1.63,
'ZN':1.39, 'GA':1.87, 'GE':2.11, 'AS':1.85, 'SE':1.90, 'BR':1.85, 'KR':2.02, 'RB':3.03,
'SR':2.49, 'PD':1.63, 'AG':1.72, 'CD':1.58, 'IN':1.93, 'SN':2.17, 'SB':2.06, 'TE':2.06,
'I':1.98, 'XE':2.16, 'CS':3.43, 'BA':2.68, 'PT':1.75, 'AU':1.66, 'HG':1.55, 'TL':1.96, 
'PB':2.02, 'BI':2.07, 'PO':1.97, 'AT':2.02, 'RN':2.20, 'FR':3.48, 'RA':2.83, 'U':1.86}
#https://www.elementschimiques.fr/?fr/proprietes/chimiques/rayon-de-van-der-waals

def spheres(atoms_coor, n):
	"""
	atoms_coor : the list that arom_coor returns
	n : the number of points distributed on the sphere
	golden angle algorithm
	"""

	sphere_lst = []

	golden_angle = np.pi * (3 - np.sqrt(5))
	
	for atom in atoms_coor:

		atom_sphere = []

		atom_sphere.append(atom[0])

		center = atom[1]
		theta = golden_angle * np.arange(n)
		z = np.linspace(1 - 1.0 / n, 1.0 / n - 1, n)

		radius = VDW_RADIUS[atom[0]] + VDW_RADIUS['O']

		points = np.zeros((n, 3))
		points[:,0] = radius * np.cos(theta) + center[0]
		points[:,1] = radius * np.sin(theta) + center[1]
		points[:,2] = z + center[2]

		atom_sphere.append(points)

		sphere_lst.append(atom_sphere)
	
	return sphere_lst


def spheres2(atoms_coor, n):
	"""
	atoms_coor : the list that arom_coor returns
	n : the number of points distributed on the sphere
	golden angle algorithm
	"""

	sphere_lst = []

	indices = np.arange(0, n, dtype=float) + 0.5
	golden_angle = np.pi * (1 + 5**0.5)
	phi = np.arccos(1 - 2*indices/n)
	theta = golden_angle * indices
	
	for atom in atoms_coor:

		atom_sphere = []

		atom_sphere.append(atom[0])

		center = atom[1]

		radius = VDW_RADIUS[atom[0]] + VDW_RADIUS['O']

		points = np.zeros((n, 3))
		points[:,0] = radius * np.cos(theta) * np.sin(phi) + center[0]
		points[:,1] = radius * np.sin(theta) * np.sin(phi) + center[1]
		points[:,2] = radius * np.cos(phi) + center[2]

		atom_sphere.append(points)

		sphere_lst.append(atom_sphere)
	
	return sphere_lst


def sphere1(n):
	"""
	"""
	golden_angle = np.pi * (3 - np.sqrt(5))

    theta = golden_angle * np.arange(n)

    z = np.linspace(1 - 1.0 / n, 1.0 / n - 1, n)
    
    radius = np.sqrt(1 - z * z)
    
    points = np.zeros((n, 3))
    
    points[:,0] = radius * np.cos(theta)
    points[:,1] = radius * np.sin(theta)
    points[:,2] = z
        
    return points

def roll_sphere(sphere_pts, atoms_coor):
	"""
	"""
	new_sphere[:,0]=new_sphere[:,0]+atoms_coor[0]
	new_sphere[:,1]=new_sphere[:,1]+atoms_coor[1]
	new_sphere[:,2]=new_sphere[:,2]+atoms_coor[2]

	return new_sphere

if __name__ == "__main__":
	import sphere_pts
	print(help(sphere_pts))