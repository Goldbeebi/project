from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from home.views import BlogViewSet, CommentViewSet

router = DefaultRouter()
router.register('blog', BlogViewSet)
router.register('comment',CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('dj_rest_auth.urls')), # 로그인, 로그아웃
    path('accounts/register/', include('dj_rest_auth.registration.urls')), #회원가입
    path('accounts/', include('accounts.urls')),
    path('', include(router.urls)) # localhost:8000/blog/
]
 