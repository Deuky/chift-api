using System;

namespace data.Converters;

public static class ConnectionStringConverter
{
    public static string FromUri(string uri, string password)
    {
        var parsedUri = new Uri(uri);

        var userInfo = parsedUri.UserInfo.Split(':', 2);
        var user = userInfo[0];

        var server = parsedUri.Host;
        var port = parsedUri.Port > 0 ? parsedUri.Port : 3306;
        var database = parsedUri.AbsolutePath.TrimStart('/');

        return $"Server={server};Port={port};Database={database};User={user};Password={password}";
    }
}