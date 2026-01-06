FROM python AS base
WORKDIR /data
COPY Makefile requirements.txt /data
RUN make -C /data build
COPY . /data
CMD ["make", "start"]
