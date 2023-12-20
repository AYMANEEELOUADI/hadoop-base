FROM hadoop_base:1
# !! IMPORTANT
# make sure hadoop_base:1 is the name of the image you built.
HEALTHCHECK CMD curl -f http://localhost:50070/ || exit 1
# Create directories for namenode storage
# specify multiple files if you want to create multiple storage files for redundancy
RUN mkdir /opt/hdfs
RUN mkdir /opt/hdfs/namenode

# ***ADD CONFIG FILES***
ADD ./config-files/hdfs-site.xml $HADOOP_HOME/etc/hadoop/
RUN rm $HADOOP_HOME/etc/hadoop/core-site.xml
COPY /config-files/core-site.xml $HADOOP_HOME/etc/hadoop/

# necessary before running namenode
RUN hdfs namenode -format

# Web
EXPOSE 50070
# Default
EXPOSE 8020

CMD hdfs namenode