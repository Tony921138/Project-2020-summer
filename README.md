AI / BigData project
====

Docker environment setup
----
1. git pull the whole repo
2. cd into the Docker-env-build directory
3. Be sure to commit yarn related services (resourcemanager, nodemanager, historyserver) before starting spark
3. type in 'docker-compose up -d' to start the service
4. services include:
   mongodb / adminmongo / jupyter notebook / hadoop / spark / kafka / zookeeper / ksql-server / ksql-cli
5. it would be best to chmod all '...data' directories (hadoop_data, jupyter_data ...) in your local
   directory to allow access

![image](https://github.com/Tony921138/Project-2020-summer/blob/master/access.gif)

## Data storage corresponding folders
### mkdir independent folders in jupyter_data for distinct data input
1. hdfs:
   - hadoop_data (hadoop fs -put) / jupyter_data (use hadoop codes)
2. mongodb:
   - jupyter_data (use pymongo codes)
3. spark:
   - jupyter_data (.ipynb codes) / spark_data (use spark-submit commands)
4. mysql:
   - jupyter_data (use pymysql codes) / mysql_data (use sql commands / source .sql files from here)

## ELK data corresponding folders
1. put your pipeline .conf files in /elk_data/logstash/ls_pipeline
2. put index templates in /elk_data/logstash/ls_template
3. put data in /elk_data/logstash/ls_data (csv files)
4. put graph settings (.ndjson files) in local machine's folder for kibana import usage
5. put shell scripts in /elk_data/logstash/ls_scripts for importing or deleting data in logstash
### ES access and LS pipelines
1. give access to elk_data/elasticsearch/es_data (chmod)
2. vi /elk_data/logstash/ls_config/pipelines.yml (config your own pipeline)
