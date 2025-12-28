from django.db import models

class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    external_id = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = "contact"
