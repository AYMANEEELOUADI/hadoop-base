FROM ubuntu:latest

ENV CASSANDRA_VERSION  4.0.7
ENV CASSANDRA_PACKAGE apache-cassandra-$CASSANDRA_VERSION-bin.tar.gz

RUN apt-get -y update && apt-get -y install dos2unix

COPY ./assets/${CASSANDRA_PACKAGE} /tmp/

RUN wget -q -O - https://www.apache.org/dist/cassandra/KEYS && tee /etc/apt/trusted.gpg.d/cassandra.asc

RUN mkdir /root/apache-cassandra && tar -xvf /tmp/${CASSANDRA_PACKAGE} -C /root/apache-cassandra --strip-components=1



ADD bin/install-cassandra /usr/bin/install-cassandra
RUN dos2unix /usr/bin/install-cassandra
RUN /usr/bin/install-cassandra

# Install start scripts and hosts file
ADD bin/pipework /usr/bin/
RUN dos2unix /usr/bin/pipework

ADD bin/start-cassandra /usr/bin/
RUN dos2unix /usr/bin/start-cassandra

ADD bin/run-command /usr/bin/
RUN dos2unix /usr/bin/run-command

# Configure host names
ADD etc/cassandra.hosts /etc/dnsmasq.d/0hosts
ADD etc/dnsmasq.conf /etc/dnsmasq.conf
ADD etc/resolv.conf /etc/resolv.dnsmasq.conf

EXPOSE 9160 9042 