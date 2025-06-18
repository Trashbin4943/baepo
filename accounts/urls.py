from django.urls import path
from .views import UserList

app_name = 'accounts'

urlpatterns = [
    path('', UserList.as_view())
]