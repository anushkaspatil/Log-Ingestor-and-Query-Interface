#This Flask app lets you easily add logs to Kafka and search through them in a MySQL database.

from flask import Flask, render_template, request, jsonify
from .log_ingestor import LogIngestor
from .log_consumer import KafkaLogConsumer
from .query_interface import Database
import logging
import threading
import requests

# app = Flask(__name__, template_folder='frontend/templates')
app = Flask(__name__, static_folder='../frontend/static',template_folder='../frontend/templates', static_url_path='/')


kafka_url = "http://kafka-rest-proxy:8082/topics/log-ingestor"
# kafka_url = "http://localhost:8082/topics/log-ingestor"
log_ingestor = LogIngestor(kafka_url)

user = 'anushka'
pswd = 'anushka'
host = 'mysql-write'
# host = 'localhost'
port = 3306
database_name = 'log_ingestor_db'
db = Database(user, pswd, host, port, database_name)

# kafka_bootstrap_servers='localhost:9092'
kafka_bootstrap_servers = 'kafka1:19092'
consumer_group='log_consumer_group'
kafka_topic='log-ingestor'

def start_log_consumer_thread():
    """
    Start reading logs from Kafka by running a Kafka log consumer in a separate thread. Just create a KafkaLogConsumer and let it begin fetching logs for you.

    """
    consumer = KafkaLogConsumer(
        user=user,
        pswd=pswd,
        host=host,
        port=port,
        database_name=database_name,
        kafka_bootstrap_servers=kafka_bootstrap_servers,
        consumer_group=consumer_group,
        kafka_topic=kafka_topic
    )
    consumer.consume_and_store_logs()

@app.route('/consumer')
def start_log_consumer():
    t = threading.Thread(target=start_log_consumer_thread)
    t.start()
    return 'Log consumer started in a separate thread.'

@app.route('/', methods=['GET','POST'])
def publish_to_kafka():

    if request.method == 'GET':
        return render_template('ingestor.html')
        # return jsonify({"error": "Invalid request GET method for this endpoint : This endpoint is used for ingesting data please use POST"}), 400

    log_data = request.json  # incoming data is in JSON format
    logging.info(f'Incoming log data: {log_data}')

    # prepare data for publishing to Kafka
    kafka_data = {
        "records": [
            {
                "value": {
                    "level": log_data.get("level", "info"),
                    "message": log_data.get("message", ""),
                    "resourceId": log_data.get("resourceId", ""),
                    "timestamp": log_data.get("timestamp", ""),
                    "traceId": log_data.get("traceId", ""),
                    "spanId": log_data.get("spanId", ""),
                    "commit": log_data.get("commit", ""),
                    "metadata": {
                        "parentResourceId": log_data.get("metadata","").get("parentResourceId", "")
                    }
                }
            }
        ]
    }

    # Publishing data to Kafka

    status = log_ingestor.publish_to_kafka(kafka_data)
    if status:
        return jsonify({"message": "Data published to Kafka successfully."}), 200

    logging.error(f"Failed to publish data to Kafka.")
    return jsonify({"error": "Failed to publish data to Kafka."}), 500

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        print(f'for data {request.form}')
        search_field = request.form['searchField']
        search_query = request.form['searchQuery']

        filter_criteria = {
            search_field: search_query
            }

        # Based on the search criteria filter the logs
        db = Database(user, pswd, host, port, database_name) # adding this becuase sql is querying old data
        filtered_logs = db.get_logs_by_filter(filter_criteria)

        # list of tuples is being converted into a list of dictionaries
        logs = [
            {
                'id': log[0],
                'level': log[1],
                'message': log[2],
                'resourceId': log[3],
                'timestamp': log[4].strftime('%Y-%m-%d %H:%M:%S'),  # Format datetime as string
                'traceId': log[5],
                'spanId': log[6],
                'commit': log[7],
                'parentResourceId': log[8]
            }
            for log in filtered_logs
        ]

        return render_template('query.html', logs=logs)

    return render_template('query.html')


if __name__ == '__main__':
    # When your Flask app starts, simply send a request to initiate the log consumer by calling the "start_log_consumer" method.
    requests.get('http://localhost:3000/consumer')

    app.run(debug=True, port=3000)
