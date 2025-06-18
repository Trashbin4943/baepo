from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', UserList.as_view())
]