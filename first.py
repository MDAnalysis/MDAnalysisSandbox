"""Hey this i smy cool module


"""

import numpy as np 

def count_names(ag, name):
    """Count how many atoms have a particular name 


    Parameters
    
    ag : AtomGroup
    the atom group to work on 

    name:str 
    the name to look for
    """
    return len(ag[ag.name == name])


