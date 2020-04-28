from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)