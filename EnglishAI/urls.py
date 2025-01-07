from django.urls import path

from .views import indexView,get_voice

urlpatterns = [
    path("hello/", indexView.as_view(), name="hello"),
    path("voiceAI/", get_voice, name="voiceAI"),

]