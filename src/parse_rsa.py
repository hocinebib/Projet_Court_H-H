#! /usr/bin/python3
"""

"""
import pandas as pd

def abs_acc(rsafile):
    """
    extracts accessibility 
    """
    rsa_dict = {'residu':[], 'acc':[], 'num':[]}

    with open(rsafile, 'r') as rsa:
        
        for line in rsa:

            if line.startswith("RES"):

                rsa_dict['residu'].append(line[3:7].strip())
                rsa_dict['acc'].append(line[14:23].strip())
                rsa_dict['num'].append(line[11:14].strip())
    rsa_df = pd.DataFrame(rsa_dict)

    return rsa_df



if __name__ == "__main__":
	import parse_rsa
	print(help(parse_rsa))