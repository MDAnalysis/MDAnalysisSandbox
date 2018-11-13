"""
Unit and regression test for the mdanalysissandbox package.
"""

# Import package, test suite, and other packages as needed
import mdanalysissandbox
import pytest
import sys

def test_mdanalysissandbox_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mdanalysissandbox" in sys.modules


def test_fixture(HVR):
    assert len(HVR.atoms) > 1
