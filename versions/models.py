from django.db import models

class MobileVersion(models.Model):
    version = models.CharField(max_length=20, unique=True)
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.version
