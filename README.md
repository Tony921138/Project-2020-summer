# AI / BigData project

## Docker environment setup on two VMs

1. git clone the whole repo onto vm1 and vm2
2. cd into Docker-main on vm1 and Docker-elk on vm2 
3. Be sure to commit yarn related services (resourcemanager, nodemanager, historyserver) before starting spark in vm1 (vi docker-compose.yml)
3. type in 'docker-compose up -d' to start services in both vms
4. services include:
   mongodb / adminmongo / jupyter notebook / hadoop / yarn / spark / kafka / zookeeper / mysql / mysql-workbench / ELK stack
5. it would be best to chmod all '\_data' directories (hadoop_data, jupyter_data in vm1, elk_data/es/es_data in vm2...) in your local directory to allow access (as shown below)

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
1. put pipeline .conf files in elk_data/ls/ls_pipeline (conf file for different pipelines)
2. put index templates in elk_data/ls/ls_template (json files)
3. put data in elk_data/logstash/ls_data (csv files)
4. edit elk_data/ls/ls_config/pipelines.yml for different pipeline settings
5. put graph settings (.ndjson files) in local directory for kibana import usage
6. put shell scripts in elk_data/ls/ls_scripts for importing or deleting data in logstash

### ES access
- give access to elk_data/es/es_data (chmod) after 'docker-compose up -d'

### Connecting ES to Jupyter
- before establishing connection, input commands listed below in both vms to open up port 9200
  - firewall-cmd --zone=public --add-port=9200/tcp --permanent
  - firewall-cmd --reload
  - firewall-cmd --list-ports
