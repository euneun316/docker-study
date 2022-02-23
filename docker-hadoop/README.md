# docker-hadoop

## m1 image build
```
docker build --platform linux/amd64 -t imok2/hadoop-base:hadoop3.2.2-java8 ./base
docker build --platform linux/amd64 -t imok2/hadoop-namenode:hadoop3.2.2-java8 ./namenode
docker build --platform linux/amd64 -t imok2/hadoop-datanode:hadoop3.2.2-java8 ./datanode
docker build --platform linux/amd64 -t imok2/hadoop-resourcemanager:hadoop3.2.2-java8 ./resourcemanager
docker build --platform linux/amd64 -t imok2/hadoop-nodemanager:hadoop3.2.2-java8 ./nodemanager
docker build --platform linux/amd64 -t imok2/hadoop-historyserver:hadoop3.2.2-java8 ./historyserver
```
