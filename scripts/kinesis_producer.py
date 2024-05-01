import boto3
import json
import time
import random

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis')

def put_weather_data(city, temperature, humidity):
    try:
        data = {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": int(time.time())
        }

        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=city
        )
        print(f"Weather data written to Kinesis. SequenceNumber: {response['SequenceNumber']}, ShardId: {response['ShardId']}, Data: {data}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]

    for _ in range(5):
        city = random.choice(cities)
        temperature = round(random.uniform(10, 30), 2)
        humidity = round(random.uniform(40, 80), 2)

        put_weather_data(city, temperature, humidity)
        time.sleep(2)  # Simulating periodic data transmission

