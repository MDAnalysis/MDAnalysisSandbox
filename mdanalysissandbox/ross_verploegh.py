"""Simple module for computing dot products."""

import numpy as np


def dot_product(vec1, vec2):
    """Compute the dot product of two vectors."""
    return np.dot(np.array(vec1), np.array(vec2))
