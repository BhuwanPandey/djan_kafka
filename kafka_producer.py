import datetime
import json
import random

from decouple import config
from kafka import KafkaProducer

# Assign private_ip
PRIVATE_IP = config("PRIVATE_IP")

# Kafka Producer configuration
producer = KafkaProducer(
    bootstrap_servers=f"{PRIVATE_IP}:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


# Data generation for FaceEmbed model
def generate_face_embed_data():
    emotions = ["happy", "sad", "angry", "neutral"]
    genders = ["male", "female", "other"]

    data = {
        "age": random.randint(18, 80),
        "emotion": random.choice(emotions),
        "gender": random.choice(genders),
        "timestamp": datetime.datetime.now().isoformat(),
    }
    return data


# Send data to Kafka topic
def send_data_to_kafka():
    data = generate_face_embed_data()
    producer.send("face.embed.data", data)
    producer.flush()
    print(f"Sent data to Kafka: {data}")


# Generate and send data continuously
if __name__ == "__main__":
    while True:
        send_data_to_kafka()
