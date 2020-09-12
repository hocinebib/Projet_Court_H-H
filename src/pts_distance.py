#! /usr/bin/python3
"""

program that 

"""
import numpy as np

def pts_dist(pt1, pt2):
	"""
	"""

	squared_dist = np.sum((pt1-pt2)**2, axis = 0)
	dist = np.sqrt(squared_dist)

	return dist
