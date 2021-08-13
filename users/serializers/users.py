""" Users Serializers """

#Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Models
from django.contrib.auth.models import User
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """ Profile model serializer """

    class Meta:
        model = Profile
        fields = ['age', 'city', 'country', 
                  'state', 'user_image',
                  'enrollment', 'zip_code', 
                  'carrer', 'grade', 'school']

class UserSerializer(serializers.ModelSerializer):
    """ User Serializer """

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'profile']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.age =  profile_data.get('age', profile.age)
        profile.city =  profile_data.get('city', profile.city)
        profile.state =  profile_data.get('state', profile.state)
        profile.grade =  profile_data.get('grade', profile.grade)
        profile.school =  profile_data.get('school', profile.school)
        profile.carrer =  profile_data.get('carrer', profile.carrer)
        profile.country =  profile_data.get('country', profile.country)
        profile.zip_code =  profile_data.get('zip_code', profile.zip_code)
        profile.enrollment =  profile_data.get('enrollment', profile.enrollment)
        profile.user_image =  profile_data.get('user_image', profile.user_image)
        profile.save()

        return instance
        

class NewUserSerializer(serializers.ModelSerializer):
    ''' Return the data for a new user '''
    
    class Meta:
        model = User
        fields = ['username']