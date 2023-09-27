from django.contrib import admin
from django.urls import path
from studentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homeview, name='home'),
    path('delete/<int:id>', views.deleteview, name='delete'),
    path('edit/<int:id>', views.editview, name='edit'),
]
