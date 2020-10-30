from django.db import models

# Create your models here.


class Images(models.Model):
    # caption = models.CharField(max_length=80)
    image = models.ImageField(upload_to='../upload_test')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
