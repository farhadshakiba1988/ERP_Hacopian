from django.db import models
from internal.models.jobGroup import JobGroup
from internal.models.placeType import PlaceType
from internal.models.post import Post

STATUS = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
)

GENDER_TYPES = (
    ('F', 'Female'),
    ('M', 'Male'),
)


class Job(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    placeType = models.ForeignKey(PlaceType, on_delete=models.CASCADE)
    jobGroup = models.ForeignKey(JobGroup, on_delete=models.CASCADE)
    code = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=120, null=True)
    yearOfExperience = models.CharField(max_length=120, null=True)
    educationalSubstitution = models.BooleanField(default=False)
    sexuality = models.CharField(choices=GENDER_TYPES, max_length=20)
    fromAge = models.SmallIntegerField(null=True)
    toAge = models.SmallIntegerField(null=True)
    internship = models.BooleanField(default=False)
    vision = models.CharField(max_length=120, null=True)
    mbti = models.CharField(max_length=120, null=True)
    revisionDate = models.CharField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
