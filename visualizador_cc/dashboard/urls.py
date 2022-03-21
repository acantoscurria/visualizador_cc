from django.urls import path

from visualizador_cc.dashboard.views import IndexView

# from visualizador_cc.dashboard.views import MyView
# from visualizador_cc.dashboard.views import GreetingView
# from visualizador_cc.dashboard.views import MorningGreetingView


app_name = "dashboard"
urlpatterns = [
    # path('', views.index, name='index'),
    # path('about/', MyView.as_view()),
    # path('about/', GreetingView.as_view(greeting="G'day...")),
    # path('about/', GreetingView.as_view())
    # path('about/', MorningGreetingView.as_view()),
    path("", IndexView.as_view())
]
