import abc
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

from rockblock_proxy.model import RBMessage
from rockblock_proxy.config import get_influxdb_info


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, msg: RBMessage):
        raise NotImplementedError


class InfluxDBRepository(AbstractRepository):

    def add(self, msg: RBMessage):
        influxdb_info = get_influxdb_info()

        url = influxdb_info.get('url')
        token = influxdb_info.get('token')
        bucket = influxdb_info.get('bucket')
        org = influxdb_info.get('org')

        msg.data = float(bytes.fromhex(msg.data.decode()).decode())

        with InfluxDBClient(url=url, token=token, org=org) as client:

            write_api = client.write_api(write_options=SYNCHRONOUS)

            point = Point("temperature") \
                .tag("device", msg.imei) \
                .field("lat", msg.iridium_latitude) \
                .field("lon", msg.iridium_longitude) \
                .field("value", msg.data) \
                .time(datetime.utcnow(), WritePrecision.NS)

            write_api.write(bucket=bucket , record=point)

        return msg
