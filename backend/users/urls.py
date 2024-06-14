from django.urls import path

from users.views import (
    IndexView,
    UserLoginView,
    UserRegisterView,
    logout,
    UserProfileView,
    update_client_status
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
    path('update_client_status/<int:client_id>/', update_client_status, name='update_status')
]
