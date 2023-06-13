from django.urls import path
from . import views

app_name = 'polls'

urlpatterns =[
    path('', views.Index, name='index'),
    path('<int:question_id>/vote/', views.Vote, name='vote'),
    path('<int:question_id>/results/', views.Results, name='results')
]