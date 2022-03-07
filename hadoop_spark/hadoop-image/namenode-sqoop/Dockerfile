FROM imok2/hadoop-base:hadoop3.2.2-java8

HEALTHCHECK CMD curl -f http://localhost:9870/ || exit 1

ENV HDFS_CONF_dfs_namenode_name_dir=file:///hadoop/dfs/name
RUN mkdir -p /hadoop/dfs/name
VOLUME /hadoop/dfs/name

ADD run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 9870

# -----
# SQOOP
# -----
ENV SQOOP_VERSION 1.4.7

# Download & uncompress Apache Sqoop v1.4.7.
RUN set -x && \
    curl -LO http://archive.apache.org/dist/sqoop/$SQOOP_VERSION/sqoop-$SQOOP_VERSION.bin__hadoop-2.6.0.tar.gz && \
    tar zxfv sqoop-$SQOOP_VERSION.bin__hadoop-2.6.0.tar.gz && \
    mv sqoop-$SQOOP_VERSION.bin__hadoop-2.6.0 sqoop && \
    rm sqoop-$SQOOP_VERSION.bin__hadoop-2.6.0.tar.gz

# Set SQOOP_HOME & Update PATH with Sqoop's bin.
ENV SQOOP_HOME=/sqoop
ENV PATH=$PATH:${SQOOP_HOME}/bin

# Rename sqoop-env-template.sh to sqoop-env.sh & append variables
RUN mv $SQOOP_HOME/conf/sqoop-env-template.sh $SQOOP_HOME/conf/sqoop-env.sh && \
    echo "export HADOOP_HOME=/opt/hadoop-3.2.2" >> $SQOOP_HOME/conf/sqoop-env.sh && \
    echo "export HADOOP_COMMON_HOME=/opt/hadoop-3.2.2" >> $SQOOP_HOME/conf/sqoop-env.sh && \
    echo "export HADOOP_MAPRED_HOME=/opt/hadoop-3.2.2" >> $SQOOP_HOME/conf/sqoop-env.sh

# Download MySQL connector & commons lang
RUN cd $SQOOP_HOME/lib && \
    curl -LO https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.21/mysql-connector-java-8.0.21.jar && \
    rm commons-lang3-3.4.jar && \
    curl -LO https://repo1.maven.org/maven2/commons-lang/commons-lang/2.6/commons-lang-2.6.jar

CMD ["/run.sh"]
