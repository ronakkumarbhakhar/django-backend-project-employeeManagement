from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import EmployeeSerializer, AttendanceSerializer, SalarySerializer ,UserRegistration
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Employee, Salary, Attendance
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .permissions import IsEmployer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
# Create your views here.

# customizing auth token class to return extra info with token ------------- 
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        print(request.data)                                   
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            user = User.objects.get(username=username)
            token = Token.objects.get_or_create(user=user)
            data={}
            data['token']=token[0].key
            data['user_id']=user.id
            print(data)
            return Response(data)

# ----------------------------------------------------------------------------
# views for project-----------------------------------------------------------
class EmployeeListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        return Employee.objects.filter(employer_id = self.kwargs['employer_id'])

class EmployeeDetailview(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    permission_classes =[IsAuthenticated]
    serializer_class = EmployeeSerializer

class AttendanceListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    def get_queryset(self):
        return Attendance.objects.filter(employer_id = self.kwargs['employer_id'])

class SalaryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    def get_queryset(self):
        return Salary.objects.filter(employer_id = self.kwargs['employer_id'])

@api_view(['POST'])
def user_registration_view(request):
    if request.method == 'POST':
        serialize = UserRegistration(data=request.POST)
        if serialize.is_valid():
            data={}
            serialize.save()
            user = User.objects.get(username=serialize.validated_data['username'])
            token = Token.objects.create(user=user)
            data['token']=token.key
            data['user_id']=user.id
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response({'error':'data entered is not valid'})

   
    error ={'error':'method is not post please send post method'}
    return Response(error)

@api_view(['DELETE'])
def user_logout_view(request,employer_id):
    if request.method == 'DELETE':
        token = Token.objects.get(user_id=employer_id)
        token.delete()
        return Response({'data':'token deleted successfully'},status=status.HTTP_204_NO_CONTENT)