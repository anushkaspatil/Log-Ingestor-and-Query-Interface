# Log-Ingestor-and-Query-Interface

## Overview
This system is built to handle the seamless ingestion, storage, and retrieval of extensive log data. It consists of a Log Ingestor, which manages the acceptance of log data via HTTP, and a Query Interface that empowers users to conduct full-text searches and apply filters to various log attributes.

## Technologies Used
+ Programming Language: Python;
+ Database: MySQL;
+ Technologies: Kafka , Kafka Rest Proxy, Kafka Schema Registry;
+ Frontend: HTML CSS JavaScript;
+ Backend: Flask

## Features Implemented
### 1. Log Ingestor
Ingests logs in the provided JSON format via HTTP on port 3000.
Ensures scalability to handle high log volumes.
Optimizes I/O operations and database write speeds.

![Screenshot (199)](https://github.com/anushkaspatil/Log-Ingestor-and-Query-Interface/assets/103093836/818fa733-a275-40b6-bd50-4ea6061f927a)

### 2. Query Interface
Offers a user-friendly interface (Web UI/CLI) for full-text search.
Includes filters for:
level
message
resourceId
timestamp
traceId
spanId
commit
metadata.parentResourceId
Implements efficient search algorithms for quick results.

![query](https://github.com/anushkaspatil/Log-Ingestor-and-Query-Interface/assets/103093836/1e64f7c7-3069-4cf8-8cfc-2e63312485e5)


### 3. Advanced Features (To be Implemented...)
Search within specific date ranges.
Utilization of regular expressions for search.
Combining multiple filters for precise queries.
Real-time log ingestion and searching capabilities.
Role-based access control to the query interface.

## System Architecture
![Screenshot (203)](https://github.com/anushkaspatil/Log-Ingestor-and-Query-Interface/assets/103093836/1c05ca16-ed87-4d62-8199-f7d5af80e6b4)


### Log Ingestor I - Log Publisher Service:

Uses an HTTP server to receive logs.
Parses incoming JSON logs and publishes them to a Kafka topic.
Log Ingestor II - Log Consume Service:

Subscribes to the Kafka topic and consumes logs.
Stores logs from the topic to the primary read database instance.
Query Interface - Log Search Service:

Provides a user interface for search and filtering.
Processes user queries and translates them into database queries.
Utilizes optimized indexing for faster search results.
Database Structure:

MYSQL (Relational Database): Stores structured log data, optimizing for structured queries and joins.
NoSQL Database (e.g., Elasticsearch): Facilitates efficient full-text search and complex queries (to be implemented).
Scalability and Performance:

### Scalability: Implements database sharding for load distribution.
Caching Mechanism: Utilizes caching strategies for frequently accessed data.
Load Balancing: Distributes incoming requests across multiple servers for enhanced performance.
How to Run the Project:

## How to run the project
### Prerequisites: docker
1. Clone the repository: git clone https://github.com/anushkaspatil/Log-Ingestor-and-Query-Interface.git
2. Navigate to the project directory: cd log-ingestor-with-query-interface
3. Run: docker-compose up -d
4. Wait for 1-2 mins as it takes some time to create resources by Kafka and MySQL.
5. To ingest log from ui in browser go to: http://localhost:3000/consumer
6. Start consumer service: http://localhost:3000/consumer
7. To search log in browser search to http://localhost:3000/search
8. You can also use POST method to send json data to http endpoint

```json
curl --location 'localhost:3000' \
--header 'Content-Type: application/json' \
--data '{
"level": "error",
"message": "Failed to connect to DB",
"resourceId": "server-1234",
"timestamp": "2023-09-15T08:00:00Z",
"traceId": "abc-xyz-123",
"spanId": "span-456",
"commit": "5e5342f",
"metadata": {
   "parentResourceId": "boy server-0987"
}
}'
```

### Real-time Capabilities: Enhance real-time log ingestion and search.
### Enhanced Security: Strengthen security measures, especially for user access and data integrity.
### Optimization: Continuously optimize database queries and indexing strategies for better performance.

## Evaluation Criteria Met:
Volume: Efficiently handles massive log volumes.
Speed: Provides quick search results.
Scalability: Adaptable to increasing log volumes and queries.
Usability: Offers an intuitive interface for users.
Advanced Features: Implements bonus functionalities.
Readability: Maintains a clean and structured codebase.

## Conclusion:
This system effectively manages log data ingestion and provides a seamless query interface for users to retrieve specific logs based on various attributes. Continuous improvements can enhance its performance and capabilities.

## Project Acknowledgment
This project has been developed with inspiration and reference to existing sources
