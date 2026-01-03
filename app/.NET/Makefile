build:
	dotnet build .NET.sln -c Release

install: 
	dotnet publish ./data.csproj -c Release -o $(TARGET)

start:
	dotnet run --launch-profile http