using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using data.Contexts;

namespace data.Services;

public class ContactService : IContactService
{
        private readonly AppDbContext _context;

        public ContactService(AppDbContext context)
        {
            _context = context;
        }

        public async Task<Contact?> GetByIdAsync(int id)
        {
            return await _context.Contacts.FindAsync(id);
        }

        public async Task<Contact?> GetByExternalIdAsync(int id)
        {
            return await _context.Contacts.Where(
                x => x.ExternalId == id).FirstOrDefaultAsync();
        }

        public async Task<List<Contact>> GetAllAsync()
        {
            return await _context.Contacts.ToListAsync();
        }
}