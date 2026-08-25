namespace ReviewAnalysis.Application.DTOs.Reviews;

public class UpdateReviewRequestDto
{
    public string CustomerName { get; set; } = string.Empty;

    public string Email { get; set; } = string.Empty;

    public string Product { get; set; } = string.Empty;

    public string Category { get; set; } = string.Empty;

    public DateOnly PurchaseDate { get; set; }

    public int Rating { get; set; }

    public string ReviewTitle { get; set; } = string.Empty;

    public string ? ReviewDescription { get; set; }

    public bool Recommend { get; set; }
}