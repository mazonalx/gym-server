from rest_framework import fields, serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from api.v1.customers.serializers import UserProfileSerializer

CustomUser = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomUser
        fields = ['id','email','username','password','password2','first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    def create(self,validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        return user
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(write_only=True)
    bio = serializers.CharField(source='profile.bio', read_only = True)
    age = serializers.IntegerField(source='profile.age', read_only = True)
    gender = serializers.CharField(source='profile.gender', read_only = True)
    phone = serializers.CharField(source='profile.phone', read_only = True)
    avatar = serializers.CharField(source='profile.avatar', read_only = True)
    
    class Meta:
        model = CustomUser
        fields = ['email','username','first_name', 'last_name',
                  'profile','bio','age','gender','phone','image']
        #read_only_fields = ['token',]
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        profile_data = validated_data.pop('profile', {})
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        if password is not None:
            instance.set_password(password)
        instance.save()

        for(key,value) in profile_data.items():
            setattr(instance.profile, key, value)
        instance.profile.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        # Add extra responses here
        data['username'] = self.user.username
        return data
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only = True, required = True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'password2')
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value
    def save(self, **kwargs):
        password = self.validated_data['password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user
        