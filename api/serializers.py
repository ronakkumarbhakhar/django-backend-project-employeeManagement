from rest_framework import serializers
from .models import Employee, Salary, Attendance 
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    # employer_details = serializers.SerializerMethodField()
    
    class Meta:
        model =Employee
        fields = '__all__'
    
    # def get_employer_details(self,obj):
    #     id = obj.employer_id
    #     employer_details = User.objects.get(id=id)
    #     return employer_details

class AttendanceSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    date = serializers.DateField(read_only=True)
    present = serializers.BooleanField(default=False)
    employer_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        return Attendance.objects.create(**validated_data)
   
class SalarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Salary
        fields = '__all__'

class UserRegistration(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True)
    class Meta:
        model= User
        fields=['email','username','first_name','last_name','password','password2']
        extra_kwargs = {'password': {'write_only': True}}
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error':'p1 and p2 not same'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email already in use'})
        
        account = User(email=self.validated_data['email'],username=self.validated_data['username'],last_name=self.validated_data['last_name'],first_name=self.validated_data['first_name'])
        account.set_password(password)
        account.save()

        return account
