ARG PROD_BASE=base

FROM python AS base
WORKDIR /data
COPY Makefile requirements.txt /data
RUN make -C /data build
CMD ["make", "start"]

FROM base AS build
COPY . .

FROM scratch AS artifact
COPY --from=build /data /artifact

FROM $PROD_BASE AS prod
COPY --from=artifact /artifact /data
