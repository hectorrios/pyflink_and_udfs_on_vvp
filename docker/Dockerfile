FROM eu.gcr.io/vvp-stable/v2.8/flink:1.15.2-stream3-scala_2.12-java11

USER root:root
RUN apt update \
    && apt -y install python3.8 python3-pip \
    && python3.8 -m pip install apache-flink==1.15.2 \
    && apt clean \
    && ln -s /usr/bin/python3.8 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

USER 999:999

