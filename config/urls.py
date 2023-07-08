
from django.contrib import admin
from django.urls import path
from Exercise.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('task/',home)
]
