from .models import Task , Category
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        

class TaskSerilizer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['title','description','priority','status','deadline','owner','category']

class CategorySerilizer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Category
        fields = ['category_name','description','owner']