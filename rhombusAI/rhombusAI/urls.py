from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import reverse_lazy
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordChangeDoneView
from rest_framework import routers
import authentication.views as authentification_views
import types_converter.views as types_converter_views

router = routers.SimpleRouter()
router.register('file', types_converter_views.UploadedFileViewSet, basename='file')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(
        template_name = 'authentication/login.html',
        redirect_authenticated_user = True), name="login"),
    path("logout/", authentification_views.logout_user, name="logout"),
    path('password_change/', 
        authentification_views.MyPasswordChangeView.as_view(
            template_name='authentication/password_change.html',
            success_url='/password_change/done/'
        ), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'
    ), name='password_change_done'),
    path("home/", types_converter_views.home, name="home"),
    path("signup/", authentification_views.signup_page, name="signup"),
    path("photo/profile", authentification_views.photo_profile, name="photo_profile"),
    path('data_type_converter/', include('types_converter.urls')),
    #TODO Set up an authentication system for the API
    # path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
