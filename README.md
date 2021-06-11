# Projet Court (Sujet 2) :

---
## Description :

Solvent accessible surface of a protein

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

asa = dictionnaire contenant les noms des residus en clef, et les surfaces accesible au solvant comme valeur. 

|   | residu | accessibility |
|---|--------|---------------|
| 0 | CYS    | 85.2575499    |
| 1 | GLU    | 120.727667    |
| 2 | HIS    | 144.624399    |
| 3 | ARG    | 184.331165    |
| 4 | TRP    | 200.036144    |
| 5 | CYS    | 80.8248480    |
| 6 | LYS    | 183.349323    |
| 7 | PRO    | 119.654651    |
| 8 | VAL 	 | 100.306204    |

---
## Authors :
-Hocine Merouana

-Hager Elharty

-Sleheddine Kastalli

