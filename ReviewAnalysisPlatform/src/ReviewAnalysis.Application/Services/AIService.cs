using System.Net.Http.Json;
using ReviewAnalysis.Application.DTOs.AnalyzdeReviewRequest;
using ReviewAnalysis.Application.DTOs.AnalyzdeReviewResponse;
using ReviewAnalysis.Application.Interfaces;

namespace ReviewAnalysis.Application.Services;

public class AIService : IAIService
{
    private readonly HttpClient _httpClient;

    public AIService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<ReviewAnalysisResponseDto> AnalyzeReviewAsync(
        AnalyzeReviewRequestDto request)
    {
        var response = await _httpClient.PostAsJsonAsync(
            "/api/analyze-review",
            request);

        var rawResponse = await response.Content.ReadAsStringAsync();

        Console.WriteLine($"FastAPI response: {rawResponse}");

        response.EnsureSuccessStatusCode();

        var result = await response.Content
            .ReadFromJsonAsync<ReviewAnalysisResponseDto>();

        return result
            ?? throw new InvalidOperationException(
                "FastAPI returned an empty response.");
    }
}