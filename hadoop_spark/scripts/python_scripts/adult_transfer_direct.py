from pyspark import SparkContext, SparkConf, SQLContext
import pyspark.sql.functions as F
# setting
conf = SparkConf() \
    .setAppName("adult_transfer") \
    .setMaster("spark://spark-master:7077") \
    .set("spark.mongodb.input.uri", "mongodb://root:1234@mongodb2:27017/news_db.adult_news?authSource=admin")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession
# load data
df = spark.read.format("mongo").load()
# make adult_news_id as null for pk, rename columns
df = df \
    .withColumn('adult_news_id', F.lit(0)) \
    .withColumnRenamed("news_url", "adult_news_url") \
    .withColumnRenamed("news_title", "adult_news_title") \
    .withColumnRenamed("news_subtitle", "adult_news_subtitle") \
    .withColumnRenamed("news_wrtier", "adult_news_writer") \
    .withColumnRenamed("news_date", "adult_news_date") \
    .withColumnRenamed("news_article", "adult_news_article") \
    .withColumnRenamed("news_source", "adult_news_source") \
    .drop('_id') \
    .select("adult_news_id", "adult_news_url", "adult_news_title", "adult_news_subtitle", "adult_news_writer", "adult_news_date", "adult_news_article", "adult_news_source")
# export data to MySQL
df.write.format('jdbc') \
    .mode('append') \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://mysql2:3306/news_db?serverTimezone=UTC&useSSL=false") \
    .option("dbtable", "adult_news") \
    .option("user", "root") \
    .option("password", "1234") \
    .save()
spark.stop()
sc.stop()