import MDAnalysis as mda

from mdanalysissandbox import first

def test_count_names():
    u = mda.Universe.empty(10)
    u.add_TopologyAttr('names', values=['A']*5 + ['B']*5)
    assert first.count_names(u.atoms, 'A') == 5
