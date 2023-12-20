FROM couchdb:latest

# Install and configure Ruby and Ruby Version Manager (RVM)
RUN mkdir ~/.gnupg
RUN echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf
COPY mpapis.asc /tmp/mpapis.asc 
COPY pkuczynski.asc /tmp/pkuczynski.asc 
RUN gpg --import /tmp/mpapis.asc && rm /tmp/mpapis.asc
RUN gpg --import /tmp/pkuczynski.asc && rm /tmp/pkuczynski.asc
RUN \curl -sSL https://get.rvm.io | bash -s stable
RUN sed -i -e 's/mesg n .*true/tty -s \&\& mesg n/g' /root/.profile


COPY script.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/script.sh

# Add examples and lectures
ADD ./examples /app/couchdb/examples
ADD ./lectures /app/couchdb/lectures

# Copy custom config file
COPY local.ini /opt/couchdb/etc/
