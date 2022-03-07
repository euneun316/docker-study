# docker-spark

## m1 image build
```bash
# cluster-base
docker build --no-cache -f cluster-base.Dockerfile -t imok2/cluster-base:spark3.1.2 .
# spark-base
docker build --no-cache -f spark-base.Dockerfile --build-arg spark_version="3.1.2" --build-arg hadoop_version="3.2" -t imok2/spark-base:spark3.1.2 .
# spark-master
docker build --no-cache -f spark-master.Dockerfile -t imok2/spark-master:spark3.1.2 .
# spark-worker
docker build --no-cache -f spark-worker.Dockerfile -t imok2/spark-worker:spark3.1.2 .
# jupyterlab
docker build --no-cache -f jupyterlab.Dockerfile --build-arg spark_version="3.1.2" --build-arg jupyterlab_version="2.2.6" -t imok2/jupyterlab:spark3.1.2 .
```

## build.sh
```
sh ./docker-study/hadoop_spark/spark-image/build.sh
```

