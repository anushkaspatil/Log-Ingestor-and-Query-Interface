## Assignment
Log Ingestor and Query Interface

## Objective
Develop a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.
Both the systems (the log ingestor and the query interface) can be built using any programming language of your choice.
The logs should be ingested (in the log ingestor) over HTTP, on port `3000`.
We will use a script to populate the logs into your system, so please ensure that the default port is set to the port mentioned above.

## Sample Log Data Format
The logs to be ingested will be sent in this format.
```json
{
	"level": "error",
	"message": "Failed to connect to DB",
    "resourceId": "server-1234",
	"timestamp": "2023-09-15T08:00:00Z",
	"traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "5e5342f",
    "metadata": {
        "parentResourceId": "server-0987"
    }
}
```
## Requirements
The requirements for the log ingestor and the query interface are specified below.

## Log Ingestor
- Develop a mechanism to ingest logs in the provided format.
- Ensure scalability to handle high volumes of logs efficiently.
- Mitigate potential bottlenecks such as I/O operations, database write speeds, etc.
- Make sure that the logs are ingested via an HTTP server, which runs on port `3000` by default.

## Query Interface
- Offer a user interface (Web UI or CLI) for full-text search across logs.
- Include filters based on:
    - level
    - message
    - resourceId
    - timestamp
    - traceId
    - spanId
    - commit
    - metadata.parentResourceId
- Aim for efficient and quick search results.

## Advanced Features (Bonus):
These features aren’t compulsory to implement, however, adding them might increase the chances of your submission being accepted.

- Implement search within specific date ranges.
- Utilize regular expressions for search.
- Allow combining multiple filters.
- Provide real-time log ingestion and searching capabilities.
- Implement role-based access to the query interface.

## Sample Queries
The following are some sample queries that will be executed for validation.

- Find all logs with the level set to "error".
- Search for logs with the message containing the term "Failed to connect".
- Retrieve all logs related to resourceId "server-1234".
- Filter logs between the timestamp "2023-09-10T00:00:00Z" and "2023-09-15T23:59:59Z". (Bonus)

## Evaluation Criteria
Your submission will be evaluated based on the following criteria.

- Volume: The ability of your system to ingest massive volumes.
- Speed: Efficiency in returning search results.
- Scalability: Adaptability to increasing volumes of logs/queries.
- Usability: Intuitive, user-friendly interface.
- Advanced Features: Implementation of bonus functionalities.
- Readability: The cleanliness and structure of the codebase.

## Submission
We’re accepting submissions through GitHub Classroom. Please visit the following link to join and create your submission: https://classroom.github.com/a/2sZOX9xt

Make sure to include the following things in your submission:

- The entire source code.
- A README showcasing how to run the project, the system design, a list of features implemented, and any identified issues present in the system.
- (Optional) Video or presentation showcasing the solution.

> Please ensure that you’ve also applied for the role on [our jobs portal](https://jobs.lever.co/dyte-io), or your submission **will not be evaluated**.

## Tips
Here are a few tips for completing the specified task.

- Consider hybrid database solutions (relational + NoSQL) for a balance of structured data handling and efficient search capabilities.
- Database indexing and sharding might be beneficial for scalability and speed.
- Distributed systems or cloud-based solutions can ensure robust scalability.
