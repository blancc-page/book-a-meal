from rest_framework.serializers import  ModelSerializer
from .models import *

class CustomUserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'is_customer', 'is_caterer')

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('account')
        print(user_data)
        user = CustomUser.objects.create(**user_data)
        customer = Customer.objects.create(account=user, **validated_data)
        return customer
        

class CatererSerializer(ModelSerializer):
    class Meta:
        model = Caterer
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'