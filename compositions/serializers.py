from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Composition, Rating, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('user', 'composition', 'comment')


class CompositionSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        return obj.average_rating()


    class Meta:
        model = Composition
        fields = (
            'id', 'title', 'average_rating', 'type', 'release_year', 'budget',
            'premiere', 'poster', 'description', 'company', 'country',
            'genre', 'director', 'screenwriter', 'producer', 'operator',
            'сomposer', 'painter', 'editor', 'actor', 'award', 'comments'
        )


class CreateRatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = ('user', 'score', 'composition')
