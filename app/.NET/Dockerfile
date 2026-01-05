FROM mcr.microsoft.com/dotnet/sdk:9.0 AS base
WORKDIR /data

FROM base AS build
RUN apt-get update && apt-get install -y make
COPY . .
RUN make build
RUN make install TARGET=/data/publish
CMD ["make", "start"]

FROM scratch AS artifact
COPY --from=build /data/publish /artifact

FROM base AS prod
COPY --from=artifact /artifact /data
CMD ["dotnet", "data.dll"]