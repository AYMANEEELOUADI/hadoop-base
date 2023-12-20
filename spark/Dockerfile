FROM hadoop_base:1
ENV SPARK_VERSION 3.1.2
ENV SPARK_PACKAGE spark-${SPARK_VERSION}-bin-without-hadoop
ENV SPARK_HOME /usr/spark-${SPARK_VERSION}
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"
ENV PATH $PATH:${SPARK_HOME}/bin
COPY /assets/${SPARK_PACKAGE}.tgz /tmp/
RUN tar -xvf /tmp/${SPARK_PACKAGE}.tgz -C /usr/ && mv /usr/${SPARK_PACKAGE} ${SPARK_HOME}
ENV SCALA_VERSION 2.12.12
ENV SCALA_PACKAGE scala-${SCALA_VERSION}
ENV SCALA_HOME /usr/scala/scala-${SCALA_VERSION}
COPY /assets/${SCALA_PACKAGE}.tgz /tmp/
RUN tar -xvf /tmp/${SCALA_PACKAGE}.tgz -C /usr/
RUN mkdir /usr/scala && mv /usr/${SCALA_PACKAGE} ${SCALA_HOME}
RUN chmod -R 777 ${SCALA_HOME}
ENV PATH $PATH:${SCALA_HOME}/bin
RUN echo ${PATH}

RUN rm $HADOOP_HOME/etc/hadoop/core-site.xml
COPY conf/core-site.xml $HADOOP_HOME/etc/hadoop/

WORKDIR $SPARK_HOME

CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]
#cd $HIVE_HOME/bin
#./hiveserver2 --hiveconf hive.server2.enable.doAs=false