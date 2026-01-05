FROM python AS base
WORKDIR /data
RUN apt-get update && apt-get install -y make
COPY Makefile requirements.txt /data
RUN make -C /data build
CMD ["make", "start"]


FROM base AS build
COPY . .


FROM scratch AS artifact
COPY --from=build /data /artifact


FROM base AS prod
COPY --from=artifact /artifact /data
