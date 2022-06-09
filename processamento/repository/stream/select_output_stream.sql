-- QUERY 1
SELECT
"gender",
count("houses") AS "gender_count"
FROM output_ksqldb_stream_json
GROUP BY "gender"
EMIT CHANGES;

-- QUERY 2

SELECT
"id",
"name",
"houses",
"patronus",
"dt_update"
FROM output_ksqldb_stream_json
EMIT CHANGES;