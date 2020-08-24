# AI / BigData project

## Docker environment setup

1. git clone the whole repo
2. cd into Docker-main
3. Be sure to commit yarn related services (resourcemanager, nodemanager, historyserver) before starting spark
3. type in 'docker-compose up -d' to start services
4. services include:
   mongodb / adminmongo / jupyter notebook / hadoop / yarn / spark / kafka / zookeeper / mysql / mysql-workbench / ELK stack / ngrok
5. it would be best to chmod all '\_data' directories (hadoop_data, jupyter_data, elk_data/es/es_data...) in your local directory to allow access (as shown below)

![image](https://github.com/Tony921138/Project-2020-summer/blob/master/Permit.gif)

## Data storage corresponding folders
### make independent folders in jupyter_data for distinct data input
1. hdfs:
   - hadoop_data (hadoop fs -put) / jupyter_data (hadoop codes)
2. mongodb:
   - jupyter_data (pymongo codes)
3. spark:
   - jupyter_data (pyspark codes) / spark_data (use spark-submit commands)
4. mysql:
   - jupyter_data (pymysql codes) / mysql_data (use sql commands / source .sql files from here)
5. ELK:
   - elk_data/ls/ls_data (csv files)

## ELK settings corresponding folders
1. put pipeline .conf files in elk_data/ls/ls_pipeline (conf file for different pipelines)
2. put index templates in elk_data/ls/ls_template (json files)
3. put data in elk_data/logstash/ls_data (csv files)
4. edit elk_data/ls/ls_config/pipelines.yml for different pipeline settings
5. put graph settings (.ndjson files) in any local directory for kibana import usage
6. put shell scripts in elk_data/ls/ls_scripts for importing or deleting data in logstash

### establishing ES nodes
- give access to elk_data/es/es_data (chmod) after 'docker-compose up -d'

### Connecting ES to Jupyter
- before establishing connection, input commands listed below to open up port 9200
  - firewall-cmd --zone=public --add-port=9200/tcp --permanent
  - firewall-cmd --reload
  - firewall-cmd --list-ports

## Docker security env settings
1. mongodb / mysql 
  - before adding you files into the corresponding folders, please change the user name and password for mongodb and mysql
  - connect to mysql by using mysql workbench 
    - connection name: <connection_name>
    - hostname: <mysql_container_name>
    - port: <mysql_container_connection_port>
    - username: <your_username>
    - password: <your_password>
  - connect to mongodb by using adminmongo
    - connection name: <connection_name>
    - connection string: <mongodb://<username>:<password>@<mongodb_container_name>:<mongodb_connection_port>>
2. jupyter notebook
   - use "docker exec -it jupyter bash" to get into the container
   - use "jupyter notebook list" to get your token
   - input your token at http://<vm_ip>:8888
