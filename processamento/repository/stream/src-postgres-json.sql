CREATE OR REPLACE STREAM ksql_stream_json
(
  "payload" STRUCT<"id" BIGINT,
                   "name" VARCHAR,
                   "gender" VARCHAR,
                   "adress" VARCHAR,
                   "houses" VARCHAR,
                   "wand" VARCHAR,
                   "patronus" VARCHAR,
                   "birth" VARCHAR,
                   "occupation" VARCHAR,
                   "dt_update" BIGINT,
                   "messagetopic" VARCHAR,
                   "messagesource" VARCHAR>
)
WITH (KAFKA_TOPIC='src-postgres-json', VALUE_FORMAT='JSON');