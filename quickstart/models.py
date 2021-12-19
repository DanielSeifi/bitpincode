from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Documents(models.Model):
    title = models.CharField(verbose_name="عنوان مطلب", max_length=200, )
    text = models.TextField(verbose_name="متن مطلب", null=True, blank=True, )

    def __str__(self):
        return self.title


class RateDocuments(models.Model):
    document = models.ForeignKey(to=Documents, on_delete=models.CASCADE, )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, )
    rate = models.PositiveIntegerField(verbose_name="امتیاز", null=True, )

    def __str__(self):
        return self.document.title
