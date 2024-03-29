FROM imok2/cluster-base:spark3.1.2 

# -- Layer: JupyterLab

ARG spark_version=3.1.2
ARG jupyterlab_version=2.2.6

RUN pip3 install wget pyspark==${spark_version} jupyterlab==${jupyterlab_version}

# -- Runtime

EXPOSE 8886
WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8886 --no-browser --allow-root --NotebookApp.token=
