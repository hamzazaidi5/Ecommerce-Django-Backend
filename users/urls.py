from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import (
    UserViewSet, SignupView, LoginView,
)

router = DefaultRouter()


router.register("users", UserViewSet)
app_name = "users"

urlpatterns = [
    path("", include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]
