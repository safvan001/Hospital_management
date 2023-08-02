from django.urls import path,include
from app import views
app_name='app'

urlpatterns = [
    path('',views.base,name='base'),
    path('create_admin/', views.create_admin, name='create_admin'),
    path('admin_list/', views.admin_list, name='admin_list'),
    path('admin_edit/<int:pk>/', views.admin_edit, name='admin_edit'),
    path('admin_delete/<int:pk>/', views.admin_delete, name='admin_delete'),
    path('admin/', include('django.contrib.auth.urls')),
]

