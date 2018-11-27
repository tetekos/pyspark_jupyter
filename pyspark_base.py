import findspark

findspark.init('/home/folder/spark-2.4.0-bin-hadoop2.7')

from pyspark import SparkConf, SparkContext

from pyspark.sql import SQLContext, Row,SparkSession

spark = SparkSession.builder.master("local[*]").appName("Word Count").getOrCreate()

df = spark.read.format('com.databricks.spark.xml').options(rowTag='book').load('/Downloads/books.xml')

df.show(12)

df.select("author", "_id").write 
.format('com.databricks.spark.xml') 
.options(rowTag='book', rootTag='books') 
.save('newbooks.xml')
