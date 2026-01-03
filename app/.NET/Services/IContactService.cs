using Microsoft.AspNetCore.Mvc;

namespace data.Services;

public interface IContactService
{
    Task<List<Contact>> GetAllAsync();

    Task<Contact?> GetByIdAsync(int id);

    Task<Contact?> GetByExternalIdAsync(int externalId);
}