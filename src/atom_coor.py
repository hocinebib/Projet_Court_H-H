#! /usr/bin/python3
"""

program that reads a pdb file and extracts each atom coordinates

"""

def atom_coor(pdbfile):
	"""
	the function that reads the pdb file and extracts the atoms coordinates

	it returns as a result a list of lists containing the atom name and its 

	coordinates
	"""
	coor_lst=[]

	with open(pdbfile, 'r') as pdb:
		
		for line in pdb:

			if line.startswith("ATOM"):

				atom_lst=[]

				atom_lst.append(line[76:].strip())
				atom_lst.append([float(line[32:40].strip()),float(line[40:47].strip()),float(line[48:56].strip())])
				#[float(line[32:39].strip()),float(line[40:47].strip()),float(line[47:55].strip())]

				coor_lst.append(atom_lst)

	return coor_lst


if __name__ == "__main__":
	import atom_coor
	print(help(atom_coor))