import os
from logging import INFO

LOG_FORMAT = '%(asctime)s - %(levelname)6s - %(message)s'
LOG_LEVEL = INFO

proxy_token = os.environ.get('PROXY_TOKEN', 'my-token')

def get_influxdb_info():
    host = os.environ.get('INFLUXDB_HOST', 'localhost')
    port = os.environ.get('INFLUXDB_PORT', 8086)
    token = os.environ.get('INFLUXDB_TOKEN', '')
    org = os.environ.get('INFLUXDB_ORG', '')
    bucket = os.environ.get('INFLUXDB_BUCKET', '')
    return dict(url=f"http://{host}:{port}", token=token, org=org, bucket=bucket)
