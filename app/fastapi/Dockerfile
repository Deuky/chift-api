FROM python
RUN apt-get update && apt-get install -y make
WORKDIR /data
COPY Makefile requirements.txt /data
RUN make -C /data build
CMD ["make", "start"]