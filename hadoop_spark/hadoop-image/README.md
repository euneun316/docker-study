# docker-hadoop

## m1 image build
```bash
#hadoop-base
docker build --platform linux/amd64 --no-cache -t imok2/hadoop-base:hadoop3.2.2-java8 ./base
#hadoop-datanode
docker build --platform linux/amd64 --no-cache -t imok2/hadoop-datanode:hadoop3.2.2-java8 ./datanode
#hadoop-historyserver
docker build --platform linux/amd64 --no-cache -t imok2/hadoop-historyserver:hadoop3.2.2-java8 ./historyserver
#hadoop-namenode
docker build --platform linux/amd64 --no-cache -t imok2/hadoop-namenode:hadoop3.2.2-java8 ./namenode
#hadoop-namenode-sqoop
docker build --platform linux/amd64 --no-cache -t imok2/hadoop-namenode-sqoop:hadoop3.2.2-sqoop1.4.7 ./namenode-sqoop
#hadoop-nodemanager
docker build --platform linux/amd64 --no-cache -t imok2/hadoop-nodemanager:hadoop3.2.2-java8 ./nodemanager
#hadoop-resourcemanager
docker build --platform linux/amd64 --no-cache -t imok2/hadoop-resourcemanager:hadoop3.2.2-java8 ./resourcemanager
```

## build.sh
```
sh ./docker-study/hadoop_spark/hadoop-image/build.sh
```

## reference

https://github.com/big-data-europe/docker-hadoop
