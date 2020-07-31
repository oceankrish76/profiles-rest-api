from rest_framework import serializers


from django_profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing the APIView"""
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    
    # use meta class
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # passowrd field write only using extra keywordargs, dictionary inside dictionary
        # serializer validates the object
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    ## override the create function to change in particular UserProfileSerializer

    def create(self, validated_data):
        """Create and retuen a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        # user_profile should be read only
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
