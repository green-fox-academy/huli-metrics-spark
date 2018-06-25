# huli-metrics-spark
environment for data mining

### Dear Huli Developer!

This is a spark + hadoop environment for data mining jobs configured for s3 bucket reading.
At the end you will find a Spark image which has an exmaple python script to write data to an already running MapD.
You will need to ask for credentials at your DevOps team for security reasons.

# First you need to install Docker, if you already have you can skip these steps

#### (please use the Stable version!)

### [Windows](https://docs.docker.com/docker-for-windows/install/)

### [Mac](https://docs.docker.com/docker-for-mac/)

### [Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Clone the github repo

https://github.com/green-fox-academy/huli-metrics-spark

## Build docker image
With "-t" you can tag your image for terminal access

```
docker build . -t <yourImageName>
```

### Enter into the container
You can enter immediately to the container and working with it
With -v flag you can mount your working directory to share your proccess into the container

```
docker run -it -v ${PWD}/app:/home <yourImageName> bash
```
You need to copy your python script into your "${PWD}/app" folder and it will be mounted in your container "/home" folder

### Run your python script inside the container
To start your job with spark simply run your script with spark-submit command in your container

```
spark-submit yourPythonScript.py
```

### Spark with MapD setup 
This build needs and image from Dockerhub(You need an account for it)

Download the image

```
docker pull greenfox/huli-metrics-spark:latest
```

This image have extra jar files which is needed for MapD configuration.
You cannot download these jar files from Maven Central :'(

### Run the image 
Everything is the same as we did it before

```
docker run -it -v ${PWD}/app:/home greenfox/huli-metrics-spark bash
```

## Description about example script for MapD

You need to change for correct Public DNS address to reach MapD
9091 port is the HTTP backend side of MapD which you need for writing data

```
url = 'jdbc:mapd:<MapD_Public_DNS>:9091:mapd'
```

You can set your script to any S3 bucket from GreenFox to Read or Write 
Spark is able to read any files(.json, .txt, .parquet)...

```
df = spark.read.json("s3a://Bucket-name/your-file.json")
```

This piece of code shows json itself in your terminal

```
df.select(df['application'], df['some_date'], df['useful_data']).show()
         df.createOrReplaceTempView("huliExample")
```
