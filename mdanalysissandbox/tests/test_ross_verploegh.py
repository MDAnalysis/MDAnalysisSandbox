"""Unit tests for Verploegh's new function."""

import numpy as np

from mdanalysissandbox import ross_verploegh


def test_dot_product():
    """Test for the dot product."""
    vector_1 = [0, 1, 1]
    vector_2 = [1, 1, 0]
    assert (ross_verploegh.dot_product(vector_1, vector_2) ==
            1.0)
