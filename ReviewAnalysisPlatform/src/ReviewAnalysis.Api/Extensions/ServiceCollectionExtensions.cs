using Microsoft.Extensions.DependencyInjection;

using ReviewAnalysis.Application.Services;
using ReviewAnalysis.Application.Interfaces;

namespace ReviewAnalysis.Application.Extensions;

public static class ServiceCollectionExtensions
{
    public static IServiceCollection AddApplication(this IServiceCollection services)
    {
        services.AddScoped<IReviewService, ReviewService>();

        return services;
    }
}