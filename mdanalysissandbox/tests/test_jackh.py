
from mdanalysissandbox import jackh



def test_printme():
    test = "Some Text"
    ret = jackh.printme(test)
    assert ret == "Some Text!"
