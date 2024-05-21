from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('url/<str:hash>/', views.redirect_original_url),
   path('url/', views.create_short_url),
   path('url/stats/<str:hash>/', views.get_url_stats),
   path('signup/', views.signup, name='signup'),
   path('login/', views.login_view, name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   #path('', views.index, name='index'),
]