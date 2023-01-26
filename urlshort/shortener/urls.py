from django.urls import path

from shortener.views import URLShortView, URLStatisticsView, URLShortRedirectView


urlpatterns = [
    path('shortener/', URLShortView.as_view(), name='shortener'),
    path('statistics/', URLStatisticsView.as_view(), name='statistics'),
    path('<str:short_url>/', URLShortRedirectView.as_view(), name='redirect')
]
