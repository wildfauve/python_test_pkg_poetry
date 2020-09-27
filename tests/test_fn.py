import pytest
from poetry_ex import fn

def test_fn_add():
    assert fn.add(1,2) == 3
