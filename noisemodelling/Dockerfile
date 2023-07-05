FROM eclipse-temurin:11

ARG VERSION="4.0.4"

RUN apt update
RUN apt install zip unzip

WORKDIR /root

RUN wget -q https://github.com/Universite-Gustave-Eiffel/NoiseModelling/releases/download/v${VERSION}/NoiseModelling_${VERSION}.zip
RUN unzip NoiseModelling_${VERSION}.zip
RUN mv NoiseModelling_4.0.3 NoiseModelling_${VERSION}
RUN rm NoiseModelling_${VERSION}.zip

WORKDIR /root/NoiseModelling_${VERSION}

RUN chmod +x ./bin/startup_linux_mac.sh

VOLUME /data
EXPOSE 9580

CMD ["./bin/startup_linux_mac.sh"]
