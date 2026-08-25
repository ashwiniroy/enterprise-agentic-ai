using System.Text.Json.Serialization;

namespace ReviewAnalysis.Application.DTOs.AnalyzdeReviewRequest;

public class AnalyzeReviewRequestDto
{
    [JsonPropertyName("review_id")]
    public int ReviewId { get; set; }

    [JsonPropertyName("customer")]
    public string Customer { get; set; } = string.Empty;

    [JsonPropertyName("product")]
    public string Product { get; set; } = string.Empty;

    [JsonPropertyName("rating")]
    public int Rating { get; set; }

    [JsonPropertyName("review")]
    public string Review { get; set; } = string.Empty;
}