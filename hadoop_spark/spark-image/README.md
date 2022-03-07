# docker-spark

## m1 image build
```bash
# cluster-base
docker build --no-cache --platform linux/amd64 -f cluster-base.Dockerfile -t imok2/cluster-base .
# spark-base
docker build --no-cache --platform linux/amd64 -f spark-base.Dockerfile -t imok2/spark-base .
# spark-master
docker build --no-cache --platform linux/amd64 -f spark-master.Dockerfile -t imok2/spark-master .
# spark-worker
docker build --no-cache --platform linux/amd64 -f spark-worker.Dockerfile -t imok2/spark-worker .
# jupyterlab
docker build --no-cache --platform linux/amd64 -f jupyterlab.Dockerfile -t imok2/jupyterlab .
```

## build.sh
```
sh ./docker-study/hadoop_spark/spark-image/build.sh
```

