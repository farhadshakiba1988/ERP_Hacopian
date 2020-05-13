from django.db import models

from internal.models.province import Province

STATUS = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
)


class City(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    cityCode = models.CharField(max_length=120, null=True)
    cityName = models.CharField(max_length=120, null=True)
    latitude = models.CharField(max_length=120, null=True)
    longitude = models.CharField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.cityName
