build:
	dotnet build .NET.sln -c Release

install: 
	dotnet publish ./data.csproj -c Release -o $(TARGET)

start:
	dotnet publish/data.dll

start-dev:
	dotnet run --launch-profile http