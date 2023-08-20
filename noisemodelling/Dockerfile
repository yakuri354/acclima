FROM eclipse-temurin:11

ARG VERSION="4.0.4"

RUN apt-get update
RUN apt-get install zip unzip libgeos-c1v5 libnetcdf-dev libgdal-dev -y
RUN ln -s /lib/x86_64-linux-gnu/libproj.so /lib/x86_64-linux-gnu/libproj.so.0 || ln -s /lib/aarch64-linux-gnu/libproj.so /lib/aarch64-linux-gnu/libproj.so.0

WORKDIR /root

RUN wget -q https://github.com/Universite-Gustave-Eiffel/NoiseModelling/releases/download/v${VERSION}/NoiseModelling_${VERSION}.zip
RUN unzip NoiseModelling_${VERSION}.zip
RUN mv NoiseModelling_4.0.3 NoiseModelling_${VERSION}
RUN rm NoiseModelling_${VERSION}.zip

RUN wget https://github.com/orbisgis/h2gis/releases/download/v2.2.0/h2gis-2.2.0-bin.zip -O h2gis.zip
RUN unzip h2gis.zip

# COPY NoiseModelling .

COPY h2.server.properties .h2.server.properties

WORKDIR /root/NoiseModelling_${VERSION}
# WORKDIR /root/NoiseModelling

RUN chmod +x ./bin/startup_linux_mac.sh
COPY run.sh .
RUN chmod +x run.sh

VOLUME /data
VOLUME /root/NoiseModelling_4.0.4/data_dir

EXPOSE 9580
EXPOSE 8082

CMD ["./run.sh"]
