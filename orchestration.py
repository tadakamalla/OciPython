import os, io, shutil, json
import oci

class Orchestration(object):
    #config = oci.config.from_file()
    config = {
        'additional_user_agent': '',
        'eastgroup': '',
        'fingerprint': '',
        'key_file': '.',
        'log_requests': False,
        'pass_phrase': '',
        'region': 'us-ashburn-1',
        'tenancy': '',
        'user': ''
    }
    identity = oci.identity.identity_client.IdentityClient(config)
    compartments = identity.list_compartments(config['tenancy']).data
