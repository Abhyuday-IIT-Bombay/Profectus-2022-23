from rest_framework import serializers
from . models import Account

class AccountSerializer(serializers.Serializer):
     name = serializers.CharField( max_length=50, default = "")
     email = serializers.EmailField( max_length=254 , default="")
     contact = PhoneNumberField()


     def create(self, validated_data):
         return Account.objects.create(validated_data)


     def update(self,instance, validated_data):
         instance.name = validated_data.get('name', instance.title)
         instance.email = validated_data.get('email',instance.email)  