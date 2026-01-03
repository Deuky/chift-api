using data.Services;
using data.Contexts;
using data.Converters;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

var DbDSN = builder.Configuration["DATABASE_DSN"];
var DbPasswordFile = builder.Configuration["DATABASE_PASSWORD_FILE"];

if (DbDSN == null || DbPasswordFile == null)
{
    System.Environment.Exit(1);
}

var DbPassword = File.ReadAllText(DbPasswordFile).Trim();

builder.Services.AddControllers();
// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
builder.Services.AddOpenApi();
builder.Services.AddScoped<IContactService, ContactService>();
var connectionString = ConnectionStringConverter.FromUri(DbDSN, DbPassword);

builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseMySql(
        connectionString,
        ServerVersion.AutoDetect(connectionString)
    )
);


var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

// app.UseHttpsRedirection();

// app.UseAuthorization();

app.MapControllers();

app.Run();
