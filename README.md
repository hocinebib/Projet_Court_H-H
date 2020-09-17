# Projet Court (Sujet 2) :

---
## Description :

Calcul de la surface accessible au solvant d’une protéine

---
## Requirements :
Python3, Pandas, Argparse, Numpy, Scipy, Progressbar, Time
```bash
$ conda create -n proj_env
$ activate proj_env
$ conda install pandas
$ conda install -c conda-forge argparse
$ conda install -c anaconda numpy
$ conda install -c anaconda scipy
$ conda install -c conda-forge progressbar
```
### System :
- Linux : This program works on a Linux environment.
- Windows : It also works on Windows.

### Python Packages :
- Pandas
- Argparse
- Numpy
- Matplotlib
- Scipy
- Progressbar
- Time

### Data files :
- The pdb file of the protein : 1b0q.pdb, 3i40.pdb

### Programs :
- NACCESS

### Script files :
`main.py`

`acoord_atom.py`

`sph_dist`

`access_surf.py`

`time_complete.py`

`parse_rsa.py`

`comp_plot.py`

---
## Usage :
1. Cloning the repository :
```bash
$ git clone https://github.com/hocinebib/Projet_Court_H-H.git
```
you can also download the zip file than unzip it

2. Runing the code :
```bash
$ python3 main.py pdbfile nbr_of_pts rsafile
```

### Usage exemple :
```bash
$ cd Projet_Court_H-H
$ python3 src/main.py Data/1b0q.pdb 100 Data/1b0q.rsa
```
---
## Result exemple :
**Resultat pour la protéine 1b0q.pd avec 100 points par sphère.**

asa = 
{'CYS': 117.73196149237984, 'GLU': 174.3376699676473, 'HIS': 200.3454305398364, 'ARG': 278.0520990749046, 'TRP': 290.17094113914544, 'LYS': 273.4042390575278, 'PRO': 171.00491593308368} 

asa = dictionnaire contenant les noms des residus en clef, et les surfaces accesible au solvant comme valeur. 

|   | residu | accessibility |
|---|--------|---------------|
| 0 | CYS    | 114.244571    |
| 1 | GLU    | 174.425587    |
| 2 | HIS    | 200.267724    |
| 3 | ARG    | 278.468391    |
| 4 | TRP    | 290.106556    |
| 5 | CYS 1  | 117.709214    |
| 6 | LYS    | 273.497471    |
| 7 | PRO    | 171.048121    |

---
## Authors :
-Hocine Merouana

-Hager Elharty

-Sleheddine Kastalli

