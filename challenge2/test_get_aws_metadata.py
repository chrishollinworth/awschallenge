
import pytest
from get_aws_metadata import get_aws_metadata
from mock_metadata import mock_metadata
from boto import utils

@pytest.fixture()
def metadata(monkeypatch):
    def mock_get_instance_metadata(*args, **kwargs):
        return mock_metadata
    
    monkeypatch.setattr(utils, 'get_instance_metadata', mock_get_instance_metadata)

def test_no_attribute_key_parameter(metadata):
    
    assert len(get_aws_metadata()) == 6951

def test_ami_id(metadata):

    assert get_aws_metadata('ami-id') == mock_metadata['ami-id']

def test_account_id(metadata):

     assert get_aws_metadata('instance-type') == mock_metadata['instance-type']