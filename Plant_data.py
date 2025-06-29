import random
import time
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# InfluxDB configuration
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = "mytoken"
INFLUX_ORG = "myorg"
INFLUX_BUCKET = "mybucket"

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = client.write_api(write_options=SYNCHRONOUS)

def simulate_air_intake_unit():
    for unit_id in range(1, 7):
        point = Point("air_intake") \
            .tag("unit", f"intake_{unit_id}") \
            .field("intake_rpm", random.uniform(1200, 1500)) \
            .field("output_rpm", random.uniform(1100, 1450)) \
            .field("air_efficiency", random.uniform(70, 100)) \
            .field("temperature", random.uniform(25, 40)) \
            .field("pressure", random.uniform(1.0, 2.0)) \
            .field("vibration", random.uniform(0.1, 1.5)) \
            .time(datetime.utcnow(), WritePrecision.NS)
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)

def simulate_co2_absorption_unit():
    #for node in range(1, 5):
    point = Point("co2_absorption") \
        .field("temperature", random.uniform(40, 60)) \
        .field("pressure", random.uniform(1.5, 3.0)) \
        .field("absorption_rate", random.uniform(0.6, 0.95)) \
        .field("co2_concentration", random.uniform(5, 10)) \
        .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)

def simulate_desorption_unit():
    #for node in range(1, 7):
    point = Point("desorption") \
        .field("temperature", random.uniform(50, 80)) \
        .field("pressure", random.uniform(1.0, 2.5)) \
        .field("oxygen_concentration", random.uniform(10, 30)) \
        .field("co2_desorption_rate", random.uniform(0.5, 0.9)) \
        .field("h2_concentration", random.uniform(2, 5)) \
        .field("co2_concentration", random.uniform(5, 15)) \
        .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)

def simulate_output_storage_units():
    point = Point("output_tanks") \
        .field("tank_level_o2", random.uniform(20, 100)) \
        .field("tank_level_h2", random.uniform(20, 100)) \
        .field("tank_level_co2", random.uniform(20, 100)) \
        .field("purity_o2", random.uniform(85, 99)) \
        .field("purity_h2", random.uniform(80, 98)) \
        .field("purity_co2", random.uniform(75, 95)) \
        .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)

def run_simulation():
    while True:
        simulate_air_intake_unit()
        simulate_co2_absorption_unit()
        simulate_desorption_unit()
        simulate_output_storage_units()
        print("Data written to InfluxDB for all units.")
        time.sleep(5)

if __name__ == "__main__":
    run_simulation()
