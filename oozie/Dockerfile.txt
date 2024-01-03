# base image
FROM hadoop_base:2.7.1
# vars
ARG OOZIE_VERSION=4.2.0
ARG HADOOP_VERSION=2.7.1
ARG SQL_CONNECTOR_VERSION=5.1.49
ARG HADOOP_HOME=/opt/hadoop-${HADOOP_VERSION}
ARG MAVEN_VERSION=3.6.3
ARG OOZIE_HOME=/opt/oozie-${OOZIE_VERSION}
# copy oozie build
COPY oozie-${OOZIE_VERSION}.tar.gz /tmp/oozie-${OOZIE_VERSION}.tar.gz
COPY mysql-connector-java-5.1.49.tar.gz /tmp/mysql-connector-java-5.1.49.tar.gz
# install
RUN tar -xzvf /tmp/oozie-${OOZIE_VERSION}.tar.gz -C /opt/ && mkdir ${OOZIE_HOME}/libext 
COPY  ext-2.2.zip /tmp/
RUN  mv /tmp/ext-2.2.zip $OOZIE_HOME/libext/
RUN tar -xzf /tmp/mysql-connector-java-$SQL_CONNECTOR_VERSION.tar.gz -C /tmp/ && \
    cp /tmp/mysql-connector-java-$SQL_CONNECTOR_VERSION/mysql-connector-java-$SQL_CONNECTOR_VERSION.jar $OOZIE_HOME/libext/ && \
    cp $HADOOP_HOME/share/hadoop/common/*.jar $OOZIE_HOME/libext/ && \
    cp $HADOOP_HOME/share/hadoop/common/lib/*.jar $OOZIE_HOME/libext/ && \
    cp $HADOOP_HOME/share/hadoop/hdfs/*.jar $OOZIE_HOME/libext/ && \
    cp $HADOOP_HOME/share/hadoop/hdfs/lib/*.jar $OOZIE_HOME/libext/ && \
    cp $HADOOP_HOME/share/hadoop/mapreduce/*.jar $OOZIE_HOME/libext/ && \
    cp $HADOOP_HOME/share/hadoop/mapreduce/lib/*.jar $OOZIE_HOME/libext/ && \
    cp $HADOOP_HOME/share/hadoop/yarn/*.jar $OOZIE_HOME/libext/ && \
    cp $HADOOP_HOME/share/hadoop/yarn/lib/*.jar $OOZIE_HOME/libext/ && \
    echo "PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$OOZIE_HOME/bin:$PATH" >> ~/.bashrc && \
    rm -rf /tmp/oozie-${OOZIE_VERSION}.tar.gz mysql-connector-java-$SQL_CONNECTOR_VERSION.tar.gz mysql-connector-java-$SQL_CONNECTOR_VERSION /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Install Maven
COPY apache-maven-${MAVEN_VERSION}-bin.tar.gz /opt/
RUN cd /opt  && tar xfv apache-maven-${MAVEN_VERSION}-bin.tar.gz
RUN mkdir -p /var/log/oozie
#RUN mkdir -p /var/lib/oozie/data && chown -R hdfs /var/lib/oozie
RUN mkdir -p /var/lib/oozie/data
RUN rm ${OOZIE_HOME}/docs/pom.xml && rm ${OOZIE_HOME}/pom.xml
COPY docs/pom.xml ${OOZIE_HOME}/docs 
COPY main/pom.xml ${OOZIE_HOME}/
RUN export M2_HOME=/opt/apache-maven-${MAVEN_VERSION} && export PATH=/opt/apache-maven-${MAVEN_VERSION}/bin:$PATH \
 && ${OOZIE_HOME}/bin/mkdistro.sh -DskipTests -P hadoop-2 -Dhadoopversion=2.7.1  -DjavaVersion=1.8 -DtargetJavaVersion=1.8 -Dmaven.javadoc.skip=true -e 
RUN mkdir /usr/local/oozie && mv  $OOZIE_HOME/distro/target/oozie-${OOZIE_VERSION}-distro/oozie-${OOZIE_VERSION} /usr/local/oozie && export OOZIE_HOME=/usr/local/oozie/oozie-4.2.0 
ENV OOZIE_DIST_HOME=/usr/local/oozie/oozie-${OOZIE_VERSION}
RUN apt-get update && apt-get install -y gnupg2
RUN  apt-get -y update &&  apt-get install -y unzip zip --force-yes
RUN mv $OOZIE_HOME/libext ${OOZIE_DIST_HOME}/libext
RUN ln -s /var/log/oozie ${OOZIE_DIST_HOME}/log
RUN ln -s /var/lib/oozie/data ${OOZIE_DIST_HOME}/data
RUN rm ${OOZIE_DIST_HOME}/conf/oozie-site.xml
COPY oozie-site.xml ${OOZIE_DIST_HOME}/conf/
RUN ${OOZIE_DIST_HOME}/bin/oozie-setup.sh prepare-war
WORKDIR ${OOZIE_DIST_HOME}
RUN export PATH=$OOZIE_DIST_HOME/bin:$PATH
CMD [ "./bin/oozied.sh","run" ]