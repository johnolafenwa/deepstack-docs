import os,sys
import boto3


DIGITALOCEAN_SPACES_ZONE = sys.argv[1]
DIGITALOCEAN_SPACES_SPACE = sys.argv[2]
DIGITALOCEAN_SPACES_KEY = sys.argv[3]
DIGITALOCEAN_SPACES_KEY_SEC = sys.argv[4]

session = boto3.session.Session()
client = session.client('s3',
                        region_name=DIGITALOCEAN_SPACES_ZONE,
                        endpoint_url='https://{}.digitaloceanspaces.com'.format(DIGITALOCEAN_SPACES_ZONE),
                        aws_access_key_id=DIGITALOCEAN_SPACES_KEY,
                        aws_secret_access_key=DIGITALOCEAN_SPACES_KEY_SEC)

client.download_file(DIGITALOCEAN_SPACES_SPACE,
                     'deepstack/docs/tls/python/key.pem',
                     'key.pem')
client.download_file(DIGITALOCEAN_SPACES_SPACE,
                     'deepstack/docs/tls/python/cert.pem',
                     'cert.pem')