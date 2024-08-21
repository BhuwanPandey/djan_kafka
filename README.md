## Kafka Integration with Django Model and REST API

Tech Stack:
- Python 3.11 
- Sqlite
- Docker
- Zookeeper (where kafka depends on)
- Apache Kafka


## Project Setup Instructions
Git clone the repository 
```
https://github.com/BhuwanPandey/djan_kafka.git
```
Change the directory into netflix
```
cd djan_kafka
```

## Task 1
Solution is  present as file named inversion.py, To run this try
```
python inversion.py
```

## Task 2
1. Create a virtual env
```
python -m venv env
```
2. Activate env
```
env\scripts\activate
```
3. Install Dependancies
```
pip install -r requirements.txt
```
4. Make Migrations
```
python manage.py makemigrations
```
5. Migrate DB
```
python manage.py migrate
```

6. Create the .env file and add
You can find ip address with ipconfig command on window
```
PRIVATE_IP=
```
#### Run extra service with Docker

7. Setup Zookeeper
Zookeeper is an essential component in distributed systems, particularly when working with Apache Kafka.
```
docker run --rm --name kafka-zookeeper -p 2181:2181 zookeeper
```
8. Setup Kafka
Kafka is commonly used for building real-time data pipelines, stream processing applications, and event-driven systems, handling large volumes of data across multiple sources with reliability and scalability.
```
 docker run -p 9092:9092 --rm --name kafka-server \
 -e KAFKA_ZOOKEEPER_CONNECT=<private_ip>:2181 \
 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://<private_ip>:9092 \
 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
 confluentinc/cp-kafka
```

9. Run the django server
```
python manage.py runserver
```

10. Run the kafka producer
```
python kafka_producer.py
```

11. Run the kafka consumer
```
python manage.py consume_kafka  or
python manage.py consume_kafka 100  ( this will store 100 records on DB)
```

12. Visit below to get list of records 
```
http://127.0.0.1:8000/api/face_embed/
```

