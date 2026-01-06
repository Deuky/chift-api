FROM mcr.microsoft.com/dotnet/sdk:9.0 AS base
WORKDIR /data
RUN apt-get update && apt-get install -y make
COPY . /data
RUN make build
RUN make install TARGET=/data/publish
CMD ["make", "start"]
