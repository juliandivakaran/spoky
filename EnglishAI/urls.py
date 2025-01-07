from django.urls import path

from .views import indexView

urlpatterns = [
    path("hello/", indexView.as_view(), name="hello"),

]