from django.db import models

STATUS = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
)

class Post(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    explanation = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code