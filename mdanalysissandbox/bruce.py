""" this is my code module
"""

import numpy as np

def count_names(ag, name):
	"""count how many atoms have a particular name

	PARAMETERS
	-----------
	ag : Atom group
	name : str
		the name to look for

	Returns
	-------
	count :int
	"""

	return len(ag[ag.names == name])
