"""
Program that reads a PDB file and extracts each atom coordinates
"""
import pandas as pd

def coord(fichier_pdb):
    """
    The function that reads the PDB file and extracts the atoms coordinates
    it returns as a result a list of lists containing the atom name and its 
    coordinates
    """

    with open(fichier_pdb, "r") as f_pdb:
        coor_lst = []
        for ligne in f_pdb :
            if ligne[0:4] == "ATOM":
            
                # Creating the empty dictionary. 
                dico = {}
                
                # Atom extraction.
                dico["atom"] = str(ligne[77:79].strip())
                
                # Extraction of the name of the residue.
                dico["residu "] = str(ligne[17:21].strip())
                
                # Extraction of the residue number.
                dico["N° resid"] = int(ligne[22:26].strip())
                
                # Extraction of the x coordinate.
                dico["x"] = float(ligne[30:38].strip())
                
                # Extraction of the y coordinate.
                dico["y"] = float(ligne[38:46].strip())
		
                # Extraction of the z coordinate. 
                dico["z"] = float(ligne[46:54].strip())
                coor_lst.append(dico)
                
        atoms_df = pd.DataFrame(coor_lst)    
    return atoms_df


if __name__ == "__main__":
	import coor_atom
	print(help(coor_atom))
