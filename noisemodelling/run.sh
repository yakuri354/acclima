#!/bin/bash

./bin/startup_linux_mac.sh &
java -jar /root/h2gis-standalone/h2gis-dist-*.jar &

wait -n

exit $?
