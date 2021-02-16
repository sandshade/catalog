from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Link, Color, Product, OrderedItem

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=255, min_length=2)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)

    class Meta:
        model = User

        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'is_staff',
            'password',
        ]

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('Email already in use')})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'usermane': ('Username already in use')})

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
            'id',
            'url'
        ]

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'id',
            'title',
            'rbg'
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =  [
            'id',
            'title',
            'description',
            'links',
            'quantity',
            'colors',
            'registered_by',
            'date'
        ]

class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = [
            'id',
            'orderedby',
            'product',
            'quantity'
        ]