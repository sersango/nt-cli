# Massage Broker

The aim of this project is to produce a *protobuf* message through a broker (Kafka) and receive it in one or more consumers.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages.
```bash
pip install kafka-python
pip install protobuf
```
In addition, you also need to got installed `docker-compose`.


## How to run
### Kafka
First of all, it is necessary to set up Kafka broker.
```bash
cd kafka-docker
docker-compose up
```
This container is exposed through the port 9002.

### Consumers
Set up all consumers that you want. These are subscribed to the topic `protopic` and get all the messages pushed to it. Execute the following command in multiple terminals.
```bash
cd python/
python consumer.py
```  

### Producer 
The producer get a unique param. This one must be a file that contains a JSON. Producer take this files, parses the JSON and send it through the broker publishing in the same topic that the consumers are subscribed: `protopic`. To execute the producer, run this command:
```bash
cd python/
python producer.py <JSON_FILE>
```
You can use `json.txt` as example.


## TODO
* Unify both consumer and producer scripts in a unique command line application.
* Parse JSON to a Protobuf message and send it through the broker in the same way that JSON structure.

## Improvements
* Send a topic as a parameter.