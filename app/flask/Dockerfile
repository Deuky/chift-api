ARG BASE_REF=base

FROM python AS base
WORKDIR /data
COPY Makefile requirements.txt /data
RUN make -C /data build
CMD ["make", "start"]


FROM scratch AS artifact
COPY . /artifact

	
FROM ${BASE_REF} AS unit
COPY --from=artifact /artifact /data
