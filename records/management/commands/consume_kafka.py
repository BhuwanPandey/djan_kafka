"""
This module defines a Django management command to consume messages from a Kafka topic
and store them in the FaceEmbed model within the database.
"""

import json
from datetime import datetime

from decouple import config
from django.core.management.base import BaseCommand
from kafka import KafkaConsumer

from records.models import FaceEmbed

# Assign private_ip
PRIVATE_IP = config("PRIVATE_IP")


class Command(BaseCommand):
    help = "Consume Kafka topic and store in Django model"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="The number of messages to consume")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        consumer = KafkaConsumer(
            "face.embed.data",
            bootstrap_servers=f"{PRIVATE_IP}:9092",
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="face-embed-group",
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
        )
        datastore = []
        for target, message in enumerate(consumer):
            if target >= count:  # Stop consuming after reaching the count
                break
            data = message.value
            datastore.append(
                FaceEmbed(
                    age=data["age"],
                    emotion=data["emotion"],
                    gender=data["gender"],
                    timestamp=datetime.fromisoformat(data["timestamp"]),
                )
            )
            if len(datastore) > 1000:
                FaceEmbed.objects.bulk_create(datastore, batch_size=500)
                self.stdout.write(f"Successfully Stored {len(datastore)} records on DB")

        if len(datastore) > 0:
            FaceEmbed.objects.bulk_create(datastore)
            self.stdout.write(f"Successfully Stored {len(datastore)} records on DB")
