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

## Raw data storage

