using System.Text.Json.Serialization;

namespace ReviewAnalysis.Application.DTOs.AnalyzdeReviewResponse;

public class ReviewAnalysisResponseDto
{
    [JsonPropertyName("sentiment")]
    public string Sentiment { get; set; } = string.Empty;

    [JsonPropertyName("confidence")]
    public double Confidence { get; set; }

    [JsonPropertyName("summary")]
    public string Summary { get; set; } = string.Empty;

    [JsonPropertyName("embeddings")]
    public List<double> Embeddings { get; set; } = new();

    [JsonPropertyName("keywords")]
    public List<string> Keywords { get; set; } = new();

    [JsonPropertyName("entities")]
    public List<string> Entities { get; set; } = new();
}