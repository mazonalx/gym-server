from rest_framework import serializers
from apps.customers.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    bio = serializers.CharField(allow_blank=True, required=False)
    age = serializers.IntegerField(min_value=18,max_value=40)
    gender = serializers.CharField(source='get_gender_display')
    phone = serializers.CharField(allow_blank=True, required=False)
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = UserProfile
        fields = ['username','bio', 'age','gender','phone','avatar',]
        read_only_fields = ('username',)
    def get_avatar(self, obj):
        if obj.avatar:
            return obj.avatar

        return 'https://static.productionready.io/images/smiley-cyrus.jpg'