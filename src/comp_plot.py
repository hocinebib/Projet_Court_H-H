#! /usr/bin/python3
"""
plots two lists of values
"""
from matplotlib import pyplot as plt

def compare_plot(lst_rsa, lst_pjct, res_lst):
	"""
	"""
	plt.plot(lst_rsa, label="naccess result")
	plt.plot(lst_pjct, label="our result")
	plt.xticks(range(len(lst_rsa)), res_lst)
	plt.xlabel("Residus")
	plt.ylabel("Accessibility")
	plt.legend()
	plt.show()


if __name__ == "__main__":
	import comp_plot
	print(help(comp_plot))