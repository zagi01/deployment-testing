from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("authentication/", include("projecty.urls")),
    path('admin/', admin.site.urls),
]
