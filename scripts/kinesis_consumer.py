import boto3
import json
import time
# Initialize Kinesis client
kinesis_client = boto3.client('kinesis')

def get_shard_iterator():
    response = kinesis_client.get_shard_iterator(
        StreamName=stream_name,
        ShardId='shardId-000000000003',  # Replace with your shard ID
        ShardIteratorType='TRIM_HORIZON'
    )
    return response['ShardIterator']

def get_records(shard_iterator):
    response = kinesis_client.get_records(
        ShardIterator=shard_iterator,
        Limit=10
    )
    return response.get('Records', []), response.get('NextShardIterator')

def process_weather_data(data):
    print(f"Received Weather Data: {data}")

if __name__ == "__main__":
    shard_iterator = get_shard_iterator()

    while True:
        records, next_shard_iterator = get_records(shard_iterator)
        for record in records:
            data = json.loads(record['Data'])
            process_weather_data(data)

        if not next_shard_iterator:
            print("No more records in the shard. Exiting.")
            break

        shard_iterator = next_shard_iterator
        time.sleep(2)  # Add a delay between reads (adjust as needed)

## To remove kinesis datastream using awscli in a jupyter notebook
## !aws kinesis delete-stream --stream-name Fxweatherstream

