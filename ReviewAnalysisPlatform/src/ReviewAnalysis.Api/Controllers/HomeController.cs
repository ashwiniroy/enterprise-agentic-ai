using Microsoft.AspNetCore.Mvc;

namespace ReviewAnalysis.API.Controllers;

[ApiController]
[Route("api/[controller]")]
public class HomeController : ControllerBase
{
    [HttpGet]
    public IActionResult Get()
    {
        return Ok(new
        {
            Message = "Review Analysis API is running successfully!"
        });
    }
}