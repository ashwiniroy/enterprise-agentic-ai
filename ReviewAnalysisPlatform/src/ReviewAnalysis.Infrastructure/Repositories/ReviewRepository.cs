using Microsoft.EntityFrameworkCore;
using ReviewAnalysis.Domain.Entities;
using ReviewAnalysis.Domain.Interfaces.Repositories;
using ReviewAnalysis.Infrastructure.Data;

namespace ReviewAnalysis.Infrastructure.Repositories;

public class ReviewRepository : IReviewRepository
{
    private readonly ApplicationDbContext _context;

    public ReviewRepository(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task<List<Review>> GetAllAsync()
    {
        return await _context.Reviews
            .Where(x => !x.IsDeleted)
            .OrderByDescending(x => x.CreatedDate)
            .ToListAsync();
    }

    public async Task<Review?> GetByIdAsync(int id)
    {
        return await _context.Reviews
            .FirstOrDefaultAsync(x => x.Id == id && !x.IsDeleted);
    }

    public async Task<Review> AddAsync(Review review)
    {
        await _context.Reviews.AddAsync(review);

        await _context.SaveChangesAsync();

        return review;
    }

    public async Task UpdateAsync(Review review)
    {
        _context.Reviews.Update(review);

        await _context.SaveChangesAsync();
    }

    public async Task DeleteAsync(Review review)
    {
        review.IsDeleted = true;
        review.UpdatedDate = DateTime.UtcNow;

        _context.Reviews.Update(review);

        await _context.SaveChangesAsync();
    }
}