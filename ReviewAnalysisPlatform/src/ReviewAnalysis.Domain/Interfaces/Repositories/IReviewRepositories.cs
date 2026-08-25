using ReviewAnalysis.Domain.Entities;

namespace ReviewAnalysis.Domain.Interfaces.Repositories;

public interface IReviewRepository
{
    Task<List<Review>> GetAllAsync();

    Task<Review?> GetByIdAsync(int id);

    Task<Review> AddAsync(Review review);

    Task UpdateAsync(Review review);

    Task DeleteAsync(Review review);
}