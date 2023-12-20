#!/bin/bash

#Automatical stats one namenode and 3 datanodes in a docker network

#namenode
docker run -d --net dock_net --hostname namenode-master -p 9870:9870 -p 50070:50070 -p 8020:8020 --name namenode namenode:1.2

#datanode 1
docker run -d --net dock_net -p 50075:50075 --name datanode1 datanode:1.2

#datanode 2
docker run -d --net dock_net --name datanade2 datanode:latest

#resourcemanager
docker run -d --net dock_net --name resourcemanager -p 8088:8088 resourcemanager:latest

#historyserver
docker run -d --net dock_net --name historyserver -p 8188:8188 historyserver:latest