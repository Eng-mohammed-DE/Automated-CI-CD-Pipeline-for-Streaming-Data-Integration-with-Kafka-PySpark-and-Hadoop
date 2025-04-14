from kafka import KafkaProducer
import json
import time

# Kafka Producer Configuration
producer = KafkaProducer(bootstrap_servers='192.168.1.39:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

topic = 'node101' 

while True:
    message = {"sensor_id": "123", "temperature": 25}
    producer.send(topic, message)
    print(f"Sent to {topic}: {message}")
    time.sleep(2)
