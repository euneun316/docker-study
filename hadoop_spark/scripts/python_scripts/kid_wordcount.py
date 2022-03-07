from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.types import ArrayType, StringType
from konlpy.tag import Mecab
import pyspark.sql.functions as F
m = Mecab()

# setting
conf = SparkConf() \
    .setAppName("kid_wordcount") \
    .setMaster("spark://spark-master:7077") \
    .set("spark.mongodb.input.uri", "mongodb://root:1234@mongodb2:27017/news_db.kid_news?authSource=admin")

sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

# function to tokenize
def ko_tokenize(article):
    noun = set(["NNG", "NNP", "NP"])
    words_list = []
    
    for word,tag in m.pos(article):
        if tag in noun:
            if word not in stopwords:
                words_list.append(word)

    return words_list

# function to retrieve date as %Y-%m-%d
def getDate(news_date):
    return news_date[:10]

# load data
df = spark.read.format("mongo").load()

# get stopwords
# ref: https://www.ranks.nl/stopwords/korean
f = open("/opt/workspace/stop_words/korean_stop_words.txt", 'r')
lines = f.readlines()
stopwords = set()
for line in lines:
    line = line.replace('\n', '')
    stopwords.add(line)
f.close()

# define udf
udf_tokenize = F.udf(ko_tokenize, ArrayType(StringType()))
udf_getDate = F.udf(getDate, StringType())

# apply function
token_df = df \
    .withColumn('article_words_list', udf_tokenize(df.news_article)) \
    .withColumn('news_date', udf_getDate(df.news_date))

# article_words_list to rows
kid_word_count = token_df \
    .select('news_date', 'article_words_list') \
    .withColumn('article_word', F.explode('article_words_list')) \
    .groupBy("news_date", 'article_word') \
    .count() \
    .orderBy("news_date", 'count')

# make kid_count_id as null for pk, rename columns
kid_word_count = kid_word_count \
    .withColumn('kid_count_id', F.lit("null")) \
    .withColumnRenamed("news_date", "kid_count_date") \
    .withColumnRenamed("article_word", "kid_count_word") \
    .withColumnRenamed("count", "kid_count_value") \
    .select("kid_count_id", "kid_count_date", "kid_count_word", "kid_count_value")

# save file in HDFS
kid_word_count \
    .write \
    .option("delimiter",'\t') \
    .save("hdfs://namenode:9000/kid_word_count", 
          format='csv',
          mode='append')

# terminate SparkSession, SparkContext
spark.stop()
sc.stop()