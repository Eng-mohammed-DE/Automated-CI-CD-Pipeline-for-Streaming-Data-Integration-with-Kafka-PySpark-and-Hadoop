
from kafka import KafkaProducer
import json
import random
import time

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# List of employee names and departments
names = ['Ali', 'omer', 'hassan', 'sara', 'mohammed']
departments = ['HR', 'Finance', 'Engineering', 'Marketing', 'Sales']

# Function to generate random employee data and send to Kafka
def produce_data():
    while True:
        employee_data = {
            'name': random.choice(names),
            'department': random.choice(departments)
        }
        
        # Send employee data to Kafka topic 'employee_data'
        producer.send('node101', value=employee_data)

        time.sleep(1)  # Send data every 1 second

if __name__ == "__main__":
    produce_data()
