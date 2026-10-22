import pytest
from app import greet, classify_status

def test_greet():
    assert greet("Yashas") == "Hello, Yashas!"

def test_empty_name():
    with pytest.raises(ValueError): greet(" ")

@pytest.mark.parametrize("code,expected",[(200,"success"),(404,"client_error"),(503,"server_error"),(302,"other")])
def test_classify_status(code,expected):
    assert classify_status(code)==expected
