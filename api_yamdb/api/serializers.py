from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import Avg
from rest_framework import serializers

from reviews.models import Category, Genre, Title
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all(),
    )
    rating = serializers.IntegerField(required=False)
    
    class Meta:
        model = Title
        fields = '__all__'


class TitleReadOnlySerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Title
        fields = '__all__'
    
    def get_rating(self, obj):
        reviews = obj.reviews.all()
        scores = []
        for review in reviews:
            if review.score != None:
                scores.append(review.score)
        if scores:
            return Avg(scores)
        return None


class AdminOrModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )
        read_only_fields = ('role',)


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        validators=[UnicodeUsernameValidator, ]
    )
    confirmation_code = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
