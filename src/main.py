#! /usr/bin/python3
"""
the main program of the project
"""

import argparse
import wip_code as wc

if __name__ == "__main__":

	PARSER = argparse.ArgumentParser()

	PARSER.add_argument("pdb_file", help="the pdb file", type=str)

	ARGS = PARSER.parse_args()

	PDB_FILE = ARGS.pdb_file
