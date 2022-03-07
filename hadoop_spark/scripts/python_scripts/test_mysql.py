from pyspark import SparkContext, SparkConf, SQLContext

conf = SparkConf() \
    .setAppName("test_JDBC") \
    .setMaster("spark://spark-master:7077")

sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

df = spark.read.format("jdbc") \
                .option("driver", "com.mysql.cj.jdbc.Driver") \
                .option("url", "jdbc:mysql://mysql2:3306/employee?serverTimezone=UTC&useSSL=false") \
                .option("dbtable", "dept_csv") \
                .option("user", "root") \
                .option("password", "1234") \
                .load()

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

data = [("SPORTS","SEOUL",60)]

schema = StructType([
    StructField("dname", StringType(),True),
    StructField("loc", StringType(),True),
    StructField("deptno", IntegerType(),True)
  ])
 
df_2 = spark.createDataFrame(data=data, schema=schema)
df_2.show(truncate=False)

df_2.write.format('jdbc') \
    .mode('append') \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://mysql2:3306/employee?serverTimezone=UTC&useSSL=false") \
    .option("dbtable", "dept_csv") \
    .option("user", "root") \
    .option("password", "1234") \
    .save()

sc.stop()
spark.stop()