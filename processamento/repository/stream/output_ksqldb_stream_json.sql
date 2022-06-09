CREATE OR REPLACE STREAM output_ksqldb_stream_json
WITH (KAFKA_TOPIC='output-ksqldb-stream-json', PARTITIONS=3, VALUE_FORMAT='JSON')
AS
SELECT
AS_VALUE("payload"->"id") as "business_key",
"payload"->"id" as "id",
"payload"->"name",
"payload"->"gender",
"payload"->"houses",
"payload"->"patronus",
"payload"->"dt_update"
FROM ksql_stream_json
EMIT CHANGES;