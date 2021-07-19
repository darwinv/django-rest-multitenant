from rest_framework import serializers
from .models import Client, Domain
from django.contrib.auth.models import User
from django_tenants.utils import schema_context


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer de customer"""

    username = serializers.CharField(required=False)

    password = serializers.CharField(required=False)

    class Meta:
        model = Client
        fields = ('id', 'name', 'paid_until', 'on_trial', 'username',
                  'password')



    # @schema_context('public')
    def create(self, validated_data):
        """Redefinido metodo de crear"""

        username = validated_data.pop('username')
        password = validated_data.pop('password')

        instance = self.Meta.model(**validated_data)
        instance.schema_name = instance.name

        instance.save()

        domain = f'{instance.name}.example.com'

        Domain.objects.create(domain=domain, tenant=instance, is_primary=True)

        with schema_context(instance.schema_name):

            user = User(username=username, is_superuser=True,
                        is_active=True, is_staff=True)

            user.set_password(password)
            user.save()

        return instance
