from django.db import models

# Create your models here.


class Images(models.Model):
    caption = models.CharField(max_length=200, default="")
    # image = models.ImageField(upload_to='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
