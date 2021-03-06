# How to install/use Pyspark within Jupyter

## Java 8

Install Java 8:

sudo add-apt-repository ppa:webupd8team/java

Update the installer:

sudo apt update; sudo apt install oracle-java8-installer

Set the java env variables:

sudo apt install oracle-java8-set-default

Check at the end that java version is correct

java -version


## Spark-2.4.0
Download spark-2.4.0 from http://spark.apache.org/downloads.html

Unzip it and move it to a folder (just be mindful of the ownership of that folder):

tar -xzf spark-2.4.0-bin-hadoop2.7.tgz

mv spark-2.4.0-bin-hadoop2.4 /folder/spark-2.4

Add the env variables to .bashrc:

nano ~/.bashrc

export SPARK_HOME=/folder/spark-2.4.0-bin-hadoop2.7

export PATH=$SPARK_HOME/bin:$PATH

export PYSPARK_PYTHON=/home/username/anaconda3/bin/python

export PATH=$PYSPARK_PYTHON:$PATH

## Pyspark shell
Check the env variables:

echo "$SPARK_HOME"

echo "$PYSPARK_PYTHON"

echo "$PATH"

## Spark-xml
Go to https://mvnrepository.com/artifact/com.databricks/spark-xml_2.11/0.4.1 and download the jar file and then add it to the jar folder of the spark-2.4.0

## Findspark
If we want to use jupyter we can use the module findspark (https://github.com/minrk/findspark):

pip install findspark

conda config --add channels conda-forge

conda install findspark

## Jupyter

Just as an example pyspark_base.py (the books.xml file should be downloaded https://github.com/databricks/spark-xml/raw/master/src/test/resources/books.xml)

## Postgresql

Download the latest postgresql-42.2.5.jar (https://jdbc.postgresql.org/download.html) and paste it to the /folder/spark-2.4.0-bin-hadoop2.7/jar

Restart the Kernel and it will be picked up
