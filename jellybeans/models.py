from django.db import models

# Model echoing what is stored in PostgreSQL database
class JellybeanFlavor(models.Model):
    flavor = models.CharField(max_length=30)
    s3_image = models.FileField(upload_to="", null=True, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.flavor
