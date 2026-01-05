FROM python AS base
WORKDIR /data
COPY Makefile requirements.txt /data
RUN make -C /data build
CMD ["make", "start"]

FROM base AS build

FROM scratch AS artifact
COPY . /artifact

FROM base AS unit
COPY --from=artifact /artifact /data
