from django.db import models

STATUS = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
)


class PlaceType(models.Model):
    placeTypeCode = models.CharField(max_length=120)
    placeTypeName = models.CharField(max_length=120)
    finishedGoodProductAccountCode = models.CharField(max_length=120)
    rawMaterialAccountCode = models.CharField(max_length=120)
    explanation = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.placeTypeName
