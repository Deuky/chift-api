FROM python
ENV TZ=Europe/Brussels
RUN apt-get update && apt-get install -y cron pip make
WORKDIR /data
COPY requirements.txt Makefile .
RUN make build
COPY entrypoint.sh /
CMD ["/entrypoint.sh"]