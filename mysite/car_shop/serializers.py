from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class OwnerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status_owner')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Owner.objects.create_user(**validated_data)
        return user


class ClientRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Client.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'picture']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = ['carmake_name']


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ['carmodel_name']


class GenerationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generation
        fields = ['generation']


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['image']


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    user = UserProfileSerializer()
    class Meta:
        model = Review
        fields = ['user', 'parent', 'created_date']


class StateNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateNumber
        fields = ['body_number']


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    carmake = CarMakeSerializer()
    carmodel = CarModelSerializer()
    generation = GenerationSerializer()
    image = CarImageSerializer(many=True, read_only=True)
    year = serializers.DateField(format='%Y')

    class Meta:
        model = Car
        fields = ['id', 'image', 'carmake', 'carmodel', 'generation', 'price', 'year', 'modification', 'transmission', 'car_body', 'engine',
                  'rule', 'mileage', 'address_country']


class CarDetailSerializer(serializers.ModelSerializer):
    carmake = CarMakeSerializer()
    carmodel = CarModelSerializer()
    generation = GenerationSerializer()
    image = CarImageSerializer(many=True, read_only=True)
    rating = ReviewSerializer(read_only=True, many=True)
    year = serializers.DateField(format='%Y')

    class Meta:
        model = Car
        fields = ['image', 'carmake', 'carmodel', 'generation', 'year', 'mileage', 'car_body', 'color', 'modification', 'engine', 'transmission', 'drive',
                  'rule', 'state', 'customs_kyrgyzstan', 'change','stock_kyrgyzstan', 'address_country', 'register_country', 'other',
                  'description', 'appearance', 'salon', 'security', 'rating']


class CarMakeSimpleSerializer(serializers.ModelSerializer):
    carmake = CarListSerializer(many=True, read_only=True)
    class Meta:
        model = CarMake
        fields = ['carmake']


class CategoryDetailSerializer(serializers.ModelSerializer):
    category = CarMakeSimpleSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ['category_name', 'category']


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'