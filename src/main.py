#! /usr/bin/python3
"""
Main program of the project

Usage exemple :

    python main.py 1b0q.pdb 96 1b0q.rsa

"""

import argparse
import coor_atom as ac
import sph_dist as sd
import access_surf as acs
import parse_rsa as pr
import comp_plot as cp
import pandas as pd
import time
import time_complete as tc

if __name__ == "__main__":

    START = time.time()

    PARSER = argparse.ArgumentParser()

    PARSER.add_argument("pdb_file", help="the pdb file", type=str)

    PARSER.add_argument("nbr_pts",
                        help="the number of points distributed on the spheres",
                        type=int)

    PARSER.add_argument("rsa_file", help="the rsa file that naccess gives for \
                        the same pdb", type=str)

    ARGS = PARSER.parse_args()

    PDB_FILE = ARGS.pdb_file

    NBR_PTS = ARGS.nbr_pts

    RSA_FILE = ARGS.rsa_file

    print("1)- Reading pdb file and creating the dataframe")

    ACD = ac.coord(PDB_FILE)

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

    res = []
    acc = []
    for key in RS:
        res.append(key.split()[1])
        acc.append(RS[key])
    dic = {}
    dic['residu'] = res
    dic['accessibility'] = acc

    df = pd.DataFrame(dic)

    df.to_csv('Results/'+PDB_FILE.split('/')[-1].split('.')[0]+'.csv')

    print(df)

    print("8)- Protein accessibility :")

    s = sum(acc)

    print(s)

    print("9)- Parsing rsa file")

    RSA = pr.abs_acc(RSA_FILE)

    END = time.time()

    print("duration of the programm : ", tc.complete_time(START, END))

    print("10)- Showing through a plot the difference between our results and \
    Naccess results :")

    cp.compare_plot(RSA['acc'].tolist(),
                    df['accessibility'].tolist(), RSA['residu'].tolist())
