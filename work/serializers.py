from rest_framework import serializers

from work.models import Profile, Post, Friend, AddExperience, PostImgs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"


class AddExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddExperience
        fields = "__all__"


class PostImgsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImgs
        fields = "__all__"

