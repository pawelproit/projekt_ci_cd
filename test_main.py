from main import substr

def test_substr():
    assert substr(2, 3) == -1
    assert substr(-1, 1) == -2
    assert substr(0, 0) == 0
    assert substr(2, 4) == -2
