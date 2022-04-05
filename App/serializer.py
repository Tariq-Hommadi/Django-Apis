from rest_framework import serializers
from App.models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        feilds = ('Id', 'name', 'roll')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = '__all__'
        fields = ('Id', 'userID', 'task', 'dueDate', 'status')
        extra_kwargs = {'Id': {'required': False}, 'userID': {'required': False}, 'task': {
            'required': False}, 'dueDate': {'required': False}, 'status': {'required': False}}
