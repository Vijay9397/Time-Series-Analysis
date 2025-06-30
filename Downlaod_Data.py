from influxdb_client import InfluxDBClient
import pandas as pd
import os

# InfluxDB config
client = InfluxDBClient(
    url="http://localhost:8086",
    token="mytoken",
    org="myorg"
)
query_api = client.query_api()
bucket = "mybucket"

# List of plant measurements to export
measurements = [
    "air_intake",
    "co2_absorption",
    "desorption",
    "output_tanks"
]

# Output folder (optional: create subfolder for export files)
output_dir = "exported_data"
os.makedirs(output_dir, exist_ok=True)

for measurement in measurements:
    print(f"📥 Exporting: {measurement}")
    
    query = f'''
    from(bucket: "{bucket}")
      |> range(start: -24h)
      |> filter(fn: (r) => r._measurement == "{measurement}")
      |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
    '''
    
    try:
        tables = query_api.query_data_frame(query)
        df = pd.concat(tables) if isinstance(tables, list) else tables

        if not df.empty:
            df = df.sort_values("_time")
            filename = os.path.join(output_dir, f"{measurement}.csv")
            df.to_csv(filename, index=False)
            print(f"✅ Saved: {filename}")
        else:
            print(f"⚠️ No data found for: {measurement}")
    except Exception as e:
        print(f"❌ Failed to export {measurement}: {e}")

print("✅ All done.")
