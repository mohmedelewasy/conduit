from rest_framework import serializers
from profiles import models

class RegistrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=60)
    class Meta:
        model = models.Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True , },
            'password2': {'write_only': True , 'input_type': 'password'},
        }

    def save(self):
        new_account = models.Profile(
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            email = self.validated_data['email']
            )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError('password must match')

        new_account.set_password(password)
        new_account.save()
        return new_account