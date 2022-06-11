docker build -f ./cassandra_read/Dockerfile . -t reed_cassandra:1.0
docker run --network kafka-network --rm reed_cassandra:1.0