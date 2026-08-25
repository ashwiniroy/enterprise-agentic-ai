using ReviewAnalysis.Application.DTOs.AnalyzdeReviewRequest;
using ReviewAnalysis.Application.DTOs.AnalyzdeReviewResponse;
public interface IAIService
{
    Task<ReviewAnalysisResponseDto> AnalyzeReviewAsync(
        AnalyzeReviewRequestDto request);
}