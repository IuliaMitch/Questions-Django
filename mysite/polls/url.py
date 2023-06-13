from django.urls import path
from . import views

urlpatterns =[
    path('', views.Index, name='index'),
    path('/<int:question_id>/vote/', views.Vote, name='vote'),
    path('/<int:question_id>/', views.Detail, name='detail'),
    path('/<int:question_id>/results/', views.Results, name='results')
]