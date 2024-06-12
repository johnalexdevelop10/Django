from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    #ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    #ex: /polls/9/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #ex: /polls/9/results
    path("<int:pk>/result/", views.ResultView.as_view(), name="result"),
    #ex: /polls/9/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

 ##path("", views.index, name="index"),
    #ex: /polls/9/
    ##path("<int:question_id>/", views.detail, name="detail"),
    #ex: /polls/9/results
    ##path("<int:question_id>/result/", views.result, name="result"),
    #ex: /polls/9/vote
    ##path("<int:question_id>/vote/", views.vote, name="vote"),