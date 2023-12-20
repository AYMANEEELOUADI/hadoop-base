#!/bin/bash

# Sleep for 20 seconds
sleep 20

# Run the delayed script inside the container
docker exec nosql-couchdb /usr/local/bin/script.sh