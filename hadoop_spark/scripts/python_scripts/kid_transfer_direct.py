from pyspark import SparkContext, SparkConf, SQLContext
conf = SparkConf() \
    .setAppName("kid_transfer_direct") \
    .setMaster("spark://spark-master:7077") \
    .set("spark.mongodb.input.uri", "mongodb://root:1234@mongodb2:27017/news_db.kid_news?authSource=admin")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession
# import data from mongoDB
df = spark.read.format("mongo").load()
# make kid_count_id as null for pk, rename columns
import pyspark.sql.functions as F
df = df \
    .withColumn('kid_news_id', F.lit(0)) \
    .withColumnRenamed("news_url", "kid_news_url") \
    .withColumnRenamed("news_title", "kid_news_title") \
    .withColumnRenamed("news_subtitle", "kid_news_subtitle") \
    .withColumnRenamed("news_writer", "kid_news_writer") \
    .withColumnRenamed("news_date", "kid_news_date") \
    .withColumnRenamed("news_article", "kid_news_article") \
    .withColumnRenamed("news_img", "kid_news_img") \
    .withColumnRenamed("news_source", "kid_news_source") \
    .drop('_id') \
    .select("kid_news_id", "kid_news_url", "kid_news_title", "kid_news_subtitle",
            "kid_news_writer", "kid_news_date", "kid_news_article", "kid_news_img", "kid_news_source")
# export data to MySQL
df.write.format('jdbc') \
    .mode('append') \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://mysql2:3306/news_db?serverTimezone=UTC&useSSL=false") \
    .option("dbtable", "kid_news") \
    .option("user", "root") \
    .option("password", "1234") \
    .save()
spark.stop()
sc.stop()