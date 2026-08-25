using ReviewAnalysis.Application.DTOs.Reviews;
using ReviewAnalysis.Domain.Entities;
using ReviewAnalysis.Application.Services;
using ReviewAnalysis.Domain.Interfaces.Repositories;
using ReviewAnalysis.Application.Interfaces;
using ReviewAnalysis.Application.DTOs.AnalyzdeReviewResponse;
using ReviewAnalysis.Application.DTOs.AnalyzdeReviewRequest;


namespace ReviewAnalysis.Application.Services;

public class ReviewService : IReviewService
{
    private readonly IReviewRepository _repository;
    private readonly IAIService _aiService;

    public ReviewService(
    IReviewRepository repository,
    IAIService aiService)
{
    _repository = repository;
    _aiService = aiService;
}

    public async Task<List<ReviewResponseDto>> GetAllAsync()
    {
        var reviews = await _repository.GetAllAsync();

        return reviews.Select(MapToDto).ToList();
    }

    public async Task<ReviewResponseDto?> GetByIdAsync(int id)
    {
        var review = await _repository.GetByIdAsync(id);

        if (review == null)
            return null;

        return MapToDto(review);
    }

    public async Task<ReviewResponseDto> CreateAsync(CreateReviewRequestDto dto)
    {
        var entity = new Review
        {
            CustomerName = dto.CustomerName,
            Email = dto.Email,
            Product = dto.Product,
            Category = dto.Category,
            PurchaseDate = dto.PurchaseDate,
            Rating = dto.Rating,
            ReviewTitle = dto.ReviewTitle,
            ReviewDescription = dto.ReviewDescription,
            Recommend = dto.Recommend,
            // Sentiment = "Pending",
            Status = "Active"
        };

        entity = await _repository.AddAsync(entity);

var analysis = await _aiService.AnalyzeReviewAsync(
    new AnalyzeReviewRequestDto
    {
        ReviewId = entity.Id,
        Customer = entity.CustomerName,
        Product = entity.Product,
        Rating = entity.Rating,
        Review = entity.ReviewDescription
    });

// Update sentiment
entity.Sentiment = string.IsNullOrWhiteSpace(analysis.Sentiment)
    ? "Pending"
    : analysis.Sentiment;

await _repository.UpdateAsync(entity);

        return MapToDto(entity);
    }

    public async Task UpdateAsync(int id, UpdateReviewRequestDto dto)
    {
        var review = await _repository.GetByIdAsync(id);

        if (review == null)
            throw new Exception("Review not found.");

        review.CustomerName = dto.CustomerName;
        review.Email = dto.Email;
        review.Product = dto.Product;
        review.Category = dto.Category;
        review.PurchaseDate = dto.PurchaseDate;
        review.Rating = dto.Rating;
        review.ReviewTitle = dto.ReviewTitle;
        review.ReviewDescription = dto.ReviewDescription;
        review.Recommend = dto.Recommend;
        review.UpdatedDate = DateTime.UtcNow;

        await _repository.UpdateAsync(review);
    }

    public async Task DeleteAsync(int id)
    {
        var review = await _repository.GetByIdAsync(id);

        if (review == null)
            throw new Exception("Review not found.");

        await _repository.DeleteAsync(review);
    }

    private static ReviewResponseDto MapToDto(Review review)
    {
        return new ReviewResponseDto
        {
            Id = review.Id,
            CustomerName = review.CustomerName,
            Email = review.Email,
            Product = review.Product,
            Category = review.Category,
            Rating = review.Rating,
            ReviewTitle = review.ReviewTitle,
            ReviewDescription = review.ReviewDescription,
            Recommend = review.Recommend,
            Sentiment = review.Sentiment,
            Status = review.Status,
            CreatedDate = review.CreatedDate
        };
    }
}