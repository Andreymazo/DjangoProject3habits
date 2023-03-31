from django.contrib.auth.views import LogoutView
from django.urls import path, re_path
from rest_framework import serializers, viewsets, routers

# from rest_framework.authtoken.admin import User
from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserLoginView, SignupView, change_status, Habit_listAPIView, Habit_createAPIView, \
    Habit_updateAPIView, Habit_deleteAPIView, UserUpdateViewWithHabit, UserListView, UserView

app_name = UsersConfig.name
##################################Docum
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


##################################################
router = DefaultRouter()
# router = routers.DefaultRouter()
# router.register(r'users', Habit_listAPICreateView)
router.register(r'habit_list', Habit_listAPIView.as_view(),
                basename='habit_list')  # template_name='users/habit_list.html'

urlpatterns = [
    # path('', mailing, name='login'),

    path('', UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', SignupView.as_view(), name='register'),

    path('logout/', LogoutView.as_view(), name='logout'),

    # path('register/', CustomRegisterView.as_view(template_name='users/register.html'), name='register'),
    path('habit_list/', Habit_listAPIView.as_view(), name='habit_list'),
    path('habit_create/', Habit_createAPIView.as_view(), name='habit_create'),
    path('habit_update/<int:pk>/', Habit_updateAPIView.as_view(), name='habit_update'),
    path('habit_delete/', Habit_deleteAPIView.as_view(), name='habit_delete'),
    path('status/<int:pk>/', change_status, name='status'),
    path('user_list/', UserListView.as_view(template_name='mailing/Client_list.html'), name='Client_list'),
    path('user_view/<int:pk>', UserView.as_view(template_name='mailing/Client_create.html'), name='Client_create'),

    path('user_update/<int:pk>/subjects/',
         UserUpdateViewWithHabit.as_view(template_name='mailing/user_withsubject.html'), name='Client_withsubject'),
    # path('user_update/<int:pk>/subjects/',
    #      HabitUpdateViewWithSubject.as_view(template_name='mailing/user_withsubject.html'), name='Client_withsubject'),

        re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
