from django.db import models

STATUS = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
)


class Country(models.Model):
    countryCode = models.CharField(max_length=120, null=True)
    countryName = models.CharField(max_length=120, null=True)
    englishName = models.CharField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.countryName
