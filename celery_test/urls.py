from django.urls import path
from . import views


urlpatterns = [
    path('<int:n>', views.index)
]
