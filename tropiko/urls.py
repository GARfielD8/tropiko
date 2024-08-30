from django.urls import path
from .views import tropikoview


urlpatterns = [
    path('', tropikoview, name='tropiko')
]