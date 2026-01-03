using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace data;

[Table("contact")]
public class Contact
{
    [Key]
    public int Id { get; set; }

    [Column("external_id")]
    public int ExternalId { get; set; }

    public string? Name { get; set; }

    public string? Email { get; set; }
}
