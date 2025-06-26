import boto3
import json
import time
import random
from datetime import datetime

# Replace the region if yours is different
kinesis = boto3.client('kinesis', region_name='us-east-2')

products = ["Laptop", "Phone", "Tablet", "Headphones", "Monitor"]

def generate_sale():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "product": random.choice(products),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(100.0, 1000.0), 2)
    }

while True:
    sale_record = generate_sale()
    print("Sending sale:", sale_record)

    kinesis.put_record(
        StreamName="sales_stream",  # This must match exactly with your Kinesis stream
        Data=json.dumps(sale_record),
        PartitionKey="partitionkey"
    )

    time.sleep(2)
