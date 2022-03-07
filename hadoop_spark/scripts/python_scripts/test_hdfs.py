from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import col

conf = SparkConf() \
    .setAppName("test_mongoToMySQL1") \
    .setMaster("spark://spark-master:7077") \
    .set("spark.mongodb.input.uri", "mongodb://root:1234@mongodb2:27017/newsDB.kid_chosun?authSource=admin")


sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

df = spark.read.format("mongo").load()

df_filtered = df \
    .withColumn('news_date', regexp_replace('news_date', '\.', '-')) \
    .withColumn('news_date', (col('news_date').cast('date'))) \
    .filter(col('news_date') >= '2022-01-01') \
    .select('news_title', 'news_date', 'news_source', 'news_url')

df_filtered \
    .write \
    .option("delimiter",'\t') \
    .save("hdfs://namenode:9000/test", 
          format='csv',
          mode='append')