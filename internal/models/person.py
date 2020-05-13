from django.db import models
from internal.models.job import Job
from internal.models.city import City
from internal.models.country import Country
from internal.models.marriageStatus import MarriageStatus
from internal.models.militaryService import MilitaryService
from internal.models.personType import PersonType
from internal.models.religion import Religion

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

