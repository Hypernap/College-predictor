from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add/', views.add, name='add'),
  path('predict/', views.main, name='main'),
  path('clg/<int:cid>/', views.clg_page),
  path('auth/', views.auth, name='auth'),
  path('rate/', views.rate, name='rate'),
  path('logout/', views.user_logout, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
