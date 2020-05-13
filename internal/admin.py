from django.contrib import admin
from internal.models import *
from internal.models.placeType import PlaceType

admin.site.register(PersonType)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(MarriageStatus)
admin.site.register(MilitaryService)
admin.site.register(Religion)
admin.site.register(Post)
admin.site.register(PlaceType)
admin.site.register(JobGroup)
admin.site.register(Job)
admin.site.register(Person)
