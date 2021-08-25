from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
# template_name='common/login.html' 를 넣지 않으면 registration/login.html 에러가 발생
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
path('signup/', views.signup, name='signup'),
]