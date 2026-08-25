namespace ReviewAnalysis.Application.DTOs.Reviews;

public class ReviewResponseDto
{
    public int Id { get; set; }

    public string CustomerName { get; set; }

    public string Email { get; set; }

    public string Product { get; set; }

    public string Category { get; set; }

    public int Rating { get; set; }

    public string ReviewTitle { get; set; }

    public string ReviewDescription { get; set; }

    public bool Recommend { get; set; }

    public string Sentiment { get; set; }

    public string Status { get; set; }

    public DateTime CreatedDate { get; set; }
}