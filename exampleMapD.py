import os
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

if __name__ == "__main__":

     accesskey = os.environ.get('AWS_ACCESS_KEY')
     secretkey = os.environ.get('AWS_SECRET_KEY')

     if accesskey and secretkey:

         driver = 'com.mapd.jdbc.MapDDriver'
         url = 'jdbc:mapd:MapD_Public_DNS:9091:mapd'
         user = 'mapd'
         password = 'HyperInteractive'
         table = 'huliExample'

         spark = SparkSession \
                    .builder \
                    .appName("mapd") \
                    .config("spark.hadoop.fs.s3a.access.key", accesskey) \
                    .config("spark.hadoop.fs.s3a.secret.key", secretkey) \
                    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
                    .config("spark.hadoop.fs.s3a.endpoint","s3-eu-central-1.amazonaws.com") \
                    .config("spark.hadoop.com.amazonaws.services.s3.enableV4", "true") \
                    .getOrCreate()

         df = spark.read.json("s3a://Bucket-name/your-files")

         df.select(df['application'], df['some_date'], df['useful_data']).show()
         df.createOrReplaceTempView("huliExample")

         dfWrite = spark.sql(""" SELECT * FROM huliExample """)

         dfWrite.write.format('jdbc') \
                  .options(driver = driver) \
                  .options(url = url) \
                  .options(dbtable = table) \
                  .options(user = user) \
                  .options(password = password).mode("append").save()

     else:

         print("---------------------------------------------------------------------")
         print("----------------- Please check your credentials ---------------------")
         print("--- If you still struggling please contact with your DevOps team ----")
         print("---------------------------------------------------------------------")
