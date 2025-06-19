# app.py
# This is a test commit
# added self_hosted runner
def add(a, b):
    return a * b

def test_add():
    assert add(1, 2) == 2
    assert add(1, -1) == -1
