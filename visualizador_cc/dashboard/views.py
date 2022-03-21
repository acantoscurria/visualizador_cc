from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

# def index(request):
#     context = {}
#     return render(request, 'pages/dashboard/index.html', context)


class IndexView(View):
    def get(self, request):
        # <view logic>
        # return HttpResponse('result')

        context = {"result": "lala"}
        return render(request, "dashboard/index.html", context)


class GreetingView(View):
    greeting = "Good Day....."

    def get(self, request):
        return HttpResponse(self.greeting)
        # context = {'greeting': self.greeting}
        # return render(request, 'pages/dashboard/greeting_view.html', context)


class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"

    # response = {
    #     'id': '1',
    #     'name': 'lala'
    # }

    # context = {'greeting': self.greeting}
    # return render(request, 'pages/dashboard/greeting_view.html', context)
