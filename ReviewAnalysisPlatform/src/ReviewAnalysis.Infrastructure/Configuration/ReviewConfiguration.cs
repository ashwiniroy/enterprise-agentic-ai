using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using ReviewAnalysis.Domain.Entities;

namespace ReviewAnalysis.Infrastructure.Configurations;

public class ReviewConfiguration : IEntityTypeConfiguration<Review>
{
    public void Configure(EntityTypeBuilder<Review> builder)
    {
        builder.ToTable("Reviews");

        builder.HasKey(r => r.Id);

        builder.Property(r => r.CustomerName)
               .HasMaxLength(100)
               .IsRequired();

        builder.Property(r => r.Email)
               .HasMaxLength(150)
               .IsRequired();

        builder.Property(r => r.Product)
               .HasMaxLength(100)
               .IsRequired();

        builder.Property(r => r.Category)
               .HasMaxLength(100);

        builder.Property(r => r.ReviewTitle)
               .HasMaxLength(200);

        builder.Property(r => r.Sentiment)
               .HasMaxLength(30);

        builder.Property(r => r.Status)
               .HasMaxLength(30);
    }
}