from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time
from datetime import datetime

# InfluxDB config
url = "http://localhost:8086"
token = "mytoken"
org = "myorg"
bucket = "mybucket"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

def generate_data():
    while True:
        point = Point("co2_capture") \
            .tag("plant", "demo1") \
            .field("temperature", round(random.uniform(30, 100), 2)) \
            .field("pressure", round(random.uniform(1, 5), 2)) \
            .field("co2_concentration", round(random.uniform(0, 10), 2)) \
            .time(datetime.utcnow(), WritePrecision.NS)

        write_api.write(bucket=bucket, org=org, record=point)
        print("Data written:", point)
        time.sleep(2)

generate_data()
