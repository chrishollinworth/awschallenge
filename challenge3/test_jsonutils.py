import pytest
from jsonutils import get_value_from_json

def test_example1():

    testjson = '{\"a\":{\"b\":{\"c\":\"d\"}}}'
    testkey = 'a/b/c'

    assert get_value_from_json(testjson,testkey) == 'd'

def test_example2():

    testjson = '{\"x\":{\"y\":{\"z\":\"a\"}}}'
    testkey = 'x/y/z'

    assert get_value_from_json(testjson,testkey) == 'a'
