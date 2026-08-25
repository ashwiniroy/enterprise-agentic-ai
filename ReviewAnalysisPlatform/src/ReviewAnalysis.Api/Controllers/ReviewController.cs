using Microsoft.AspNetCore.Mvc;
using ReviewAnalysis.Application.DTOs.Reviews;
using ReviewAnalysis.Application.Interfaces;

namespace ReviewAnalysis.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ReviewsController : ControllerBase
{
    private readonly IReviewService _service;

    public ReviewsController(IReviewService service)
    {
        _service = service;
    }

    [HttpGet]
    public async Task<IActionResult> GetAll()
    {
        return Ok(await _service.GetAllAsync());
    }

    [HttpGet("{id}")]
    public async Task<IActionResult> Get(int id)
    {
        var review = await _service.GetByIdAsync(id);

        if (review == null)
            return NotFound();

        return Ok(review);
    }

    [HttpPost]
    public async Task<IActionResult> Create(CreateReviewRequestDto dto)
    {
        var review = await _service.CreateAsync(dto);

        return CreatedAtAction(nameof(Get), new { id = review.Id }, review);
    }

    [HttpPut("{id}")]
    public async Task<IActionResult> Update(
        int id,
        UpdateReviewRequestDto dto)
    {
        await _service.UpdateAsync(id, dto);

        return NoContent();
    }

    [HttpDelete("{id}")]
    public async Task<IActionResult> Delete(int id)
    {
        await _service.DeleteAsync(id);

        return NoContent();
    }
}