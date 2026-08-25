using ReviewAnalysis.Domain.Common;
namespace ReviewAnalysis.Domain.Entities;

public class Review :BaseEntity
{
    public int Id { get; set; }

    public string CustomerName { get; set; } = string.Empty;

    public string Email { get; set; } = string.Empty;

    public string Product { get; set; } = string.Empty;

    public string Category { get; set; } = string.Empty;

    public DateOnly PurchaseDate { get; set; }

    public int Rating { get; set; }

    public string ReviewTitle { get; set; } = string.Empty;

    public string ReviewDescription { get; set; } = string.Empty;

    public bool Recommend { get; set; }

    public string Sentiment { get; set; } = "Pending";

    public string Status { get; set; } = "Active";

    public DateTime CreatedDate { get; set; } = DateTime.UtcNow;

    public DateTime? UpdatedDate { get; set; }
}