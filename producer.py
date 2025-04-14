from kafka import KafkaProducer
import json
import time

# Kafka Producer Configuration
producer = KafkaProducer(bootstrap_servers='192.168.1.39:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
request_timeout_ms=120000 

# Infinite loop to send data to Kafka
while True:
    message = {"sensor_id": "123", "temperature": 25}
    producer.send('node101', message)
    print(f"Sent: {message}")
    time.sleep(2)  # Simulate sending data every 2 seconds