from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserDetailView, AdminUserViewSet, AdminDeleteUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="User Management API",
        default_version='v1',
        description="API documentation for the User Management API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'admin/users', AdminUserViewSet, basename='admin-users')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_api'),
    path('login/', LoginView.as_view(), name='login_api'),
    path('user/', UserDetailView.as_view(), name='user-detail_api'),   
    path('admin/users/<int:id>/', AdminDeleteUserView.as_view(), name='admin-delete-user_api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair_api'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh_api'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    
]

