FROM python AS base
ENV TZ=Europe/Brussels
WORKDIR /data

RUN apt-get update && apt-get install -y cron
COPY requirements.txt Makefile .
RUN make -C /data build
COPY --exclude=Dockerfile --exclude=requirements.txt --exclude=Makefile . .
RUN make -C /data install
CMD ["/entrypoint.sh"]
