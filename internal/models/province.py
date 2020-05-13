from django.db import models
from internal.models.country import Country

STATUS = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
)

class Province(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    provinceCode = models.CharField(max_length=120, null=True)
    provinceName = models.CharField(max_length=120, null=True)
    latitude = models.CharField(max_length=120, null=True)
    longitude = models.CharField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.provinceName