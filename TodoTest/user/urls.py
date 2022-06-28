from django.urls import path

from .views import logout, Login, SignUp, ViewProfile, UpdateProfile

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('profile/', ViewProfile.as_view(), name='view_profile'),
    path('edit_profile/', UpdateProfile.as_view(), name='edit_profile'),
]