import boto.utils
import json

METADATA_URL_ROOT = 'http://169.254.169.254'

metadata = {}

def get_aws_metadata(*args):
    try:
        metadata = boto.utils.get_instance_metadata(version='latest', url=METADATA_URL_ROOT, data='meta-data/', timeout=None, num_retries=5)
        if len(args) > 0:
            return metadata[args[0]]
        else:
             return json.dumps(metadata)
    except Exception:
        print("Metadata not found") 
        raise
