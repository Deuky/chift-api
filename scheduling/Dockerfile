FROM python AS base
ENV TZ=Europe/Brussels
WORKDIR /data

RUN apt-get update && apt-get install -y cron
COPY requirements.txt Makefile .
RUN make -C /data build
COPY . .
RUN make -C /data install
COPY entrypoint.sh /
CMD ["/entrypoint.sh"]
