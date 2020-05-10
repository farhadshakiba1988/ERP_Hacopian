from rest_framework import serializers

from web.models import Person


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        field = '__all__'