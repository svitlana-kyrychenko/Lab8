docker build -f ./kafka_write/Dockerfile . -t write_kafka:1.0
docker run --network kafka-network --rm write_kafka:1.0