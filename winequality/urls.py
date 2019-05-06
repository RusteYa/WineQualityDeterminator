from django.urls import path

from winequality import views
from winequality.views import HomeView, WineQualityView, WineQualityDeterminateView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('determinate', WineQualityDeterminateView.as_view(), name="determinate"),
    path('result', WineQualityView.as_view(), name="result"),
]
