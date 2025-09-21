



from django.urls import path,include
from .views import Roomview

urlpatterns = [
    path('home/', Roomview.as_view())
]