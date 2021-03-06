from rest_framework import serializers
from . import models

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        user = models.UserProfile(email=validated_data['email'],
        name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = '__all__'
        #extra_kwargs = {'user_profile': {'read_only': True}}
