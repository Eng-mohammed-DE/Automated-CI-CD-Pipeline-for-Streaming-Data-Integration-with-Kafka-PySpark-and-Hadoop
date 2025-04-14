# my spark scrip here venv3.10/include/spark_consumer.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder \
    .appName("data_lake") \
    .master("local[*]") \
    .config("spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1,"
            "org.apache.commons:commons-pool2:2.11.1,"
            "org.slf4j:slf4j-api:1.7.36") \
    .getOrCreate()

schema = StructType().add("name", StringType()).add("department", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "stage-topic") \
    .option("startingOffsets", "latest") \
    .option("maxOffsetsPerTrigger", 1000) \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
            .select(from_json(col("value"), schema).alias("data")) \
            .select("data.*")

query = json_df.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("checkpointLocation", "/user/hadoop/checkpoints/raw_employee_data") \
    .option("path", "/user/hadoop/raw_employee_data/") \
    .start()

query.awaitTermination()
    