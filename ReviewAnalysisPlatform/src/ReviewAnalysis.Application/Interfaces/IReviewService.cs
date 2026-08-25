using ReviewAnalysis.Application.DTOs.Reviews;
using ReviewAnalysis.Domain.Entities;
namespace ReviewAnalysis.Application.Interfaces;

public interface IReviewService
{
    Task<List<ReviewResponseDto>> GetAllAsync();

    Task<ReviewResponseDto?> GetByIdAsync(int id);

    Task<ReviewResponseDto> CreateAsync(CreateReviewRequestDto dto);

    Task UpdateAsync(int id, UpdateReviewRequestDto dto);

    Task DeleteAsync(int id);
}