from rest_framework import serializers
from .models import User


class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    password2 = serializers.CharField()

    # Настройка полей
    class Meta:
        model = User
        fields = ['number', 'password', 'password2', 'full_name','city',
                  'avatar', 'tel_number_relatives', 'name_relatives',
                  'address', 'location_access', 'role',]

    def save(self, *args, **kwargs):
        user = User(
            number=self.validated_data['number'],
            full_name=self.validated_data['full_name'],
            city=self.validated_data['city'],
            avatar=self.validated_data['avatar'],
            tel_number_relatives=self.validated_data['tel_number_relatives'],
            name_relatives=self.validated_data['name_relatives'],
            address=self.validated_data['address'],
            location_access=self.validated_data['location_access'],
            role=self.validated_data['role'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()

        return user