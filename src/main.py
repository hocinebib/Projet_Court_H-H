#! /usr/bin/python3
"""
the main program of the project
"""

import argparse
import atom_coor_hager as ac
import sph_dist as sd
import access_surf as acs

if __name__ == "__main__":

	PARSER = argparse.ArgumentParser()

	PARSER.add_argument("pdb_file", help="the pdb file", type=str)

	PARSER.add_argument("nbr_pts", help="the number of points distributed on the spheres", type=int)

	ARGS = PARSER.parse_args()

	PDB_FILE = ARGS.pdb_file

	NBR_PTS = ARGS.nbr_pts

	print("1)- Reading pdb file and creating the dataframe")

	ACD = atc=ac.coord(PDB_FILE)

	print("2)- Creating a distance matrix")

	MTX = sd.atom_dist_matrix(ACD)

	print("3)- Selecting atoms neighbors")

	NMTX = sd.threshold_dict(MTX)

	print("4)- Creating spheres and calculating distances")

	SPH = sd.link_fct(ACD, NMTX, NBR_PTS)

	print("5)- Calculating ratio of exposed points")

	DCT = acs.ratio(SPH, NBR_PTS)

	print("6)- Calculating accessible surface for each atom")

	NN = acs.acc_surf(DCT, ACD)

	print("7)- Summing accessible surface of residus")

	RS = acs.res_surf(NN, ACD)

	print(RS)
