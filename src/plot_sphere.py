#! /usr/bin/python3
"""

program that 

"""
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot_sphere(points_coor):
	"""
	"""
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	ax.scatter3D(points_coor[:,0], points_coor[:,1],points_coor[:,2], s=10, c="black")
	plt.show()

