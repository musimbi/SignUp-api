from django.urls import path, include
from new import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('restricted/', views.restricted),
    path('register/', views.registration),

]