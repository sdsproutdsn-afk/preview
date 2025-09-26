from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, RegisterUserView, UserLoginView

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    # User auth (still direct URLs)
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('login/', UserLoginView.as_view(), name='user-login'),

    # Contacts (auto-generated routes)
    path('', include(router.urls)),
]
