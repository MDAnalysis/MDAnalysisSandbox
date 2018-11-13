import pytest
from pkg_resources import resource_filename

import MDAnalysis as mda


@pytest.fixture()
def HVR():
    fn = resource_filename(__name__,
                           '../data/1hvr.pdb')

    return mda.Universe(fn)
