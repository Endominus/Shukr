from django.db import models

# Create your models here.
class Thanks(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'thanks'

    def __str__(self):
        return self.text