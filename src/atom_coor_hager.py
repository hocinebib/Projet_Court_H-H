"""
program that reads a pdb file and extracts each atom coordinates
"""
import pandas as pd

def coord(fichier_pdb):
    """
	the function that reads the pdb file and extracts the atoms coordinates
	it returns as a result a list of lists containing the atom name and its 
	coordinates
    
	"""

    with open(fichier_pdb, "r") as f_pdb:
        coor_lst = []
        for ligne in f_pdb :
            if ligne[0:4] == "ATOM":
            
                # Création du dictionnaire vide.
                dico = {}
                
                # Extraction de l'atome
                dico["atom"] = str(ligne[13:14])
                
                # Extraction du nom du résidu.
                dico["residu "] = str(ligne[17:21])
                
                # Extraction du numéro du résidu.
                dico["N° resid"] = int(ligne[22:26])
                
                # Extraction de la coordonnée x.
                dico["x"] = float(ligne[30:38])
                
                # Extraction de la coordonnée y.
                
                dico["y"] = float(ligne[38:46])
                # Extraction de la coordonnée z.
                
                dico["z"] = float(ligne[46:54])
                coor_lst.append(dico)
                
        DF_coord = pd.DataFrame(coor_lst)
        
    return DF_coord



if __name__ == "__main__":
	import atom_coor
	print(help(atom_coor))