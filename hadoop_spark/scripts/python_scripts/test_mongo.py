from pyspark import SparkContext, SparkConf, SQLContext

conf = SparkConf() \
    .setAppName("test_mongo") \
    .setMaster("spark://spark-master:7077") \
    .set("spark.mongodb.input.uri", "mongodb://root:1234@mongodb2:27017/newsDB.kid_chosun?authSource=admin")


sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

df = spark.read.format("mongo").load()
df.show(3)

sc.stop()
spark.stop()