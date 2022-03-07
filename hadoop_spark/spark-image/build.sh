# -- Building the Images

SPARK_VERSION="3.1.2"
HADOOP_VERSION="3.2"
JUPYTERLAB_VERSION="2.2.6"

# cluster-base
docker build --no-cache \
  --platform linux/amd64 \
  -f cluster-base.Dockerfile \
  -t imok2/cluster-base .

# spark-base
docker build --no-cache \
  --platform linux/amd64 \
  --build-arg spark_version="${SPARK_VERSION}" \
  --build-arg hadoop_version="${HADOOP_VERSION}" \
  -f spark-base.Dockerfile \
  -t imok2/spark-base .

# spark-master
docker build --no-cache \
  --platform linux/amd64 \
  -f spark-master.Dockerfile \
  -t imok2/spark-master .

# spark-worker
docker build --no-cache \
  --platform linux/amd64 \
  -f spark-worker.Dockerfile \
  -t imok2/spark-worker .

# jupyterlab
docker build \
  --platform linux/amd64 \
  --build-arg spark_version="${SPARK_VERSION}" \
  --build-arg jupyterlab_version="${JUPYTERLAB_VERSION}" \
  -f jupyterlab.Dockerfile \
  -t imok2/jupyterlab .
