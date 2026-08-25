using Microsoft.EntityFrameworkCore;
using ReviewAnalysis.Infrastructure.Data;
using ReviewAnalysis.Infrastructure.Extensions;
using ReviewAnalysis.Application.Interfaces;
using ReviewAnalysis.Application.Services;
using ReviewAnalysis.Infrastructure.Repositories;
using ReviewAnalysis.Domain.Interfaces.Repositories;


var builder = WebApplication.CreateBuilder(args);

// Add services
builder.Services.AddControllers();

//db
builder.Services.AddInfrastructure(builder.Configuration);

builder.Services.AddScoped<IReviewService, ReviewService>();
builder.Services.AddScoped<IReviewRepository, ReviewRepository>();


builder.Services.AddCors(options =>
{
    options.AddPolicy("Frontend", policy =>
    {
        policy
            .WithOrigins("http://localhost:3000")
            .AllowAnyHeader()
            .AllowAnyMethod()
            .AllowCredentials();
    });
});

builder.Services.AddHttpClient<IAIService, AIService>(client =>
{
    client.BaseAddress = new Uri("http://127.0.0.1:8000");
});
// OpenAPI
builder.Services.AddOpenApi();

// Swagger
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure middleware
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();

    app.UseSwagger();
    app.UseSwaggerUI(options =>
    {
        options.SwaggerEndpoint("/swagger/v1/swagger.json", "Review Analysis API v1");
        options.RoutePrefix = "swagger";
    });
}
app.UseCors("Frontend");
app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();