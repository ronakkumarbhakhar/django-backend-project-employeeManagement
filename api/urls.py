from django.urls import path,include
from .views import EmployeeListCreateView ,AttendanceListCreateView, SalaryListCreateView, user_registration_view, CustomAuthToken, user_logout_view
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('employees/<int:employer_id>/',EmployeeListCreateView.as_view()),
    path('attendance/<int:employer_id>/',AttendanceListCreateView.as_view()),
    path('salary/<int:employer_id>/',SalaryListCreateView.as_view()),
    # path('api-auth/login/',obtain_auth_token,name='login'),
    path('api-auth/login/',CustomAuthToken.as_view(),name='login'),
    path('api-auth/registration/',user_registration_view,name='register'),
    path('api-auth/logout/<int:employer_id>/',user_logout_view,name='logout'),
    ]
