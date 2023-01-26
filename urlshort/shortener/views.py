from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, ListView

from shortener.services.urls import create_shortened_url, get_url
from shortener.models import URL


class URLShortView(View):
    template_name = 'shortener/shortener.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        url = create_shortened_url(original_url=request.POST['url'])
        return render(request, self.template_name, context={'url': url})


class URLShortRedirectView(View):
    def get(self, _, short_url: str):
        return HttpResponseRedirect(get_url(short_url=short_url).original_url)


class URLStatisticsView(ListView):
    model = URL
    template_name = 'shortener/statistics.html'
