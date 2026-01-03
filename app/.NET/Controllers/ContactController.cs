using data.Services;
using Microsoft.AspNetCore.Mvc;

namespace data.Controllers;

[ApiController]
public class ContactController : ControllerBase
{
    private readonly ILogger<ContactController> _logger;
    private readonly IContactService _contactService;

    public ContactController(
        ILogger<ContactController> logger,
        IContactService contactService
    )
    {
        _logger = logger;
        _contactService = contactService;
    }

    [HttpGet("contact/external_id/{externalId}", Name = "GetContactByExternalId")]
    public async Task<IActionResult> GetExternalById(int externalId)
    {
        return Ok(await _contactService.GetByExternalIdAsync(externalId));
    }

    [HttpGet("contact/{id}", Name = "GetContact")]
    public async Task<IActionResult> GetById(int id)
    {
        return Ok(await _contactService.GetByIdAsync(id));
    }
    
    [HttpGet("contacts", Name = "GetContacts")]
    public async Task<IActionResult> GetAll()
    {
        return Ok(await _contactService.GetAllAsync());
    }
}
