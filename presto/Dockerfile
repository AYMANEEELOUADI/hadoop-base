FROM openjdk:8

ENV PRESTO_VERSION=0.181
ENV PRESTO_HOME=/opt/presto

# extra dependency for running launcher
RUN apt-get update 
RUN apt-get install -y --no-install-recommends \
    python2.7-minimal --fix-missing \
    && rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/python2.7 /usr/bin/python

COPY /assets/presto-server-${PRESTO_VERSION}.tar.gz /tmp/
WORKDIR /opt
RUN mkdir ${PRESTO_HOME} && tar -xzf /tmp/presto-server-${PRESTO_VERSION}.tar.gz -C ${PRESTO_HOME} --strip-components=1 && \
    mkdir -p ${PRESTO_HOME}/data && \
    rm -f /tmp/presto-server-${PRESTO_VERSION}.tar.gz

#COPY launcher ${PRESTO_HOME}/bin

WORKDIR ${PRESTO_HOME}

ENTRYPOINT ["./bin/launcher"]

CMD ["run"]

