from django.db import models

STATUS = (
    ('Active', 'Active'),
    ('InActive', 'InActive'),
)
GENDER_TYPES = (
    ('F', 'Female'),
    ('M', 'Male'),
)

STATUS_TYPES = (
    ('Enabled', 'Enabled'),
    ('Disabled', 'Disabled'),
)


class PersonType(models.Model):
    type = models.IntegerField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)


class Country(models.Model):
    countryCode = models.CharField(max_length=120, null=True)
    countryName = models.CharField(max_length=120, null=True)
    englishName = models.CharField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)


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


class MarriageStatus(models.Model):
    code = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)


class MilitaryService(models.Model):
    code = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)


class Religion(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    explanation = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)


class Post(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    explanation = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)


class PlaceType(models.Model):
    placeTypeCode = models.CharField(max_length=120)
    placeTypeName = models.CharField(max_length=120)
    finishedGoodProductAccountCode = models.CharField(max_length=120)
    rawMaterialAccountCode = models.CharField(max_length=120)
    explanation = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)


class JobGroup(models.Model):
    code = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    explanation = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)


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


class Person(models.Model):
    personType = models.ForeignKey(PersonType, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    marriageStatus = models.ForeignKey(MarriageStatus, on_delete=models.CASCADE)
    militaryService = models.ForeignKey(MilitaryService, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    fileNumber = models.CharField(max_length=120, null=True)
    cardNumber = models.CharField(max_length=120, null=True)
    code = models.CharField(max_length=120, null=True)
    firstName = models.CharField(max_length=120, null=True)
    lastName = models.CharField(max_length=120, null=True)
    fatherName = models.CharField(max_length=120, null=True)
    nationalCode = models.CharField(max_length=120, null=True)
    birthCertificateNumber = models.CharField(max_length=120, null=True)
    issueDate = models.CharField(max_length=120, null=True)
    birthDate = models.CharField(max_length=120, null=True)
    deathDate = models.CharField(max_length=120, null=True)
    marriageDate = models.CharField(max_length=120, null=True)
    sex = models.CharField(choices=GENDER_TYPES, max_length=20)
    email = models.CharField(max_length=120, null=True)
    getEmail = models.BooleanField(default=False)
    getSMS = models.BooleanField(default=False)
    nfc = models.CharField(max_length=120, null=True)
    password = models.CharField(max_length=120, null=True)
    explanation = models.CharField(max_length=120, null=True)
    status = models.CharField(choices=STATUS, max_length=20)
    isSent = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
