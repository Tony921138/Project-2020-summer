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
5. it would be best to chmod all '\_data' directories (hadoop_data, jupyter_data, elk_data/ls/ls_data...) in your local directory to allow access (as shown below)

![image](https://github.com/Tony921138/Project-2020-summer/blob/master/Permit.gif)

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
5. ELK:
   - elk_data/ls/ls_data (csv files)

## ELK settings corresponding folders
1. put your pipeline .conf files in elk_data/ls/ls_pipeline (conf file for different pipelines)
2. put index templates in elk_data/ls/ls_template (json file)
3. put data in elk_data/logstash/ls_data (csv files)
4. edit elk_data/ls/ls_config/pipelines.yml for different pipeline settings
5. put graph settings (.ndjson files) in local directory for kibana import usage
6. put shell scripts in elk_data/ls/ls_scripts for importing or deleting data in logstash

### ES access
1. give access to elk_data/es/es_data (chmod) after 'docker-compose up -d'
